import os

# Add references
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from azure.core.credentials import AzureKeyCredential

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_connection = os.getenv("PROJECT_ENDPOINT")
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")

        key_vault_name = os.getenv('KEY_VAULT')
        app_tenant = os.getenv('TENANT_ID')
        app_id = os.getenv('APP_ID')
        app_password = os.getenv('APP_PASSWORD')

        # Get Azure AI services key from keyvault using the service principal credentials
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
        credential = ClientSecretCredential(app_tenant, app_id, app_password)
        keyvault_client = SecretClient(key_vault_uri, credential)
        secret_key = keyvault_client.get_secret("Project-Key")
        cog_key = secret_key.value

        print('Project Key:', secret_key.value)

        credential = AzureKeyCredential(cog_key)
        
        # Initialize the project client
        projectClient  = AIProjectClient(            
            credential = credential,
            endpoint=project_connection,
        )
        
        ## Get a chat client
        chat = projectClient.inference.get_chat_completions_client()

        # Initialize prompt with system message
        prompt=[
            SystemMessage("You are a helpful AI assistant that answers questions.")
        ]

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            prompt.append(UserMessage(input_text))
            response = chat.complete(
                model=model_deployment,
                messages=prompt)
            completion = response.choices[0].message.content

            print(completion)
            
            prompt.append(AssistantMessage(completion))

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()