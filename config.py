"""
settings for the app here.
"""
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# open settings
MODEL="qwen-local-4b:latest"
EMB_MODEL="qwen-local-embedding:latest"
BASE_URL="http://localhost:11434/v1"

# sensitive settings
API_KEY=getenv("API_KEY")
DB_NAME=getenv("DB_NAME")
DB_USER=getenv("DB_USER")
DB_PASS=getenv("DB_PASS")
DB_ADDR=getenv("DB_ADDR")
