# Step 4 — Basic RAG Pipeline

## Objective
Generate answers using retrieved context while enforcing grounding and source tracking.

## Files Implemented
- pipelines/rag_basic.py
- pipelines/llm_stub.py
- app.py (end-to-end test harness)

## RAG Flow
User Query
→ Retriever (Top-K chunks)
→ Grounded Prompt Construction
→ LLM Generation
→ Answer + Sources

## Prompt Grounding Rule
- LLM must answer ONLY from provided context
- If answer not found, respond with "I don't know"

## Output Schema
{
  "query": str,
  "answer": str,
  "sources": List[str]
}

## Command Used
python app.py

## Observed Output
RAG OUTPUT
Answer: [LLM OUTPUT PLACEHOLDER]
Sources: ['offer']

## Outcome
✅ End-to-end RAG pipeline works
✅ Source tracking enabled (hallucination-ready)
✅ Ready for real LLM + evaluation layer
# Step 4 — Basic RAG Pipeline

## Objective
Generate answers using retrieved context while enforcing grounding and source tracking.

## Files Implemented
- pipelines/rag_basic.py
- pipelines/llm_stub.py
- app.py (end-to-end test harness)

## RAG Flow
User Query
→ Retriever (Top-K chunks)
→ Grounded Prompt Construction
→ LLM Generation
→ Answer + Sources

## Prompt Grounding Rule
- LLM must answer ONLY from provided context
- If answer not found, respond with "I don't know"

## Output Schema
{
  "query": str,
  "answer": str,
  "sources": List[str]
}

## Command Used
python app.py

## Observed Output
RAG OUTPUT
Answer: [LLM OUTPUT PLACEHOLDER]
Sources: ['offer']

## Outcome
✅ End-to-end RAG pipeline works
✅ Source tracking enabled (hallucination-ready)
✅ Ready for real LLM + evaluation layer
