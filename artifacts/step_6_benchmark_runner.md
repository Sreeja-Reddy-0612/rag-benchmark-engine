# Step 6 — Benchmark Runner

## Objective
Automate evaluation of RAG pipelines using a gold evaluation dataset instead of
manual or hard-coded testing.

## Files Implemented
- experiments/run_benchmark.py
- data/eval_dataset.json
- experiments/results/benchmark_results.json

## Benchmark Flow
Evaluation Dataset (questions + ground truth)
→ RAG Pipeline Execution
→ Retrieval Metrics (Recall@K, MRR)
→ Answer Quality Scoring
→ Hallucination Detection
→ Structured JSON Report

## Command Used
python -m experiments.run_benchmark

## Observed Output
{
  "question": "What is this document about?",
  "recall@5": 1.0,
  "mrr": 1.0,
  "qa_score": 0.0,
  "hallucinated": false
}

## Interpretation
- Retrieval quality is perfect (correct document ranked first)
- QA score is zero because a stub LLM is used
- Hallucination detection confirms grounded output

## Outcome
✅ Fully automated evaluation
✅ No hard-coded metrics
✅ Ready for multi-pipeline comparison
