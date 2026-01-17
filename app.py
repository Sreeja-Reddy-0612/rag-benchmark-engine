from ingestion.loader import load_documents
from ingestion.cleaner import clean_document
from chunking.recursive_chunker import RecursiveChunker

from embeddings.embedder import Embedder
from vectorstore.index import VectorIndex
from vectorstore.retriever import Retriever

from pipelines.rag_basic import BasicRAGPipeline
from pipelines.llm_stub import DummyLLM


def main():
    # Ingestion
    docs = load_documents("data/documents")
    docs = [clean_document(d) for d in docs]

    # Chunking
    chunker = RecursiveChunker(chunk_size=500)
    chunks = chunker.chunk(docs)

    # Embedding + index
    embedder = Embedder()
    texts = [c["text"] for c in chunks]
    embeddings = embedder.embed_texts(texts)

    index = VectorIndex(embedding_dim=embeddings.shape[1])
    index.add(embeddings, chunks)

    retriever = Retriever(embedder, index)

    # RAG pipeline
    llm = DummyLLM()
    rag = BasicRAGPipeline(retriever, llm)

    result = rag.run("What is this document about?", top_k=3)

    print("\nRAG OUTPUT")
    print("Answer:", result["answer"])
    print("Sources:", result["sources"])


if __name__ == "__main__":
    main()
