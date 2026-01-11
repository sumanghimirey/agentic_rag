import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ROUTER_MODEL = os.getenv("OPENAI_MODEL_ROUTER")
    GENERATION_MODEL = os.getenv("OPENAI_MODEL_GENERATION")

    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PORT = os.getenv("POSTGRES_PORT")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    VECTOR_DIMENSION = int(os.getenv("VECTOR_DIMENSION"))

settings = Settings()