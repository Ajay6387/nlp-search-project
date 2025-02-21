import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = "postgresql://postgres:Ajay%40Rajput%409555@db.rxsqnewbzxstvrmteurc.supabase.co:5432/postgres"


# Raise an error if the API key is not set
if not OPENAI_API_KEY:
    raise ValueError("⚠️ OpenAI API Key is missing! Add it to the .env file.")


DB_CONFIG = {
    "user": "postgres",  
    "password": "AjayRajput@9555",
    "database": "postgres",  
    "host": "db.rxsqnewbzxstvrmteurc.supabase.co",  
    "port": "5432",
    "ssl": "require" 
}






