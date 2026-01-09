### Lang Chain
LangChain is the open source framework designed to help developer to build application
powered by Large Language Model (LLM) in a structured, scalable and production oriented way.

- It focuses on **orchestration**: connecting models, data sources, tools and control logics into reliable workflows.
- LangChain is not an LLM.
- It is an orchestration framework that turns LLMs into reliable, testable, and scalable applications.
- If you are building production-grade AI systems, especially RAG or multi-step reasoning workflows, LangChain provides the necessary structure and tooling.
	
#### 1. Why LangChain Exists ?
Using as LLM directly(for example via an API call) is simple, but real-world applications quickly need more:
- Prompt reuse and versioning
- Multi-step reasoning and workflows
- Integrate with extarnal data
- Memory and conversational context
- Tool calling and agent like behaviour
- Observability, debugging, and evaluation
 
LangChain provides abstractions to solve these problems consistently.

---

#### 2. Core Architecture overview

At a high level, LangChain applications are built from these layers:
- Models
- Prompts
- Chains
- Data Collector
- RAG
- Memory
- Agents and tools
- Callback and Observability

Each layer can be used independently or combined.

---

#### 3. Models

LangChain provides a unified interface for different model types:
- LLMs (Text-in -> Text-out)
	- Example: OpenAI, Azure OpenAI, Anthropic, Hugging Face Infernce
	- Purpose: Summrization, Reasoning, Explanation, classification
- Chat Models
	- System / user / assistant messages
	- Better multi-turn handling
- Embedding Models
	- Used for Semantic models
	- Required for RAG pipelines

---

#### 4. Chains workflows

A chain is a sequence of calls where the output of one step feeds to next.
- Simple Chain
	- Prompt -> Model -> output
- Sequential Chain
	- Step-by-step logic
	- Example:
		- Extract entities
		- Summarize extracted content
		- Format final answer

- Router Chains
	- Decide which chain to excute based on input
	- Useful for multi-domain assistant

- Why chains are important:
	- They bring determinism and structure to LLM-driven logic.

---

#### 5. Data Handling and Document Processing

- Document loader
- Text Splitter

---

#### 6. Vector Store and Embedding Generation

LangChain integrates with most vector databases.
- Vector Store: FAISS, Pinecone, Chroma, Weaviate, Milvus, Azure AI Search
- Responsibilities: store embeddings, similarity search, return relevant chunks.

---

#### 7. Strengths and Limitations

##### Strengths
- Strong RAG support
- Modular and extensible
- Vendor-agnostic model interfaces
- Rich ecosystem
- Production tooling (LangSmith)

##### Limitations
- Learning curve for beginners
- Rapid API changes
- Can be overkill for simple use cases
- Agents can be costly and unpredictable

---

#### 8. When You Should Use LangChain
- Use LangChain if:
	- You are building RAG systems
	- You need structured multi-step LLM workflows
	- You integrate multiple data sources
	- You need observability and evaluation
- Avoid if
	- You only need a single prompt call
	- You want minimal abstraction