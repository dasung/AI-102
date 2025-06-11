from azure.core.credentials import AzureKeyCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
import config

def get_azure_key_credential():
    """
    Authenticates to Azure Key Vault and returns AzureKeyCredential for AI service.
    """
    credential = ClientSecretCredential(config.APP_TENANT, config.APP_ID, config.APP_PASSWORD)
    keyvault_client = SecretClient(config.KEY_VAULT_URI, credential)
    secret_key = keyvault_client.get_secret(config.SECRET_NAME)
    cog_key = secret_key.value

    print('Project Key:', secret_key.value)

    return AzureKeyCredential(cog_key)

def get_token_credential():
    """
    Authenticates to Azure using ClientSecretCredential and returns a TokenCredential for use with Azure SDK clients (such as AgentsClient).
    """
    credential = ClientSecretCredential(config.APP_TENANT, config.APP_ID, config.APP_PASSWORD)
    return credential
