# Step 9 — Regression Detection & Baseline Tracking

## Objective
Prevent silent quality degradation in RAG pipelines by automatically
detecting regressions in retrieval quality, answer quality, and cost
whenever data, configuration, or system behavior changes.

This step brings the project in line with real enterprise ML lifecycle practices.


## Baseline Strategy

A known-good benchmark run is captured as a fixed baseline and stored as:

experiments/baselines/baseline_v1.json



This baseline represents expected system behavior under stable conditions.

### Baseline Metrics Tracked
- Recall@K
- Mean Reciprocal Rank (MRR)
- QA score
- Hallucination rate
- Average cost per query



## Regression Detection Logic

A regression is flagged when:

- Recall@5 drops more than 5%
- MRR drops more than 5%
- QA score drops more than 10%
- Cost increases more than 20%

Threshold-based detection ensures explainability and deterministic behavior.



## Implementation Components

- `experiments/regression/regression_detector.py`
- `experiments/baselines/baseline_v1.json`
- `experiments/run_benchmark.py` (extended)



## Execution Flow

1. Run benchmark on current pipeline
2. Aggregate metrics across evaluation dataset
3. Load baseline metrics
4. Compare current vs baseline
5. Automatically flag regressions



## Observed Outputs

### Case 1 — No Regression
=== Regression Check ===
✅ No regression detected

shell
Copy code

### Case 2 — Regression Detected
=== Regression Check ===
❌ Regression detected: {
"recall_regressed": true,
"mrr_regressed": true,
"qa_regressed": false,
"cost_regressed": false
}



## Validation Method

Regression was intentionally triggered by:
- Adding noisy, unrelated research PDFs
- Increasing knowledge base size
- Introducing domain mismatch

This simulates real-world data drift scenarios.



## Outcome

✅ Baseline quality locked  
✅ Automatic regression detection enabled  
✅ Silent failures prevented  
✅ Enterprise-grade evaluation lifecycle achieved  

