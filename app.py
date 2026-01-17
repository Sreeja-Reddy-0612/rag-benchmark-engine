from ingestion.loader import load_documents
from ingestion.cleaner import clean_document
from chunking.fixed_chunker import FixedChunker
from chunking.recursive_chunker import RecursiveChunker

def main():
    docs = load_documents("data/documents")
    docs = [clean_document(d) for d in docs]

    fixed_chunker = FixedChunker(chunk_size=500, overlap=50)
    recursive_chunker = RecursiveChunker(chunk_size=500)

    fixed_chunks = fixed_chunker.chunk(docs)
    recursive_chunks = recursive_chunker.chunk(docs)

    print(f"Documents: {len(docs)}")
    print(f"Fixed chunks: {len(fixed_chunks)}")
    print(f"Recursive chunks: {len(recursive_chunks)}")

    print("\nSample fixed chunk:\n", fixed_chunks[0]["text"][:300])
    print("\nSample recursive chunk:\n", recursive_chunks[0]["text"][:300])

if __name__ == "__main__":
    main()
