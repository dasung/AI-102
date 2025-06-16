

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

# Run Language Model in Mobile App

### Use Case:

   - You are building an Azure AI Language solution.
     - You need to deploy the solution to a location without internet connectivity.
     - What should you do?

### Design: <TODO>
   - Use model in [Docker Image container](https://learn.microsoft.com/en-us/azure/ai-services/containers/disconnected-containers)
   - Consider [Billing & Data Security](https://learn.microsoft.com/en-us/training/modules/investigate-container-for-use-with-ai-services/3-use-ai-services-container)
   - Find difference between [Export Model](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/export-your-model) vs [Deploy to Containers](https://learn.microsoft.com/en-us/training/modules/investigate-container-for-use-with-ai-services/3-use-ai-services-container)


---

# Prompth Fow App
https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/03-Use-prompt-flow-chat.html


---

#  Agent Project Idea for Gaming
Simulated (NPC) Opponents:
    * Most AI opponents follow hardcoded behavior trees
    * Sim Agent analyze the player’s strategies and counter with enemies(NPC) in real time.
Storytelling Agent:
    * Most games use pre-written dialogues
    * Conversational story teller agent could have dynamic conversations with memory of player choices.

Game Master Agent:
    * Most survival games rely on predefined gaming story.
    * Game Master analyze player tactics and dynamically send aggressive enemies, limit resources, create random events.

AI Agents as “Living” Opponents & Allies (Beyond Standard NPC AI)
    * AI agents could use reinforcement learning (RL) to evolve.
    * Enemies and allies in your game LEARN over time, creating a more immersive experience.

#  Example Agentic App

![ai-agent-code-pattern](./images/ai-agent-code-pattern.png)

    * 1- Connect to the AI Foundry project for your agent, using the project endpoint and Entra ID authentication.
    * 2- Get a reference to an existing agent
        * The model deployment that the agent interpret and respond to prompts.
        * Instructions that determine the functionality and behavior.
        * Tools and resources that the agent can use to perform tasks.
    * 3- Create a stateful thread that retains message history and data artifacts generated during the chat.
    * 4- Add messages to the thread and invoke it with the agent.
    * 5- Check the thread status, and when ready, retrieve the messages and data artifacts.
    * 6- Repeat the previous two steps as a chat loop until the conversation can be concluded.
    * 7- When finished, delete the agent and the thread to clean up.