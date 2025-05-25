# 2.2] Choose and deploy models from the model catalog in Azure AI Foundry portal

### Key enterprise requirements for Model usage:
   * Data and privacy: you get to decide what happens with your data.
   * Security and compliance: built-in security.
   * Responsible AI and content safety: evaluations and content safety.

### How to scale for real-world workloads:
   * Model deployment: Where will you deploy the model for the best balance of performance and cost?
   * Model monitoring and optimization: How will you monitor, evaluate, and optimize model performance?
   * Prompt management: How will you orchestrate and optimize prompts to maximize the accuracy and relevance of generated responses?
   * Model lifecycle: How will you manage model, data, and code updates as part of an ongoing Generative AI Operations (GenAIOps) lifecycle?

## Optimize model performance:

   * Apply prompt patterns to optimize your model's output
[Prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering?tabs=chat) - The process of designing and optimizing prompts to improve the model's performance 
   * Instruct the model to act as a persona
[system prompt] - As a developer, add instructions to guide your model without exposing the end user
[user prompt] - messages from end users
   * Ask for better question suggestions
   * Add context - to help improve the relevance of its response.

## Apply model optimization strategies

   * RAG - A technique when using a data source to provide grounding context to prompts.
   * Fine-tuning - A technique when training of a model by providing example prompts and responses.

# 2.3] Develop an AI app with the Azure AI Foundry SDK
[Summary]
By using the Azure AI Foundry SDK, you can develop rich AI applications that use resources in your Azure AI Foundry projects. The Azure AI Foundry SDK AIProjectClient class provides a programmatic proxy for a project, enabling you to access connected resources and to use service-specific libraries to consume them.

# 2.4] Get started with prompt flow
   * [Prompt flow] - a feature within Azure AI Foundry that allows you to author flows.

# 2.5] Develop a RAG-based solution 
   * Azure AI Search resource: Manage indexing and querying.
   * Azure AI Services resource: To enrich the data in the data source with AI-generated insights.
   * Create a storage account:  The documents to be searched are stored.

   * Identify the need to ground your language model with Retrieval Augmented Generation (RAG).
   * Index your data with Azure AI Search to make it searchable for language models.
   * Build an agent using RAG on your own data in Azure AI Foundry.
