# ingestion/cleaner.py

import re
from typing import Dict


def clean_text(text: str) -> str:
    """Basic text cleaning for ingestion."""
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def clean_document(doc: Dict) -> Dict:
    """Clean text inside a document record."""
    doc["text"] = clean_text(doc["text"])
    return doc
