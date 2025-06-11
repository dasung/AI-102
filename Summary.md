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
#### Microsoft Entra ID authentication
   - Client applications are authenticated by using a Microsoft Entra ID token for credentials that have permission to access the Azure AI Vision resource in Azure.

###### <span style="color: green;font-weight: bold; font-size: 16px;">When developing and testing an application, it's common to use key-based authentication or Microsoft Entra ID authentication based on your own Azure credentials. In production, consider using Microsoft Entra ID authentication based on a managed identity for your Azure application or use Azure Key Vault to store authorization keys securely.</span>

---

### How to Architec AI into massive set of Data in an Organization
 - [Margie's Travel agency's document indexing AI Design](https://learn.microsoft.com/en-us/training/modules/create-azure-cognitive-search-solution/1-introduction) with Azure AI Search

