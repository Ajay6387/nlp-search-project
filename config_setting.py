import os
# import psycopg2
# # Use environment variables for sensitive data (Best Practice)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","YOUR_OPENAI_API_KEY")
DATABASE_URL = "postgresql://postgres:Ajay%40Rajput%409555@db.rxsqnewbzxstvrmteurc.supabase.co:5432/postgres"

DB_CONFIG = {
    "user": "postgres",  
    "password": "AjayRajput@9555",
    "database": "postgres",  
    "host": "db.rxsqnewbzxstvrmteurc.supabase.co",  
    "port": "6543",
    "ssl": "require" 
}




