from ingestion.loader import load_documents
from ingestion.cleaner import clean_document
from chunking.recursive_chunker import RecursiveChunker

from embeddings.embedder import Embedder
from vectorstore.index import VectorIndex
from vectorstore.retriever import Retriever


def main():
    # Load + clean docs
    docs = load_documents("data/documents")
    docs = [clean_document(d) for d in docs]

    # Chunk
    chunker = RecursiveChunker(chunk_size=500)
    chunks = chunker.chunk(docs)

    print(f"Total chunks: {len(chunks)}")

    # Prepare embeddings
    texts = [c["text"] for c in chunks]
    metadatas = chunks

    embedder = Embedder()
    embeddings = embedder.embed_texts(texts)

    # Build index
    vector_index = VectorIndex(embedding_dim=embeddings.shape[1])
    vector_index.add(embeddings, metadatas)

    # Retrieve
    retriever = Retriever(embedder, vector_index)
    results = retriever.retrieve(
        query="What is Week 5 about?",
        top_k=3
    )

    print("\nTop retrieval results:")
    for r in results:
        print("- Score:", r["score"])
        print("  Text preview:", r["metadata"]["text"][:200])
        print()

if __name__ == "__main__":
    main()
