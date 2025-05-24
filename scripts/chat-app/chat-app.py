import os

# Add references
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.identity import ClientSecretCredential

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_connection = os.getenv("PROJECT_ENDPOINT")
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")

        credential = ClientSecretCredential(
                tenant_id="40b9bc57-e3eb-4d3b-80db-ad123ac9a09a",
                client_id="0adab6d4-b8fb-4c6b-a6aa-119a4b4079f3",
                client_secret="Ooh8Q~6j~v0GjSCSzYAFpOstnlkAC1QJfXfb5b0Q",
                )
        
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