# app.py

from ingestion.loader import load_documents
from ingestion.cleaner import clean_document

def main():
    docs = load_documents("data/documents")
    docs = [clean_document(d) for d in docs]

    print(f"Total documents loaded: {len(docs)}")
    print("Sample document keys:", docs[0].keys())
    print("Sample text preview:", docs[0]["text"][:300])

if __name__ == "__main__":
    main()
