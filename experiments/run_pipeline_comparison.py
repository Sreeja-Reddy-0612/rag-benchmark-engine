# experiments/run_pipeline_comparison.py

import json
from pathlib import Path

from pipelines.rag_basic import BasicRAGPipeline
from pipelines.rag_reranked import RerankedRAGPipeline
from pipelines.llm_stub import DummyLLM

from evaluation.retrieval_metrics import recall_at_k, mean_reciprocal_rank
from evaluation.answer_quality import simple_answer_match
from evaluation.hallucination import is_hallucinated

from experiments.run_benchmark import build_retriever, load_eval_dataset

BASE_DIR = Path(__file__).resolve().parents[1]


def run_comparison():
    retriever = build_retriever()
    eval_data = load_eval_dataset()

    llm = DummyLLM()

    pipelines = {
        "basic_rag": BasicRAGPipeline(retriever, llm),
        "reranked_rag": RerankedRAGPipeline(retriever, llm)
    }

    results = {}

    for name, pipeline in pipelines.items():
        pipeline_scores = []

        for sample in eval_data:
            q = sample["question"]
            rel = sample["relevant_docs"]
            exp = sample["expected_answer"]

            out = pipeline.run(q)
            sources = out["sources"]
            ans = out["answer"]

            pipeline_scores.append({
                "recall@5": recall_at_k(sources, rel, 5),
                "mrr": mean_reciprocal_rank(sources, rel),
                "qa_score": simple_answer_match(ans, exp),
                "hallucinated": is_hallucinated(ans, [ans])
            })

        results[name] = pipeline_scores

    out_path = BASE_DIR / "experiments" / "results" / "pipeline_comparison.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n=== Pipeline Comparison Complete ===")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    run_comparison()
