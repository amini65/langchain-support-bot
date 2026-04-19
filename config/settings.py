import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
    ADMIN_EMAIL= os.getenv("ADMIN_EMAIL")
    MODEL_NAME="gpt-3.5-turbo"
    TEMPERATURE= 0.7


Settings= Settings();    