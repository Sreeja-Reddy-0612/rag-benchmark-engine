# Step 3 — Embeddings & Vector Store

## Objective
Enable semantic search by embedding chunks and indexing them in a vector store.

## Files Implemented
- embeddings/embedder.py
- vectorstore/index.py
- vectorstore/retriever.py
- app.py (test harness)

## Technology Choices
- SentenceTransformers (all-MiniLM-L6-v2)
- FAISS IndexFlatL2 (exact search, deterministic)

## Why Exact Search?
- Evaluation-first system
- Deterministic Recall@K and MRR
- Easier regression detection

## Retrieval Flow
Chunks → Embeddings → FAISS Index → Top-K Similarity Search

## Command Used
python app.py

## Observed Output
Total chunks: 5

Top retrieval results:
- Score: 1.6880
  Text preview: "We are excited to have you join our team..."

- Score: 1.7355
  Text preview: "NIRVAHA WELLNESS LLP Hyderabad..."

## Outcome
✅ Semantic retrieval working
✅ Metadata correctly mapped to vectors
✅ Retrieval layer ready for RAG pipelines
