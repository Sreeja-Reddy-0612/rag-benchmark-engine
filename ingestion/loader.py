# ingestion/loader.py

from pathlib import Path
from typing import List, Dict

from PyPDF2 import PdfReader


def load_txt(file_path: Path) -> List[Dict]:
    """Load a TXT file and return document records."""
    text = file_path.read_text(encoding="utf-8")

    return [{
        "doc_id": file_path.stem,
        "text": text,
        "source": "txt",
        "page": None,
        "path": str(file_path)
    }]


def load_pdf(file_path: Path) -> List[Dict]:
    """Load a PDF file and return one record per page."""
    reader = PdfReader(str(file_path))
    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        documents.append({
            "doc_id": file_path.stem,
            "text": text,
            "source": "pdf",
            "page": page_number,
            "path": str(file_path)
        })

    return documents


def load_documents(data_dir: str) -> List[Dict]:
    data_path = Path(data_dir)
    all_docs = []

    print("Scanning directory:", data_path.resolve())

    for file_path in data_path.iterdir():
        print("Found file:", file_path.name)

        if file_path.suffix == ".txt":
            all_docs.extend(load_txt(file_path))

        elif file_path.suffix == ".pdf":
            all_docs.extend(load_pdf(file_path))

    return all_docs
