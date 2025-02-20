import asyncpg
import openai
from config_setting import DB_CONFIG, OPENAI_API_KEY

class QueryEngine:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.pool = None  

    async def get_connection(self):
        """Create a connection pool if it doesn't exist."""
        if self.pool is None:
            self.pool = await asyncpg.create_pool(**DB_CONFIG, statement_cache_size=0)
        return self.pool

    async def get_openai_embedding(self, text):
        """Fetch embeddings from OpenAI."""
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-3-small",
            api_key=self.api_key
        )
        return response["data"][0]["embedding"]

    async def update_embeddings(self):
        """Store OpenAI embeddings for products (if not already stored)."""
        pool = await self.get_connection()
        async with pool.acquire() as conn:
            rows = await conn.fetch("SELECT id, name FROM products WHERE embedding IS NULL")
            for row in rows:
                embedding = await self.get_openai_embedding(row["name"])
                
                # ✅ Convert embedding list to a PostgreSQL-compatible string format
                embedding_str = "[" + ",".join(map(str, embedding)) + "]"

                await conn.execute(
                    """
                    UPDATE products
                    SET embedding = $1::vector
                    WHERE id = $2
                    """,
                    embedding_str,  # ✅ Pass string instead of list
                    row["id"]
                )

    async def hybrid_search(self, query, top_k=5):
        """Perform a vector similarity search."""
        pool = await self.get_connection()
        async with pool.acquire() as conn:
            query_embedding = await self.get_openai_embedding(query)

            # ✅ Convert query embedding to PostgreSQL-compatible string format
            query_embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

            results = await conn.fetch(
                """
                SELECT id, name, embedding <=> $1::vector AS similarity
                FROM products
                ORDER BY similarity
                LIMIT $2
                """,
                query_embedding_str,  # ✅ Correctly formatted string
                top_k
            )
            return results
