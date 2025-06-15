

# Vedio Processing App

### Use Case:
- We have some missing lectures as video to complete before the examination of "Machine Learning 101". We only interested cover specific points  like "loss function" + "overfitting". 
- Need AI app to output Auto-generated video clips tagged with key moments of the lecture. 

### Design: 
- This demonstrate how to integrate  a [custom Language model with Azure Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/customize-language-model-how-to?tabs=customizewebportal)

```mermaid
flowchart TD

    subgraph h_flow1[Vedio&nbsp;Processing&nbsp]
        direction LR
        X0[Upload Video]:::box
        X1[Azure Blob Storage]:::box 
        X2[Azure AI Video Indexer]:::box
        X3[Get Transcript generated]:::box
        
        X0 --> X1 --> X2 --> X3
    end

    subgraph h_flow2[Train&nbsp;BuiltIn&nbsp;Language&nbsp;Model&nbsp]
        direction LR
        Y0[Feed adaptation text]:::box
        Y1[Add Custom Vocabulary]:::box
        Y2[Traning]:::box
        Y3[Deploy]:::box
        Y4[Analyze Transcript/Timestamps]:::box

        Y0 --> Y1 --> Y2 --> Y3 --> Y4
    end

    %% main tree-view

    A[Azure Video Indexer portal]:::box
    C[Generate Highlight Clips]:::box
    D[Student Portal]:::box
    E[Searchable video - jumping on clickable keywords]:::box

    A --> h_flow1 --> h_flow2 --> C --> D --> E

    %% syle definition

    classDef box fill:#ECECFF,color:black
    classDef green-step fill:#107C10,color:white,stroke:#107C10
    style h_flow1 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px
    style h_flow2 fill:#FFF4BD,color:black,stroke:#FFD700,stroke-width:1px

```
---



