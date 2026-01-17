# app.py
"""
Local experiment runner for RAG Benchmark Engine.

Purpose:
- Run end-to-end RAG pipeline (with stub LLM)
- Validate evaluation metrics independently
"""

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


def run_rag_pipeline():
    print("\n=== Running RAG Pipeline ===")

    # Ingestion
    docs = load_documents("data/documents")
    docs = [clean_document(d) for d in docs]

    # Chunking
    chunker = RecursiveChunker(chunk_size=500)
    chunks = chunker.chunk(docs)

    # Embedding + Index
    embedder = Embedder()
    embeddings = embedder.embed_texts([c["text"] for c in chunks])

    index = VectorIndex(embedding_dim=embeddings.shape[1])
    index.add(embeddings, chunks)

    retriever = Retriever(embedder, index)

    # RAG
    llm = DummyLLM()
    rag = BasicRAGPipeline(retriever, llm)

    result = rag.run("What is this document about?", top_k=3)

    print("Answer:", result["answer"])
    print("Sources:", result["sources"])


def run_evaluation_tests():
    print("\n=== Running Evaluation Tests ===")

    # Retrieval metrics
    retrieved_docs = ["offer", "policy"]
    relevant_docs = ["offer"]

    print("Recall@1:", recall_at_k(retrieved_docs, relevant_docs, k=1))
    print("MRR:", mean_reciprocal_rank(retrieved_docs, relevant_docs))

    # Answer quality
    generated = "This is an internship offer letter"
    expected = "internship offer"

    print("QA Score:", simple_answer_match(generated, expected))
    print(
        "Hallucinated:",
        is_hallucinated(generated, ["This is an internship offer letter"])
    )


if __name__ == "__main__":
    run_rag_pipeline()
    run_evaluation_tests()
