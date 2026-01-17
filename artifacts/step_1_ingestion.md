# Step 1 — Document Ingestion

## Objective
Convert raw documents (PDF / TXT) into clean, structured document records with metadata.
This step is intentionally isolated from chunking and embeddings to keep the pipeline modular
and reproducible.

## Files Implemented
- ingestion/loader.py
- ingestion/cleaner.py
- app.py (test harness)

## Key Design Decisions
- One record per PDF page for finer-grained retrieval later
- Stable doc_id based on filename
- Metadata preserved: source, page, path
- No framework dependency (LangChain avoided)

## Metadata Schema
{
  "doc_id": str,
  "text": str,
  "source": "pdf" | "txt",
  "page": int | None,
  "path": str
}

## Command Used
python app.py

## Observed Output
Scanning directory: C:\Users\APPLE\Desktop\rag-benchmark-engine\data\documents
Found file: week 4-8 plan.pdf
Found file: week_1-4_plan.pdf
Total documents loaded: 23
Sample document keys: dict_keys(['doc_id', 'text', 'source', 'page', 'path'])

## Outcome
✅ Ingestion layer successfully normalizes raw documents into structured records.
✅ Ready for downstream chunking experiments.
