# experiments/run_benchmark.py

import json
from pathlib import Path

from ingestion.loader import load_documents
from ingestion.cleaner import clean_document
from chunking.recursive_chunker import RecursiveChunker

from embeddings.embedder import Embedder
from vectorstore.index import VectorIndex
from vectorstore.retriever import Retriever

from pipelines.rag_basic import BasicRAGPipeline
# from pipelines.llm_stub import DummyLLM
from llm.openai_client import OpenAIClient


from evaluation.retrieval_metrics import recall_at_k, mean_reciprocal_rank
from evaluation.answer_quality import simple_answer_match
from evaluation.hallucination import is_hallucinated

from experiments.regression.regression_detector import detect_regression

BASE_DIR = Path(__file__).resolve().parents[1]


def load_eval_dataset():
    eval_path = BASE_DIR / "data" / "eval_dataset.json"
    with open(eval_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_retriever():
    docs = load_documents(BASE_DIR / "data" / "documents")
    docs = [clean_document(d) for d in docs]

    chunker = RecursiveChunker(chunk_size=100)
    chunks = chunker.chunk(docs)

    embedder = Embedder()
    embeddings = embedder.embed_texts([c["text"] for c in chunks])

    index = VectorIndex(embedding_dim=embeddings.shape[1])
    index.add(embeddings, chunks)

    return Retriever(embedder, index)


def run_benchmark():
    eval_data = load_eval_dataset()
    retriever = build_retriever()

    # llm = DummyLLM()
    # llm = OpenAIClient()
    # llm = OpenAIClient(model="gpt-4o-mini")
    try:
        
        llm = OpenAIClient(model="gpt-4o-mini")
        print("Using OpenAI LLM")
    except Exception:
        
        from pipelines.llm_stub import DummyLLM
        llm = DummyLLM()
        print("Falling back to DummyLLM (no quota)")



    rag_pipeline = BasicRAGPipeline(retriever, llm)

    results = []
    total_cost = 0.0
    for sample in eval_data:
        question = sample["question"]
        relevant_docs = sample["relevant_docs"]
        expected_answer = sample["expected_answer"]

        rag_result = rag_pipeline.run(question, top_k=5)

        retrieved_sources = rag_result["sources"]
        generated_answer = rag_result["answer"]

        total_cost += rag_result["cost"]

        metrics = {
    "question": question,
    "recall@5": recall_at_k(retrieved_sources, relevant_docs, 5),
    "mrr": mean_reciprocal_rank(retrieved_sources, relevant_docs),
    "qa_score": simple_answer_match(generated_answer, expected_answer),
    "hallucinated": is_hallucinated(
        generated_answer,
        [generated_answer]
    ),
    "cost": rag_result["cost"]
}


        results.append(metrics)
    print("Total cost for benchmark run: $", round(total_cost, 6))

    output_path = BASE_DIR / "experiments" / "results" / "benchmark_results.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Aggregate current metrics
    avg_metrics = {
        "recall@5": sum(r["recall@5"] for r in results) / len(results),
        "mrr": sum(r["mrr"] for r in results) / len(results),
        "qa_score": sum(r["qa_score"] for r in results) / len(results),
        "hallucination_rate": sum(
            1 for r in results if r["hallucinated"]
        ) / len(results),
        "avg_cost": total_cost / len(results)
    }

    # Load baseline
    baseline_path = BASE_DIR / "experiments" / "baselines" / "baseline_v1.json"
    with open(baseline_path, "r", encoding="utf-8") as f:
        baseline = json.load(f)

    # Detect regression
    regression_report = detect_regression(avg_metrics, baseline)

    print("\n=== Benchmark Complete ===")
    for r in results:
        print(r)

    print("\n=== Regression Check ===")
    if regression_report["any_regression"]:
        print("❌ Regression detected:", regression_report)
    else:
        print("✅ No regression detected")


if __name__ == "__main__":
    run_benchmark()
