# 3. Secure Azure AI Services
## Consider Authentication
### Authentication Ways
- Authentication Keyas
- `Azure Key Vault Service`
- Subcription Keys - Token Based authentication
- Microsoft Entra ID authentication
### Authenticate using service principals
## Implement network security
- Network Access Restrictions
- CConfigure Access Rules


# 4. Monitor AI Services
- Monitor cost (Pricing Calculator)
- Cost analysis
- Create alerts
- View metrics
- Manage diagnostic logging

# 5. Deploy AI Services in Containers

- Containers enable you to host Azure AI services either on-premises or in Azure.
- Now your data can stay on your local network and not be passed to the cloud.
- container on-premises will also decrease the latency between the service and your local data, which can improve performance.

### What is a Container?
- A container is abstracting the underlying operating system and hardware of a service.
- Usually [container image deploy to a container host](https://learn.microsoft.com/en-us/training/modules/investigate-container-for-use-with-ai-services/2-understand-containers).
  - A Docker* server.
  - An Azure Container Instance (ACI).
  - An Azure Kubernetes Service (AKS) cluster.

### Data Secure with Containers?
- When using Azure AI services containers, the model is downloaded to the container image.
  - Eg: Azure [container image for Sentiment Analysis](https://learn.microsoft.com/en-us/training/modules/investigate-container-for-use-with-ai-services/3-use-ai-services-container)
  - mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment
-  The model locally on Docker host while keeping the data processing within your environment. 
-  Container must periodically connect to Azure to send usage metrics for billing

# 6. AI Responsibility and Content Safety