### Vector:
A vector database is a database designed to store, index and search high dimensional vectors that represent text, images, audio and other idea. It is optimize for similarity search, which means finding items that are most similar to given query vetor.

#### What its stores
- Vector(a list of floating point number, usually 256 or 4096 dimensions).
- That original data or metadata.
- Indexs structure that make similarity search fast.

#### Why vectors are used
Models like OpenAI, Qwen, or Sentence-Transformers convert text into vectors.
Vectors encode semantic meaning, so similar text ends up close in vector space.

#### What a vector DB does
A vector database provides:

- Insert embeddings
-  Query by similarity (top-k nearest neighbors)
- Filtering with metadata
- Fast indexing using ANN algorithms like HNSW, IVF, PQ.

#### How similarity search works
When you query with an embedding, the DB finds the nearest vectors using distance metrics such as:
- cosine similarity
- Euclidean distance
- dot product

#### Why not use a normal database

Normal DBs are not designed for high-dimensional vector search.
Vector DBs use special data structures and optimized search algorithms, giving millisecond-level results even with millions or billions of vectors.

#### Popular vector databases
- Pinecone
- Weaviate
- Chroma
- Milvus
- Qdrant
- Redis Vector Index
- Elasticsearch / OpenSearch with vector support

#### When to use a vector DB

- Retrieval Augented Generation(RAG)
- Semantic search
- Chat over documents
- Recommendation Systems
- Deduplication and clustering

#### What is dimension in vector DB ?
In a vector database, dimensions refer to the number of values inside each embedding vector.
It is simply the length of the vector that represents your text, image, or data.

Example:

If an embedding model outputs:
[0.12, -0.44, 0.88, … ]
and there are 1536 numbers, then the dimension is 1536.

#### Why dimensions are usually 256 to 4096

This range is practical because:

- Small dimensions
	- Less storage
	- Faster search
	- But captures less semantic meaning

- Large dimensions
	- More semantic capacity
	- Better accuracy for retrieval
	- But higher storage and slower search
- Research shows that 256, 384, 768, 1024, 1536, 2048, 4096 are good trade-offs between performance and cost.

---
### Three major vector databases: Pinecone, Milvus, and Qdrant

#### Pinecone

Pinecone is a fully managed, cloud-based vector database.
You do not manage servers, scaling, or index building; Pinecone handles everything.

Key points

- Fully managed service
- Very easy setup
- High reliability and auto-scaling
- Strong metadata filtering
- Pay-per-use model
- When to use: Note - Choose Pinecone when you want a simple, production-ready solution without managing infrastructure.

#### Milvus

Milvus is an open-source, high-performance vector database originally built by Zilliz.

Key points
- Open source
- Can run on your own server, Kubernetes, or cloud
- Supports huge datasets, billions of vectors
- Uses powerful ANN algorithms like HNSW, IVF, PQ
- Rich ecosystem with Zilliz Cloud (managed version)
- When to use: Choose Milvus if you want full control, on-premise deployment, or extremely large-scale vector search.


#### Qdrant
Qdrant is an open-source, developer-focused vector database written in Rust.

Key points
- Open source
- Lightweight and easy to deploy
- Known for speed and efficiency due to Rust
- Strong filtering and hybrid search
- Has a cloud offering similar to Pinecone
- When to use - Choose Qdrant when you want an easy, fast, self-hosted option with excellent performance and modern API design.

#### Comparision:
| Feature     | Pinecone                           | Milvus                            | Qdrant                        |
| ----------- | ---------------------------------- | --------------------------------- | ----------------------------- |
| Deployment  | Cloud only (managed)               | Self-hosted and cloud             | Self-hosted and cloud         |
| Complexity  | Easiest                            | Medium to high                    | Easy                          |
| Performance | Very high                          | Very high                         | Very high                     |
| Scaling     | Automatic                          | Manual or Kubernetes              | Manual or Kubernetes          |
| Best for    | Production apps with minimal setup | Large-scale enterprise or on-prem | Fast, lightweight deployments |
