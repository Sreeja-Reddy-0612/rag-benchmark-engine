# Step 2 — Chunking Engine

## Objective
Split documents into retrieval-ready chunks using multiple strategies while preserving metadata.

## Files Implemented
- chunking/base_chunker.py
- chunking/fixed_chunker.py
- chunking/recursive_chunker.py
- app.py (test harness)

## Chunking Strategies
1. Fixed Chunking
   - Fixed character length
   - Configurable overlap
   - Baseline strategy

2. Recursive Chunking
   - Splits by semantic boundaries (paragraphs, sentences)
   - Reduces semantic breakage
   - Higher retrieval quality

## Chunk Metadata Schema
{
  "chunk_id": str,
  "text": str,
  "doc_id": str,
  "source": str,
  "page": int,
  "path": str
}

## Command Used
python app.py

## Observed Output
Documents: 23
Fixed chunks: 65
Recursive chunks: 71

Sample fixed chunk:
"Excellent — here’s your complete breakdown for Week 5 – GenAI APIs..."

Sample recursive chunk:
"Excellent — here’s your complete breakdown for Week 5 – GenAI APIs..."

## Outcome
✅ Multiple chunking strategies implemented
✅ Metadata preserved across chunks
✅ Ready for embedding and retrieval benchmarking
