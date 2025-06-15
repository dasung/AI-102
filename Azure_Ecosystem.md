
# Azure AI Foundry - To Explore
## Hub (==for enterprice ML==)
### Azure AI Hub Resources
   - Storage
   - Compute
   - Specialized tools
### Project
#### Resource Group
##### <span style="color: red; font-weight: bold; background-color: black; font-size: 18px; padding: 8px 8px; display: inline-block;white-space: pre;">Azure AI Foundry Resource [Default]<br/><br/>code via `Azure AI Foundry SDK`</span>
   - [Resource authorization](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/03-Use-prompt-flow-chat.html)
   - [Audio-enabled generative AI App](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/09-audio-chat.html)
      - Phi-4-multimodal-instruct
   - [Vision-based generative AI Chat App](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/08-gen-ai-vision.html)
      - Phi-4-multimodal-instruct
   - [Image generative AI App](https://learn.microsoft.com/en-us/training/modules/generate-images-azure-openai/4-dall-e-rest-api)
      -  DALL-E 3
### Project Properties
#### [Fine-tuning](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/05-Finetune-model.html)
   - _TrainingData.jsonl_
#### [Prompt-flow](https://learn.microsoft.com/en-us/training/modules/get-started-prompt-flow-ai-studio/1-introduction)
#### Content Understanding
## Project (Single/Multi service AI Resource)
###  <span style="color: red; font-weight: bold; background-color: black; font-size: 20px; padding: 8px 8px; display: inline-block;white-space: pre;">Azure AI Foundry Service [Default]<br/><br/>code via `Azure AI Foundry SDK`</span>

#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Language Service</span>
##### [Pre-configured Features](https://learn.microsoft.com/en-us/training/modules/analyze-text-ai-language/)
   - Detect Language
   - Extract Key phrases
   - Analyze Sentiment
   - Extract Entities ([Built-In NER](https://learn.microsoft.com/en-us/training/modules/analyze-text-ai-language/6-extract-entities))
   - Extract Linked Entities
   - Summarization
   - Question Answering
##### Learned Features
   - [Custom NER](https://learn.microsoft.com/en-us/training/modules/custom-name-entity-recognition/2-understand-custom-named)
   - Conversational language understanding [(CLU)](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2a-understand-prebuilt-capabilities)
      - intents
      - utterances
      - entities
   - [Custom text classification](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2a-understand-prebuilt-capabilities)

#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Vision Service</span>
   - [Image Analysis](https://learn.microsoft.com/en-us/training/modules/analyze-images/3-analyze-image?pivots=python)
      - VisualFeatures.TAGS
      - VisualFeatures.OBJECTS
      - VisualFeatures.CAPTION
      - VisualFeatures.DENSE_CAPTIONS
      - VisualFeatures.PEOPLE
      - VisualFeatures.SMART_CROPS
      - VisualFeatures.READ
   - [Optical character recognition (OCR)](https://learn.microsoft.com/en-us/training/modules/read-text-images-documents-with-computer-vision-service/2-options-read-text)
   - [Read text in images](https://learn.microsoft.com/en-us/training/modules/read-text-images-documents-with-computer-vision-service/4-use-read-api?pivots=python)
      - [Optical character recognition (OCR)](https://learn.microsoft.com/en-us/training/modules/read-text-images-documents-with-computer-vision-service/4-use-read-api?pivots=python)
   - [Face Analysis](https://learn.microsoft.com/en-us/training/modules/detect-analyze-recognize-faces/3-detect-analyze-faces?pivots=python)
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Custom Vision service</span>
   - [Custom Vision portal](https://learn.microsoft.com/en-us/training/modules/classify-images/2-provision-azure-resources-for-custom-vision)

#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Video Indexer service</span>
   - [Video Indexer portal](https://learn.microsoft.com/en-us/training/modules/analyze-video/2-understand-video-indexer-capabilities)
      - Insights
      - TimeLine
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Speech Service</span>
   - Speech Recognition
      - `Speech-to-Text API`
   - [Speech synthesis](https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/1-introduction)
     - `Text-to-Speech API`
   - Speech Translation
      - `Speech Translation API`
   - Keyword Recognition
   - Intent Recognition
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Translator Service</span>
   - Translation (Good afternoon)
   - Transliteration (Kon'nichiwa)
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Document Intelligence Service</span>
   - [Form Processing](https://learn.microsoft.com/en-us/training/modules/read-text-images-documents-with-computer-vision-service/2-options-read-text)
   - [Document analysis models](https://learn.microsoft.com/en-us/training/modules/work-form-recognizer/9-form-recognizer-studio)   
     - Read model
     - Layout model
   - [prebuilt models](https://learn.microsoft.com/en-us/training/modules/plan-form-recognizer-solution/4-choose-model-type)

     - Invoice model
     - Receipt model
     - W-2 tax model
   - [Custom models](https://learn.microsoft.com/en-us/training/modules/plan-form-recognizer-solution/2-understand)
     - Custom template models
     - [Custom neural models](https://learn.microsoft.com/en-us/training/modules/work-form-recognizer/6-train-custom-models)
   - [Composed models](https://learn.microsoft.com/en-us/training/modules/plan-form-recognizer-solution/4-choose-model-type)
     - multiple custom models
#### <span style="color: green;font-weight: bold; font-size: 16px;">Azure AI Content Understanding Service</span>
   - [Multimodal content extraction](https://learn.microsoft.com/en-us/training/modules/read-text-images-documents-with-computer-vision-service/2-options-read-text)
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
### <span style="color: red; font-weight: bold; background-color: black; font-size: 20px; padding: 8px 8px; display: inline-block;white-space: pre;">Azure AI Services Resource<br/><br/>via `multi service account`</span>
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

##### <span style="color: green;">Face Resource</span>
   - [Face Detection](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/03-face-service.html)

##### <span style="color: green;">Custom Vision Resource</span>
   - [Image classification](https://learn.microsoft.com/en-us/training/modules/classify-images/3-understand-image-classification)
   - [Object Detection](https://learn.microsoft.com/en-us/training/modules/detect-objects-images/3-train-object-detector)

##### <span style="color: green;">Azure AI Search Resource</span>
   - [Replicas and partitions](https://learn.microsoft.com/en-us/training/modules/create-azure-cognitive-search-solution/2-manage-capacity)
   - [search components](https://learn.microsoft.com/en-us/training/modules/create-azure-cognitive-search-solution/3-search-components)
     - Data source
     - Skillset (Enrich data with AI)
     - Indexer (Engine does indexing)
       - Knowledge stores
         - Azure Data Factory
         - Microsoft Power BI
         - Downstreaming Images
         - `Azure AI Search REST interface`
     - Index (serchble unit)
       
  #### Keys and EndPoints
 -  Key1
 -  Key2
 -  Endpoint
  #### Monitoring
  -  Create Alerts
  -  Visualize Metrics
### Storage Account Resource
   - data indexing for [Azure AI Search Service](https://microsoftlearning.github.io/mslearn-knowledge-mining/Instructions/Exercises/01-azure-search.html)
   - [knowledgeStore object](https://learn.microsoft.com/en-us/training/modules/create-knowledge-store-azure-cognitive-search/3-define-knowledge-store)
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

### Azure AI Document Intelligence resources
#### Resource Management
##### Keys and EndPoints
 -  Key1
 -  Key2
 -  Endpoint
### Other Resource
   - AI agent
   - Chat Bots




