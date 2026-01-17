# chunking/fixed_chunker.py

from typing import List, Dict
from chunking.base_chunker import BaseChunker


class FixedChunker(BaseChunker):
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, documents: List[Dict]) -> List[Dict]:
        chunks = []

        for doc in documents:
            text = doc["text"]
            start = 0
            chunk_id = 0

            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end]

                chunks.append({
                    "chunk_id": f"{doc['doc_id']}_{chunk_id}",
                    "text": chunk_text,
                    "doc_id": doc["doc_id"],
                    "source": doc["source"],
                    "page": doc["page"],
                    "path": doc["path"]
                })

                chunk_id += 1
                start += self.chunk_size - self.overlap

        return chunks
