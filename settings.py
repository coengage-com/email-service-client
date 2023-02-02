import os

from dotenv import load_dotenv

load_dotenv()

EMAIL_SERVICE_API_HOST = os.getenv("EMAIL_SERVICE_API_HOST")
