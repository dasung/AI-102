
# Azure AI Foundry - To Explore
## Hub (==for enterprice ML==)
### Azure AI Hub Resources
   - Storage
   - Compute
   - Specialized tools
### Project
#### Resource Group
##### Azure AI Foundry Resource
   - [Resource authorization](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/03-Use-prompt-flow-chat.html)
   - [Audio-enabled generative AI App](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/09-audio-chat.html)
      - Phi-4-multimodal-instruct
### Project Properties
#### [Fine-tuning](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/05-Finetune-model.html)
   - _TrainingData.jsonl_
#### [Prompt-flow](https://learn.microsoft.com/en-us/training/modules/get-started-prompt-flow-ai-studio/1-introduction)
#### Content Understanding
## Project (Single/Multi service AI Resource)
###  <span style="color: red; font-weight: bold; background-color: black; font-size: 16px; padding: 8px 8px; display: inline-block;">Default Azure AI Services</span>

#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Language Service</span>
##### Pre-configured Features
   - Question answering
   - Language detection
   - Key phrase extraction
   - Sentiment analysis
   - Entity linking
   - Summarization
##### Learned Features
   - Conversational language understanding [(CLU)](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2a-understand-prebuilt-capabilities)
      - intents
      - utterances
      - entities
   - [Custom text classification](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2a-understand-prebuilt-capabilities)
   - [Custom named entity recognition](https://learn.microsoft.com/en-us/training/modules/custom-name-entity-recognition/2-understand-custom-named)
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Vision Service</span>
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Foundry Service</span> - code via `Azure AI Foundry SDK`
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Speech Service</span>
   - Speech Recognition
      - `Speech-to-Text API`
   - Speech synthesis
     - `Text-to-Speech API`
   - Speech Translation
      - `Speech Translation API`
   - Keyword Recognition
   - Intent Recognition
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Translator Service</span>
   - Translation (Good afternoon)
   - Transliteration (Kon'nichiwa)
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Document Intelligence Service</span>
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Search Service</span>


### Project Properties
#### Overview
   - API Key
   - Endpoints
     - Azure AI Foundry project endpoint
     - Azure OpenAI endpoint
     - Azure AI Services endpoint
       - Speech to Text endpoint
       - Text to Speech endpoint
#### Model Catelog (==If you need a LLM model==)
   - GPT-4o-mini
   - O3
   - [GPT-4](https://learn.microsoft.com/en-us/training/modules/ai-foundry-sdk/04-chat-client?pivots=python)
      - code via `Azure AI Foundry SDK`
      - code via `Azure OpenAI SDK`
#### Models + Endpoints
   - [Model deployment](https://learn.microsoft.com/en-us/training/modules/explore-models-azure-ai-studio/4-improve-model)
   - [Embedding deployment](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html)
#### Playgrounds
   - System Prompt
   - [Default content filter](https://learn.microsoft.com/en-us/training/modules/responsible-ai-studio/6-operate-responsibly)
      - Remove content filter

#### Protect and govern
   - Guardrails + controls
      - Custom content filter
   - Evaluation
      - Manual _(Evaluation_Data.jsonl)_
      - Auto
#### Data + Indexes
   - Data Files
   - [Vector Indexes](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/04-Use-own-data.html) (==for RAG==)
     - Vector Search `Azure AI Search Service`

### <span style="color: yellow; font-weight: bold; background-color: black; font-size: 16px; padding: 8px 8px; display: inline-block;">Azure Foundry Agent Service</span>
####  Agents Playground
#### Model Deployment
#### Setup
##### Agent Name
##### Instructions
#### Tools
##### [Built-in tools](https://learn.microsoft.com/en-us/training/modules/build-agent-with-custom-tools/1-introduction)
   * [Knowledge tool](https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-azure/4-when-use-agent-service)
     * File search
     * Azure AI Search
   * [Code interpreter tool](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/01-agent-fundamentals.html)

##### [Custom tools](https://learn.microsoft.com/en-us/training/modules/build-agent-with-custom-tools/3-custom-tool-options)
   * Custom function - (LLM-Generated)
   * Azure Functions - (External Workflow)
   * OpenAPI specification tools
   * Azure Logic Apps

# Azure Foundry Portal - Try Yourself
## Resource Group
### AI Services Resource
#### _Microsoft-Inovated models_ 
##### <span style="color: green;">Language Service Resource</span>
   - Text AnalysisApps
     - Language detection
     - Key phrase extraction
     - Sentiment analysis
     - Entity linking
   - [Question AnsweringApp](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2a-understand-prebuilt-capabilities)
      - host [Knowladge Base](https://learn.microsoft.com/en-us/training/modules/create-question-answer-solution-ai-language/4-create-knowledge-base) via `Azure AI Search Service`
   - [CLU App](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2-understand-resources-for-building)
   - [Custom Named Entity Recognition App](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/05-extract-custom-entities.html)


##### <span style="color: green;">Translator Service Resource</span>
   - [Text TranslatorApp](https://learn.microsoft.com/en-us/training/modules/translate-text-with-translator-service/3-understand-language-detection-translation-transliteration)

##### <span style="color: green;">Speech Service Resource</span>
   - [Speech-enabled App](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/07-speech.html)
   - [Speech Translate/Synthesize App](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/08-translate-speech.html)


  #### Keys and EndPoints
 -  Key1
 -  Key2
 -  Endpoint
  #### Monitoring
  -  Create Alerts
  -  Visualize Metrics
### `ACI` Container Instances Resource
#### Overview
   - Status
   - IP Address
   - FQDN
### Azure AI Content Safety Resource
  #### Keys and EndPoints
 -  Key1
 -  Key2
 -  Endpoint
  #### Access Control
  - Role Assignments 
### Key Vault Resource
 - Keys
 - Secrets
   - _service principal_
 - Certificate

### Other Resource
   - AI agent
   - Chat Bots




