# RAG Quality Benchmarking & Evaluation Engine

Enterprise-grade, evaluation-first Retrieval-Augmented Generation (RAG)
benchmarking system designed to **measure, compare, and prevent regressions**
in retrieval quality, answer faithfulness, hallucination rate, and cost
across multiple RAG architectures.



## Problem Statement

Most RAG systems focus on generating answers but fail to answer a more
important question:

> “Is this version of the system actually better than the previous one?”

In production environments, RAG pipelines often suffer from:

- No objective evaluation
- Silent retrieval regressions
- Hallucinations going unnoticed
- Cost increases without visibility
- Architecture decisions made without evidence

These issues make RAG systems unreliable at enterprise scale.



## Solution Overview

This project implements an **evaluation-first RAG platform** that:

- builds multiple RAG pipelines under identical conditions
- benchmarks retrieval and answer quality using ground-truth datasets
- tracks hallucination and cost metrics
- compares pipeline architectures objectively
- detects regressions automatically over time

The system behaves like an **AI quality control layer**, not a chatbot demo.



## Intended Use Cases

- Enterprise knowledge assistants
- Internal RAG platforms
- AI infrastructure and platform teams
- Regulated or high-stakes AI systems
- Model and retriever experimentation environments



## System Architecture

```text
Documents
   ↓
Ingestion & Cleaning
   ↓
Chunking Engine
 (fixed | recursive)
   ↓
Embedding & Vector Store
 (FAISS + metadata)
   ↓
RAG Pipelines
 (basic | reranked)
   ↓
Evaluation Engine
 (Recall@K | MRR | QA | Hallucination)
   ↓
Cost Tracking
   ↓
Regression Detection
   ↓
Benchmark Reports
```



## Key Features

- Multiple RAG pipeline implementations
- Metadata-aware retrieval
- FAISS-based semantic search
- Ground-truth evaluation dataset
- Retrieval metrics (Recall@K, MRR)
- Answer quality evaluation
- Hallucination detection
- Real LLM integration with cost tracking
- Quota-aware LLM fallback
- Baseline-based regression detection



## Tech Stack

- Python
- SentenceTransformers
- FAISS
- OpenAI SDK (v2.x)
- JSON-based evaluation datasets
- Modular, production-style codebase



## How It Works (High Level)

1. Documents are ingested and cleaned
2. Text is chunked using fixed or recursive strategies
3. Chunks are embedded and indexed in FAISS
4. Multiple RAG pipelines retrieve relevant context
5. Answers are generated using LLM or fallback logic
6. Retrieval and QA metrics are computed
7. Token usage and cost are tracked per query
8. Results are compared against stored baselines
9. Regressions are automatically flagged



## How to Run Locally

```bash
git clone https://github.com/Sreeja-Reddy-0612/rag-benchmark-engine
cd rag-benchmark-engine

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt

python -m experiments.run_benchmark
```



## Project Status

- ✅ Step 1: Document ingestion and normalization  
- ✅ Step 2: Chunking engine (fixed & recursive)  
- ✅ Step 3: Embeddings and FAISS vector store  
- ✅ Step 4: Grounded RAG pipelines  
- ✅ Step 5: Evaluation engine  
- ✅ Step 6: Automated benchmark runner  
- ✅ Step 7: Multi-pipeline comparison  
- ✅ Step 8: Real LLM integration & cost tracking  
- ✅ Step 9: Regression detection & baselines  



## Design Principles

- Evaluation before optimization
- No silent regressions
- Deterministic behavior
- Clear architectural boundaries
- Cost-aware AI systems
- Enterprise realism over demos



## Author

**Sreeja Reddy**  
AI Engineer focused on RAG systems, LLM evaluation,  
GenAI reliability, and AI infrastructure engineering.

GitHub: https://github.com/Sreeja-Reddy-0612  
LinkedIn: https://www.linkedin.com/in/sreeja-reddy-5ab708288/
