
# 4] Azure AI Language Studio (To create your NLP App)
### 4.1] Azure AI Language Service:
   * Language detection
   * Key phrase extraction - text that indicate the main topics or core concepts
   * Sentiment analysis - how positive or negative the text is
   * Named entity recognition - people, locations, time periods, organizations ..
   * Entity linking - providing reference links to Wikipedia articles

![text-analytics-resource](./images/text-analytics-resource.png)

### 4.2] Create QnA Solusion with Azure AI Language Resource

   [Why Knowladge base is needed ?](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/02-qna.html)
         ```
         Azure AI Language includes a question answering capability that enables you to create a knowledge base of question and answer pairs that can be queried using natural language input.
         Create a question answering project in Azure AI Language Studio.
         ```
```mermaid
flowchart TD
   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      R[Azure AI Language service]:::box
      X[enable the Question Answering feature]:::box 
      Y[Add Storage account]:::box
      Z[add Storage Blob Data Contributor]:::box
      
      R --> X --> Y --> Z
   end
   subgraph Horizontal2[Create&nbsp;Custom&nbsp;Question&nbsp;Answering&nbsp;Project]
      direction LR
      C[Enter basic information]:::box
      D[Add sources - url to the knowledge base]:::box
      E[Edit the knowledge base]:::box
      G[Train and test the knowledge base]:::box
      H[Deploy the knowledge base]:::box
      C --> D --> E --> G --> H
   end
   a[Azure Portal]:::box --> Horizontal1
   Horizontal1 --> A
   A[Language Studio portal]:::box
   A --> Horizontal2 --> F[Client's code: QuestionAnsweringClient]:::box
   F --> K[Test app with get_answers]:::box

     %% Styling
    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#107C10,color:white,stroke:#107C10
    style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
    style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```
### 4.3] Build a Conversational Language Understanding Model
### Pre-configured features of Azure AI Language service :  features without any model labeling or training
   * Language detection
   * Key phrase extractions
   * Sentiment analysis 
   * Named entity recognition
   * Entity linking
   * Summarization
### Learned features of Azure AI Language service :  require you to label data, train, and deploy your model
   [Why CLU is needed ?](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/03-language-understanding.html)
      ```
      CLU - To interpret natural language input from users, predict the users intent (what they want to achieve), and identify any entities to which the intent should be applied.
      Create a conversational language understanding project in Azure AI Language Studio.
      ```
   * Conversational language understanding (CLU)
   * Question answering
   * Custom named entity recognition
   * Custom text classification
### 4.4] Create a custom text classification solution
### Azure AI Language project life cycle
   ![classify-development-lifecycle-small](./images/classify-development-lifecycle-small.png)
   ```
   Create a custom text classification project in Azure AI Language Studio.
   ```
   * When labeling multiple label projects, you can assign as many classes that you want per file
   ![single-multiple-graphic-small](./images/single-multiple-graphic-small.png)

#### Azure AI Languge [Evaluation metrics](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/concepts/evaluation-metrics?azure-portal=true)
   * Model evaluation is triggered automatically after training  custom text classification.
      * Recall - How many true-positives lables were identified
      `Recall = #True_Positive / (#True_Positive + #False_Negatives)`
      * Precision - How many of the predicted labels are correct
      `Precision = #True_Positive / (#True_Positive + #False_Positive)`
      * F1 Score - A function of recall and precision, seek seek a balance between precision and recall.
      `F1 Score = 2 * Precision * Recall / (Precision + Recall)`
### 4.5] Custom named entity recognition

   - [Why custom NER?](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/05-extract-custom-entities.html) 
     -  When the entities you want to extract are not included in the built-in services
     - Knowladge Miniing and improve search results
   - Defined your custom entity clearly


```mermaid
flowchart TD
   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      X[Azure AI Language service]:::box --> Y[Add Storage account]:::box
      Y --> Z[add Storage Blob Data Contributor]:::box
   end
   subgraph Horizontal2[Custom NER project]
      direction LR
      M[Upload sample ads]:::box
      C[Label your data]:::box
      D[Add entity]:::box
      E[Train your model]:::box
      G[Evalate your model]:::box
      H[Deploy your model]:::box
      M --> C --> D --> E --> G --> H
   end
   a[Azure Portal]:::box --> Horizontal1
   Horizontal1 --> A
   A[Language Studio portal]:::box
   A --> Horizontal2 --> F[Client's code: TextAnalyticsClient ]:::box
   F --> K[Test app for custom entitties]:::box

     %% Styling
    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#107C10,color:white,stroke:#107C10
    style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
    style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```


### 4.6] Translate text with Azure AI Translator service

### 4.7] Create speech-enabled apps with Azure AI services

### Azure Speech Recognition [Speech-to-text API](https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/3-speech-to-text)
![speech-to-text](./images/speech-to-text.png)

### Azure Speech Synthesis [text-to-speech API](https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/4-text-to-speech)
![text-to-speech](./images/text-to-speech.png)

### 4.8] Translate speech with the Azure AI Speech service

### [Speech translation](https://learn.microsoft.com/en-us/training/modules/translate-speech-speech-service/3-translate-speech-text) using the Azure AI Speech SDK
![translate-speech-small](./images/translate-speech-small.png)

### 4.9] Develop an audio-enabled generative AI application