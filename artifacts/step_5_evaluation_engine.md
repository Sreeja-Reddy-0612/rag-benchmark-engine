# Step 5 — Evaluation Engine

## Objective
Introduce objective evaluation for RAG systems by separating retrieval quality,
answer correctness, and hallucination detection.

## Files Implemented
- evaluation/retrieval_metrics.py
- evaluation/answer_quality.py
- evaluation/hallucination.py
- data/eval_dataset.json
- app.py (evaluation test runner)

## Evaluation Dimensions

### 1. Retrieval Quality
Metrics:
- Recall@K
- Mean Reciprocal Rank (MRR)

Purpose:
- Measure retriever effectiveness independent of LLM behavior

### 2. Answer Quality
Metric:
- Token overlap–based QA score (0–1)

Purpose:
- Compare generated answer vs expected answer deterministically

### 3. Hallucination Detection
Method:
- Check unsupported tokens against retrieved context

Purpose:
- Identify ungrounded or fabricated responses

## Test Command
python app.py

## Observed Output
Recall@1: 1.0
MRR: 1.0
QA Score: 1.0
Hallucinated: False

## Outcome
✅ Evaluation logic validated independently
✅ Clear separation between retrieval and generation failures
✅ Ready for benchmark runner and pipeline comparison
