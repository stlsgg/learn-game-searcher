"""
settings for the app here.
"""
from dotenv import load_dotenv
from os import getenv

load_dotenv()

MODEL=getenv("MODEL")
EMB_MODEL=getenv("EMB_MODEL")
BASE_URL=getenv("BASE_URL")
API_KEY=getenv("API_KEY")
DB_NAME=getenv("DB_NAME")
DB_USER=getenv("DB_USER")
DB_PASS=getenv("DB_PASS")
DB_ADDR=getenv("DB_ADDR")
