from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

AI_ENDPOINT = os.getenv('AI_SERVICE_ENDPOINT')
KEY_VAULT_NAME = os.getenv('KEY_VAULT')
APP_TENANT = os.getenv('TENANT_ID')
APP_ID = os.getenv('APP_ID')
APP_PASSWORD = os.getenv('APP_PASSWORD')
SECRET_NAME = os.getenv('SECRET_NAME')

KEY_VAULT_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net/"
