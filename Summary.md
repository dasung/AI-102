#  Azure AI Foundry project
### Feature includes:
   - Generative AI model deployment
   - Agents
   - pre-built Azure AI services
     - NLP
     - Vision
     
### When:
   - If you involve collaborative development by a team of software engineers and service operators. 
     - Use Azure AI Foundry hub project
   - If you don't need all of the functionality in an Azure AI Foundry hub
     - Use Azure AI multi-service resource 
   - If you only need to use Azure AI Vision in app
     - Use a standalone Azure AI Vision resource in 
     - One benefit is the standalone service provides a free tier to explore the service at no cost.

###### <span style="color: green;font-weight: bold; font-size: 16px;"> If your project needs LLM integration & Training AI Hub project is a must.</span>
- [Audio-enabled generative AI App](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/09-audio-chat.html)

# Authentication

### For Agentic Tools - [From OpenAI Specification](https://learn.microsoft.com/en-us/training/modules/build-agent-with-custom-tools/4-how-use-custom-tools)
 - Currently, three authentication types are supported with OpenAPI 3.0 tools: anonymous, API key, and managed identity.

 ### For Azure AI Foundry project

   - To connect to the endpoint, client applications must be authenticated. 


## Options for authentication: 
[reference](https://learn.microsoft.com/en-us/training/modules/analyze-images/2-provision-computer-vision-resource)
#### Key-based authentication
   - Client applications are authenticated by passing an authorization key (which you can find and manage in the portal).
#### [Microsoft Entra ID authentication](https://learn.microsoft.com/en-us/training/modules/work-form-recognizer/3-get-started)
   - Client applications are authenticated by using a Microsoft Entra ID token for credentials that have permission to access the Azure AI Vision resource in Azure.

###### <span style="color: green;font-weight: bold; font-size: 16px;">When developing and testing an application, it's common to use key-based authentication or Microsoft Entra ID authentication based on your own Azure credentials. In production, consider using Microsoft Entra ID authentication based on a managed identity for your Azure application or use Azure Key Vault to store authorization keys securely.</span>

---

### How to Architec AI into massive set of Data in an Organization
 - [Margie's Travel agency's document indexing AI Design](https://learn.microsoft.com/en-us/training/modules/create-azure-cognitive-search-solution/1-introduction) with Azure AI Search

 ### Cognitive AI services

 - Cognitive Skill AI refers to artificial intelligence systems designed to mimic or replicate human-like cognitive abilities, such as reasoning, problem-solving, learning, perception, and decision-making. 
 - Microsoft Azure offers several Cognitive AI services under its Azure AI Services (formerly Cognitive Services) suite. These services provide pre-built AI models for vision, language, speech, decision-making, and more, allowing developers to integrate advanced cognitive capabilities into applications without building models from scratch.

 Eg:
 -  Vision AI (Image & Video Analysis)
   - Computer Vision – Analyze images
   - Video Indexer – Analyze videos for insights
- Speech AI (Voice Processing)
   - Text-to-Speech – Generate natural-sounding speech.
   - Speech Translation – Real-time speech translation.
- Language AI (Natural Language Processing)  
   - Text Analytics – Sentiment analysis, key phrase extraction.

 ### Azure AI Search services
- Azure AI Search uses an enrichment pipeline of AI skills (Cognitive Skill) to extract AI-generated fields from documents and include them in a search index.
- The index might be considered the primary output from an indexing process, the enriched data it contains might also be useful in other ways.

---

# Responsible use of AI

To ensure AI's impacts are positive on people's lives, Microsoft uses the following principles when it designs and builds AI solutions.

- Fairness:
  - All AI systems should treat people fairly, regardless of race, belief, gender, sexuality, or other factors.
- Reliability and safety:
  - All AI systems should give reliable answers with quantifiable confidence levels.
- Privacy and security:
  - All AI systems should secure and protect sensitive data and operate within applicable data protection laws.
- Inclusiveness: 
  - All AI systems should be available to all users, regardless of their abilities.
- Transparenc:
  - All AI systems should operate understandably and openly.
- Accountability:
  - All AI systems should be run by people who are accountable for the actions of those systems.


----
## Describe business problems that you would use [composed models](https://learn.microsoft.com/en-us/training/modules/create-composed-form-recognizer-model/1-introduction) to solve.
- You work for a company that conducts polls for private companies and political parties. Participants submit their responses as paper forms or as online PDFs. For each poll you conduct, respondents may complete up to three different form types but you want to analyze them with a single service. You want to create an AI service that can recognize these three form types and apply a different analysis to each. The three form types each have a different set of fields that you want to extract.