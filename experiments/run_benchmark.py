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
from pipelines.llm_stub import DummyLLM

from evaluation.retrieval_metrics import recall_at_k, mean_reciprocal_rank
from evaluation.answer_quality import simple_answer_match
from evaluation.hallucination import is_hallucinated


BASE_DIR = Path(__file__).resolve().parents[1]


def load_eval_dataset():
    eval_path = BASE_DIR / "data" / "eval_dataset.json"
    with open(eval_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_retriever():
    docs = load_documents(BASE_DIR / "data" / "documents")
    docs = [clean_document(d) for d in docs]

    chunker = RecursiveChunker(chunk_size=500)
    chunks = chunker.chunk(docs)

    embedder = Embedder()
    embeddings = embedder.embed_texts([c["text"] for c in chunks])

    index = VectorIndex(embedding_dim=embeddings.shape[1])
    index.add(embeddings, chunks)

    return Retriever(embedder, index)


def run_benchmark():
    eval_data = load_eval_dataset()
    retriever = build_retriever()

    llm = DummyLLM()
    rag_pipeline = BasicRAGPipeline(retriever, llm)

    results = []

    for sample in eval_data:
        question = sample["question"]
        relevant_docs = sample["relevant_docs"]
        expected_answer = sample["expected_answer"]

        rag_result = rag_pipeline.run(question, top_k=5)

        retrieved_sources = rag_result["sources"]
        generated_answer = rag_result["answer"]

        metrics = {
            "question": question,
            "recall@5": recall_at_k(retrieved_sources, relevant_docs, k=5),
            "mrr": mean_reciprocal_rank(retrieved_sources, relevant_docs),
            "qa_score": simple_answer_match(generated_answer, expected_answer),
            "hallucinated": is_hallucinated(
                generated_answer,
                [generated_answer]  # stub context for now
            ),
        }

        results.append(metrics)

    output_path = BASE_DIR / "experiments" / "results" / "benchmark_results.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n=== Benchmark Complete ===")
    for r in results:
        print(r)


if __name__ == "__main__":
    run_benchmark()
