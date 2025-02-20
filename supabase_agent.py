import os
import traceback
import httpx
from dotenv import load_dotenv
from datetime import datetime
from time import sleep
from loguru import logger


load_dotenv()  # Load environment variables

class SupabaseFunctionCallError(Exception):
    pass

class SupabaseAgent():
    def __init__(self, timeout: int = 60):
        self.supabase_url = os.getenv("SUPABASE_ENDPOINT")
        self.supabase_key = os.getenv("SUPABASE_KEY")  # Load API key

        self.MAX_RETRIES = 3

        # Initialize the httpx client with authorization headers
        self.client = httpx.AsyncClient(
            base_url=self.supabase_url,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "apikey": self.supabase_key,
                "Authorization": f"Bearer {self.supabase_key}"
            },
            timeout=timeout
        )


    async def call_supabase_function(self, schemaname: str = None, functionname: str = None, params: dict = None):
        logger.debug(f"Calling Supabase function at URL: {self.supabase_url}")

        for attempt in range(self.MAX_RETRIES):
            logger.debug(f"Attempt {attempt + 1} of {self.MAX_RETRIES} at {datetime.now()}")
            try:
                response = await self.client.post(
                    url="/rest/v1/rpc/" + functionname,  # Supabase function endpoint
                    json={"schemaname": schemaname, "params_dict": params}
                )

                if response.status_code in [200, 201, 204]:
                    logger.success(f"Received response for '{functionname}' function.")
                    return response.json()
                else:
                    logger.warning(f"Unexpected status code {response.status_code} received.")
                    logger.error(f"The response is {response.content}")

            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error occurred: {e}. Status: {e.response.status_code}")
            except Exception as e:
                logger.error(f"An error occurred: {e}\nTraceback:\n{traceback.format_exc()}")

            if attempt < self.MAX_RETRIES - 1:
                logger.info("Retrying...")
                sleep(1)

        logger.error("Maximum retry attempts reached. Function call failed.")
        raise SupabaseFunctionCallError("Failed to call Supabase function after several attempts.")

    async def update_supabase_status(self, table_schema: str, table_name: str, id: int, status: str):
        """
        Update the status of a row in the specified table using Supabase.

        Args:
            table_schema (str): Schema name.
            table_name (str): Table name.
            id (int): Row ID.
            status (str): New status value.

        Returns:
            bool: True if successful, False otherwise.
        """
        response = await self.call_supabase_function(
            schemaname="public",
            functionname="update_using_json",
            params={
                "input_table_name": f"{table_schema}.{table_name}",
                "row_data": {"status": status},
                "condition_json": {"id": id},
            },
        )
        return response is not None



