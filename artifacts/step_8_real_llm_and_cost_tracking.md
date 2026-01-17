# Step 8 — Real LLM Integration & Cost Tracking

## Objective
Integrate a real production-grade Large Language Model (LLM) into the RAG
benchmarking system and extend the evaluation framework to measure cost,
token usage, and system resilience under real-world API constraints.

This step upgrades the system from evaluation-only infrastructure to a
production-credible GenAI platform.

---

## LLM Implementations

### 1. DummyLLM (Offline / Fallback Mode)

**Purpose**
- Enable offline benchmarking without external API dependencies
- Validate retrieval, evaluation, and benchmarking logic
- Act as a graceful fallback when real LLM APIs are unavailable

**Behavior**
- Returns a deterministic placeholder response
- Zero input tokens
- Zero output tokens
- Zero cost

## Command Used
python -m experiments.run_benchmark


**Interface Contract**
```json
{
  "text": "[LLM OUTPUT PLACEHOLDER]",
  "input_tokens": 0,
  "output_tokens": 0,
  "cost": 0.0
}
