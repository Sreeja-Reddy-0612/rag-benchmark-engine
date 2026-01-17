# Step 7 — Multiple Pipeline Comparison

## Objective
Compare different RAG architectures under identical evaluation conditions to make
evidence-based design decisions.

## Pipelines Compared
1. Basic RAG
   - Single-stage retrieval
   - Top-K chunks passed directly to LLM

2. Reranked RAG
   - Two-stage retrieval
   - Initial broad retrieval followed by semantic reranking

## Files Implemented
- pipelines/rag_reranked.py
- experiments/run_pipeline_comparison.py
- experiments/results/pipeline_comparison.json

## Comparison Flow
Evaluation Dataset
→ Run Basic RAG
→ Run Reranked RAG
→ Compute Recall@K, MRR, QA Score, Hallucination
→ Store side-by-side comparison report

## Command Used
python -m experiments.run_pipeline_comparison

## Observed Output
{
  "basic_rag": [
    { "recall@5": 1.0, "mrr": 0.33, "qa_score": 0.0, "hallucinated": false }
  ],
  "reranked_rag": [
    { "recall@5": 1.0, "mrr": 0.33, "qa_score": 0.0, "hallucinated": false }
  ]
}

## Interpretation
- Both pipelines retrieve the correct document
- Reranking does not improve results for this dataset
- Demonstrates how evaluation prevents unnecessary complexity

## Outcome
✅ Architecture-level RAG comparison enabled  
✅ Evaluation-driven decision making  
✅ Ready for real LLM and cost-based tradeoff analysis
