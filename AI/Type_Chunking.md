In a RAG (Retrieval-Augmented Generation) pipeline, **chunking** is the process of splitting large documents into smaller pieces before generating embeddings and storing them in a vector database.

The choice of chunking directly impacts retrieval quality, context relevance, and LLM response accuracy.

## 1. Fixed-Size Chunking

Splits text into chunks of a predefined size (e.g., 500 tokens).

### Example

```
Chunk 1: Tokens 1-500
Chunk 2: Tokens 501-1000
Chunk 3: Tokens 1001-1500
```

### Advantages

* Simple and fast
* Easy to implement
* Works well for uniform text

### Disadvantages

* May split sentences or paragraphs
* Can lose semantic meaning

### Best For

* Large-scale ingestion pipelines
* Simple document repositories

---

## 2. Fixed-Size Chunking with Overlap

Chunks overlap by a certain number of tokens.

### Example

```
Chunk 1: Tokens 1-500
Chunk 2: Tokens 450-950
Chunk 3: Tokens 900-1400
```

Overlap = 50 tokens

### Advantages

* Preserves context across chunk boundaries
* Most commonly used in production RAG systems

### Disadvantages

* Increases storage and embedding costs

### Best For

* General-purpose RAG applications

---

## 3. Sentence-Based Chunking

Splits text based on sentence boundaries.

### Example

```
Sentence 1
Sentence 2
Sentence 3
```

Group multiple sentences into one chunk.

### Advantages

* Maintains complete thoughts
* Better semantic coherence

### Disadvantages

* Chunk sizes become inconsistent

### Best For

* Articles
* Research papers
* Reports

---

## 4. Paragraph-Based Chunking

Uses paragraph boundaries as chunk separators.

### Example

```
Paragraph 1 → Chunk 1
Paragraph 2 → Chunk 2
Paragraph 3 → Chunk 3
```

### Advantages

* Preserves document structure
* High semantic quality

### Disadvantages

* Some paragraphs may be extremely large

### Best For

* Contracts
* Policies
* Technical documentation

---

## 5. Recursive Chunking

Attempts to split text hierarchically.

### Process

```
Document
 ├─ Heading
 │   ├─ Paragraph
 │   │   ├─ Sentence
 │   │   │   ├─ Words
```

Common separators:

```
\n\n
\n
.
space
```

If chunk exceeds the limit, the algorithm tries the next level.

### Advantages

* Maintains structure
* Widely used in frameworks like LangChain

### Best For

* General-purpose RAG systems

---

## 6. Semantic Chunking

Splits text based on meaning rather than size.

### Example

A document contains:

```
Section 1: Machine Learning
Section 2: Databases
Section 3: Networking
```

Chunks are created when semantic similarity changes significantly.

### Advantages

* High retrieval accuracy
* Natural topic boundaries

### Disadvantages

* Computationally expensive
* Requires embeddings during chunking

### Best For

* Enterprise search
* Knowledge assistants

---

## 7. Document Structure-Based Chunking

Uses document elements such as:

* Headings
* Subheadings
* Tables
* Lists
* Sections

### Example

```
H1: Introduction
  → Chunk

H1: Installation
  H2: Requirements
  H2: Setup
```

### Advantages

* Retains document hierarchy
* Excellent for technical manuals

### Best For

* HTML documents
* PDFs
* Word documents

---

## 8. Sliding Window Chunking

Creates chunks by moving a window across the document.

### Example

```
Window Size = 500
Step Size = 250
```

```
1-500
251-750
501-1000
```

### Advantages

* Strong contextual continuity

### Disadvantages

* High duplication

### Best For

* Question-answering systems

---

## 9. Token-Based Chunking

Uses tokenizer counts instead of character counts.

### Example

```
Max Chunk Size = 512 tokens
```

### Advantages

* Matches embedding model limits
* More accurate than character-based chunking

### Best For

* Production RAG systems

---

## 10. Metadata-Aware Chunking

Chunks are created while preserving metadata.

### Example

```json
{
  "document": "Policy.pdf",
  "page": 10,
  "section": "Benefits"
}
```

Each chunk retains:

* Page number
* Section
* Source document
* Author

### Advantages

* Better citations
* Better filtering during retrieval

### Best For

* Enterprise document search

---

## 11. Agentic Chunking

An LLM determines where chunk boundaries should be.

### Process

```
Read section
Understand topic
Create meaningful chunk
Assign summary
Store chunk
```

### Advantages

* Very high semantic quality

### Disadvantages

* Expensive
* Slow ingestion

### Best For

* High-value knowledge bases

---

## 12. Hierarchical Chunking

Creates parent-child relationships between chunks.

### Example

```
Document
 ├─ Chapter
 │   ├─ Section
 │   │   ├─ Paragraph
```

Retrieval may happen at:

* Paragraph level
* Section level
* Chapter level

### Advantages

* Multi-level retrieval
* Better context reconstruction

### Best For

* Large manuals
* Legal documents
* Books

---

## Recommended Chunking Strategies

| Use Case              | Recommended Method                   |
| --------------------- | ------------------------------------ |
| General RAG           | Recursive + Overlap                  |
| PDF Documents         | Structure-Based + Recursive          |
| Research Papers       | Sentence + Semantic                  |
| Legal Documents       | Hierarchical + Metadata              |
| HTML Pages            | DOM/Structure-Based                  |
| Enterprise Search     | Semantic + Metadata                  |
| Large Knowledge Bases | Hierarchical + Semantic              |
| OCR Documents         | Structure-Based + Metadata + Overlap |

For your OCR/PDF extraction projects, a strong production approach is:

**Document Structure Chunking → Recursive Chunking → 10–20% Overlap → Metadata Storage**

This preserves headings, tables, page references, and semantic context while maintaining high retrieval accuracy.
