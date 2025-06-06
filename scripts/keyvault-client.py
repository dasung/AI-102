from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from Authenticator import get_azure_key_credential
import config

"""
    Access to Azure AI services is typically controlled through authentication keys, 
    which are generated when you initially create an Azure AI services resource.
    You can develop applications that consume Azure AI services by using this keys for authentication.
    However, store the key in an .env file is making key vulnerable to unauthorized access.
    A better approach is to store the key securely in Azure Key Vault, and provide access to the key through this Key Vault. 
    
    This app access Azure AI services to detect language after authenticating the secret in the key vault.
"""

def main():
    global ai_endpoint
    global cog_key

    try:
        # Get AzureKeyCredential from Authenticator
        azure_credential = get_azure_key_credential()
        ai_endpoint = config.AI_ENDPOINT
        # Get user input (until they enter "quit")
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                CallAxureLanguageService(userText, ai_endpoint, azure_credential)
                

    except Exception as ex:
        print(ex)

def CallAxureLanguageService(text, ai_endpoint, azure_credential):

    # Create client using endpoint and key
    ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=azure_credential)

    # call the service to get the detected language
    detectedLanguage = ai_client.detect_language(documents = [text])[0]
    print('User Input Language:', detectedLanguage.primary_language.name)

    # call service to get sentiment
    sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
    print("\nSentiment: {}".format(sentimentAnalysis.sentiment))

    # call service to get key phrases
    phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
    if len(phrases) > 0:
        print("\nKey Phrases:")
        for phrase in phrases:
            print('\t{}'.format(phrase))
    
    # call service to get entities
    entities = ai_client.recognize_entities(documents=[text])[0].entities
    if len(entities) > 0:
        print("\nEntities")
        for entity in entities:
            print('\t{} ({})'.format(entity.text, entity.category))

    # call service to extract linked entities
    entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
    if len(entities) > 0:
        print("\nLinks")
        for linked_entity in entities:
            print('\t{} ({})'.format(linked_entity.name, linked_entity.url))


if __name__ == "__main__":
    main()