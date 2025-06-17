
## Analyze text with Azure AI Language


<table border="1">
  <tr>
    <td rowspan="5">
    <img src="./images/text-analytics-resource.png" >
    <td>1) Language detection - To determine which language is used in the input document.</td>
  </tr>
  <tr>
    <td>2) Key phrase extraction - Identify the main topics or core concepts</td>
  </tr>
  <tr>
    <td>3) Sentiment analysis - To determine how positive or negative the input text using  confidenceScores</td>
  </tr>
  <tr>
    <td>4) Named entity recognition - People, locations, time periods, organizations ..</td>
  </tr>
  <tr>
    <td>5) Entity linking - Providing reference links to Wikipedia articles</td>
  </tr>
</table>   

### Text Analysis App

#### Use Case:
- Travel agency wants to process hotel reviews that have been submitted to the company’s web site.  

#### Design: 
- Use Azure AI Language to determine the written language, the sentiment (positive, neutral, or negative), the main topics and named entities of each review.

```mermaid
flowchart TD
   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      X0[Azure AI Language service]:::box
      X1[Get Keys and Endpoint]:::box 
      
      X0 --> X1
   end

   subgraph Horizontal2[Analyze&nbsp;Results&nbsp;Using&nbsp;Client]
      direction LR
      Y0[DetectLanguage - ai_client.detect_language]:::box
      Y1[AnalyzeSentiment - ai_client.analyze_sentiment]:::box
      Y2[ExtractKeyPhrases - ai_client.extract_key_phrases]:::box
      Y3[RecognizeEntities - ai_client.recognize_entities]:::box
      Y4[RecognizeLinkedEntities - ai_client.recognize_linked_entities]:::box
      Y0 --> Y1 --> Y2 --> Y3 --> Y4
   end

   %% main tree-view
   A[Azure Portal]:::box
   B[Configure Client App]:::box
   C[Client's code: TextAnalyticsClient]:::box

   A --> Horizontal1 --> B --> C --> Horizontal2

   %% Styling
   classDef box fill:#ECECFF,color:black
   classDef green-step fill:#107C10,color:white,stroke:#107C10
   style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
   style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```

---

## Create QnA Solusion with Azure AI Language Resource

### [Why Knowladge base is needed ?](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/02-qna.html)
   -  Azure AI Language includes a question answering capability
   -  Knowledge Base is needed for store QnA pairs 
   -  Azure AI Language Studio is used for Knowledge Base.

### Diff between QnA vs Conversational language understanding


<table border="1">
  <tr>
    <th>Question answering</th>
    <th>Language understanding</th>
  </tr>
  <tr>
    <td>User submits a question, expecting an answer</td>
    <td>User submits an utterance, expecting an appropriate action</td>
  </tr>
  <tr>
    <td>Service uses natural language understanding</td>
    <td>Service uses natural language understanding</td>
  </tr>
  <tr>
    <td>match the question to an answer in the knowledge base</td>
    <td>interpret the utterance, match it to an intent, and identify entities</td>
  </tr>
  <tr>
    <td>Response is a static answer to a known question</td>
    <td>Response indicates the most likely intent and referenced entities</td>
  </tr>
  <tr>
    <td>Client application typically presents the answer to the user</td>
    <td>Client application is responsible for performing appropriate action based on the detected intent</td>
  </tr>
</table> 


### Qestion Answering App
#### Use Case:
- Many organizations publish FAQs as documents or web pages, which works well for a small set of question and answer pairs, but large documents can be difficult and time-consuming to search.

#### Design: 
- Use Azure AI Language's question answering capability that enables you to create a knowledge base of question and answer pairs.
- Most commonly company used as a Chat bot that can look up answers to questions.

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
      C[Enter basic project info]:::box
      D[Add sources - url of FAQ to the knowledge base]:::box
      E[Edit the knowledge base]:::box
      G[Train and test the knowledge base]:::box
      H[Deploy the knowledge base]:::box
      C --> D --> E --> G --> H
   end
   a[Azure Portal]:::box --> Horizontal1
   Horizontal1 --> A
   A[Language Studio portal]:::box
   A --> Horizontal2 --> F[Client's code: QuestionAnsweringClient]:::box
   F --> K[Test app with ai_client.get_answers]:::box

     %% Styling
    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#107C10,color:white,stroke:#107C10
    style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
    style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```

---

## Build a Conversational Language Understanding Model

### A common design pattern for CLU

<table border="1">
  <tr>
    <td rowspan="3">
    <img src="./images/language-understanding-app.png" >
    <td>1) An app accepts natural language input from a user.</td>
  </tr>
  <tr>
    <td>2) A language model is used to determine semantic meaning (the user's intent).</td>
  </tr>
  <tr>
    <td>3) The app performs an appropriate action.</td>
  </tr>
</table>

### [CLU Capabilities](https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/2a-understand-prebuilt-capabilities)

```mermaid
flowchart LR
   A[CLU Capabilities]:::box

   X0[Pre-configured<br>features]:::box
   Y0["• Summarization<br>(PII) detection"]:::box
   Y1["• Key phrase extraction<br>• Sentiment analysis<br>• Language detection <br>• Named entity recognition<br>• Question answering"]:::box

    
   X1[Learned features]:::box
   Z0["• CLU<br>• Custom named entity recognition<br>• Custom text classification"]:::box
   
   X3["How to Define<br> the Model"]:::green-step
   O1[Utterances]:::green-step
   O2[Intents]:::green-step
   O3[Entities]:::green-step

   %% Built-In Tools
   A ==> X0 ==> Y0 
          X0 ==> Y1

   %% Custom Tools
   A ==> X1 
   X1 ==> Z0

   %% other
   A ==> X3
   X3 --> |user input|O1 -.-> B["💡 user entered text / voice"]:::my
   X3 --> |get meaning|O2 -.-> C["💡 task or action to perform"]:::my
   X3 --> |undertand subjects|O3 -.-> D["💡 1 or more device list to apply task"]:::my



   %% invisible node
    classDef my stroke-width:0,fill:none
    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#9bf4b2,color:black,stroke:#9bf4b2
```

### Conversational Language Understanding App
#### Use Case:
- a conversational language model for a clock application might be expected to process input such as:
   - What is the time in London?
   - Tell me time in London?
   - What is UK time now?
- *NOTE - CLU can be used to identify user wants to know time in London. But client application must implement to determine the correct time and show user.*

#### Design: 
 - define a conversational language understanding model that applications can use to interpret natural language input from users, predict the users intent (what they want to achieve), and identify any entities to which the intent should be applied.

```mermaid
flowchart TD
   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      X0[Azure AI Language service]:::box
      X1[Select Pricing tier F0 -free]:::box
      X2[Agree on Responsible AI Notice]:::box
      X3[Get Keys and Endpoint]:::box 
      
      X0 --> X1 --> X2 --> X3
   end

   subgraph Horizontal2[Create&nbsp;CLU&nbsp;Project]
      direction LR
      Y0[Enter basic project info]:::box
      Y1[Add your Language Resource]:::box
      Y2[select Conversational language understanding]:::box
      Y3[Set Utterances primary language: English]:::box
      Y4[Create intents]:::box
      Y5[Label each intent with sample utterances]:::box
      Y6[Train and test the model]:::box
      Y7[Add a learned entity]:::box
      Y8[Add a list entity]:::box
      Y9[Add a prebuilt entity]:::box
      
      Y0 --> Y1 --> Y2 --> Y3 --> Y4 --> Y5 --> Y6
      Y6 --> Y7
      Y6 --> Y8
      Y6 --> Y9 --> |Retrain the model|Y6
   end

   subgraph Horizontal3[Develop&nbsp;Client&nbsp;App]
      direction LR
      D[Client's code: ConversationAnalysisClient]:::box
      E[client.analyze_conversation]:::box
      F[Find topIntent and list of entities]:::box
      G[Apply the appropriate action]:::box
      
      D --> E --> F --> G
   end

   %% main tree-view
   A[Azure Portal]:::box
   B[Language Studio portal]:::box
   C[Deploy the model]:::box


   A --> Horizontal1 --> B --> Horizontal2 --> C --> Horizontal3

   %% Styling
   classDef box fill:#ECECFF,color:black
   classDef green-step fill:#9bf4b2,color:white,stroke:#9bf4b2
   style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
   style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
   style Horizontal3 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```

---

## Create a custom text classification App

- Learn how to use the Azure AI Language service to classify text into custom groups.
 
### Use Case:
- A video game summary might be classified as "Adventure", "Strategy", "Action" or "Sports".
- [Developer defines, to text files](https://learn.microsoft.com/en-us/training/modules/custom-text-classification/2-understand-types-of-classification-projects)
### Design
- Custom text classification projects are all about [build, train, improve, and deploy your classification model](https://learn.microsoft.com/en-us/training/modules/custom-text-classification/3-understand-how-to-build-projects). 
- our labels would be "Action", "Adventure", "Strategy", and so on.
- Training will teach our model what types of video game summaries should be labeled which genre.

![classify-development-lifecycle-small](./images/classify-development-lifecycle-small.png)

```mermaid 
flowchart TD

   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      X0[Azure AI Language service]:::box
      X1[Add Storage account]:::box
      X2[Agree on Responsible AI Notice]:::box
      X3[Get Keys and Endpoint]:::box 
      
      X0 --> X1 --> X2 --> X3
   end

   %% main tree
   Horizontal1 ==> A[Define Lables]
   A ==> B[Tag Data] ==> C[Train Model]
   C ==> D[View Model] ==> |Identify weak labels|E[Improve Model] ==> F[Deploy Model]
    ==> H[Classify Text]:::green-step ==> G["💡"]:::my
   A -.-> |identify categories|info1["• Action<br>• Adventure<br>• Strategy<br>• Sports"]
   B  -.-> |label existing game summaries|info2["• Explore a lost world → Adventure<br>•  A cricket → Sport"]
   C  -.-> info3["Upload labeled data to Azure AI Language Studio"]
   D  -.-> |evaluate Model|info4["Check precision, recall, and F1-score"]
   E  -.-> |fix mislabled data|info5["Strategy mislabeled with Adventure"]
   F  -.-> |GameGenreClassifier|info6["Deployed trained model as an API endpoint"]
   H  -.-> |call the API|info7["API returns predicted label"]

   %% style definition
   classDef infoNode stroke-dasharray:5,stroke:#888
   classDef box fill:#ECECFF,color:black
   classDef green-step fill:#9bf4b2,color:black,stroke:#9bf4b2

   style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
   
   %% Apply the class to multiple nodes
   class info1,info2,info3,info4,info5,info6,info7 infoNode
   class A,B,C,D,E,F box
   
   classDef my stroke-width:0,fill:none
```
 

### Azure AI Languge [Evaluation metrics](https://learn.microsoft.com/en-us/training/modules/custom-text-classification/2-understand-types-of-classification-projects)
   * Model evaluation is triggered automatically after training  custom text classification.
   * [Correct classification] - Suppose actual label is x and the model predicts a label x.
   * For evaluation, custom text classification uses the [following metrics](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/concepts/evaluation-metrics?azure-portal=true)
      - *Precision -*  reveals how many of the predicted classes are correctly labeled
      - *Recall -* reveals how many of the predicted classes are correct.
      - *F1 Score -* is a function of precision and recall., seek seek a balance between precision and recall.
#### Example Evaluation
   - let's your model is correctly classifying "Action" games and some "Action and Strategy" games, but failing at "Strategy" games. 
   - To improve your model, you'll want to find more high quality and varied summaries for both "Action and Strategy" games, as well as "Strategy" games to teach your model how to differentiate the two.

---
## Custom Named Entity Recognition App

   - [Why custom NER?](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/05-extract-custom-entities.html) 
     -  When the entities you want to extract are not included in the built-in services
     - Knowladge Miniing and improve search results
   - Defined your custom entity clearly
### Use Case:
-  Looks at bank statements documents, identifies, and extracts user defined entities such as,
   - Person names and addresses 
   - Branch

### Design: 

![extraction-development-lifecycle.png](./images/extraction-development-lifecycle.png)


```mermaid
flowchart TD
   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      X[Azure AI Language service]:::box --> N[enable  Custom named entity recognition extraction feature]:::box
      N --> Y[Add Storage account]:::box
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
   F --> K[Test app with ai_client.begin_recognize_custom_entities]:::box

     %% Styling
    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#107C10,color:white,stroke:#107C10
    style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
    style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```

---

## Translate text with Azure AI Translator service

### [Azure AI Translator Capabilities](https://learn.microsoft.com/en-us/training/modules/translate-text-with-translator-service/3-understand-language-detection-translation-transliteration)

```mermaid
flowchart LR
   A[AI Translator]:::box

   X0[Translation]:::box
   Y0["Good afternoon"]:::my
       
   X1[Transliteration]:::box
   Z0["Kon'nichiwa"]:::my
   
   X3["<a href='https://learn.microsoft.com/en-us/training/modules/translate-text-with-translator-service/4-specify-translation-options'>Translation options</a>"]:::green-step
   O1[Word alignment]:::green-step
   O2[Sentence length]:::green-step
   O3[Profanity filtering]:::green-step

   A ==> K[Language detection]:::box  -.-> W["Text : こんにちは / ja"]:::my
   %% Built-In Tools
   A ==> X0 -.-> Y0 

   %% Custom Tools
   A ==> X1 
   X1 -.-> Z0

   %% other
   A ==> X3
   X3 --> |includeAlignment param|O1 -.-> B["💡 spaces used to seperate words?"]:::my
   X3 --> |includeSentenceLength param|O2 -.-> C["💡 how best to ssplay translated output?"]:::my
   X3 --> |profanityAction param|O3 -.-> D["💡 omit some translated parts"]:::my



   %% invisible node
    classDef my stroke-width:0,fill:none
    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#9bf4b2,color:black,stroke:#9bf4b2
```

## Text Translate App
### Use Case:
- Translates input in any supported language to the target language of your choice. 

### Design: 
- Use Azure [AI Translator](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/06-translate-text.html) translate text between languages..

```mermaid
flowchart TD
   subgraph Horizontal1[Create&nbsp;a&nbsp;Language&nbsp;Service&nbsp;resource]
      direction LR
      X0[Create Azure AI Translator resource]:::box
      X1[Get Keys and Endpoint]:::box 
      
      X0 --> X1
   end

   subgraph Horizontal2[Client&nbsp;Translation&nbsp;App]
      direction LR
      Y0[ai_client.get_languages]:::box
      Y1[ai_client.translate]:::box
      Y0 --> Y1 
   end

   %% main tree-view
   A[Azure Portal]:::box
   B[Choose target language]:::box
   C[Client's code: TextTranslationClient]:::box

   A --> Horizontal1 --> B --> C --> Horizontal2

   %% Styling
   classDef box fill:#ECECFF,color:black
   classDef green-step fill:#107C10,color:white,stroke:#107C10
   style Horizontal1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
   style Horizontal2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
```

## Create speech-enabled apps with Azure AI services

### [Azure AI Speech Service](https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/1-introduction)
   - Speech to text : speech recognition
   - Text to speech: speech synthesis
   - Speech Translation: translate spoken input
   - Keyword Recognition: to recognize keywords or short phrases
   - Intent Recognition: CLU to determine the semantic meaning of spoken input
### [1] Azure Speech Recognition [Speech-to-text API](https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/3-speech-to-text)
   - Real-time transcription: Instant transcription for live audio inputs.
![speech-to-text](./images/speech-to-text.png)

### [2] Azure Speech Synthesis [text-to-speech API](https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/4-text-to-speech)
   - convert large volumes of text to audio - generate an audio-book from the source text.
![text-to-speech](./images/text-to-speech.png)

[TODO]: [Recognize and synthesize speech app](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/07-speech.html)

### [3] [Translate speech to text](https://learn.microsoft.com/en-us/training/modules/translate-speech-speech-service/3-translate-speech-text) using the Azure AI Speech SDK

- develop a translator application that people can use when traveling in places where they don’t speak the local language. They would be able to say phrases such as “Where is the station?” or “I need to find a pharmacy” in their own language, and have it translate them to the local language.
![translate-speech-small](./images/translate-speech-small.png)

[TODO] Speech Translation APP: https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/08-translate-speech.html

### [4] Develop an audio-enabled generative AI application
#### Use Case:
- Develop a client app that engages in audio-based chats with a multimodal model 
- The key difference is that prompts for an audio-based chat include multi-part user messages that contain both a text content item and an audio content item.

### Design: 
[TODO](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Labs/09-audio-chat.html) In this exercise, you used Azure AI Foundry and the Azure AI Inference SDK to create a client application uses a multimodal model to generate responses to audio.