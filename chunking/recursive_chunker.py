# chunking/recursive_chunker.py

from typing import List, Dict
from chunking.base_chunker import BaseChunker


class RecursiveChunker(BaseChunker):
    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def _split_text(self, text: str) -> List[str]:
        separators = ["\n\n", "\n", ". "]
        chunks = [text]

        for sep in separators:
            temp = []
            for chunk in chunks:
                if len(chunk) <= self.chunk_size:
                    temp.append(chunk)
                else:
                    temp.extend(chunk.split(sep))
            chunks = temp

        return chunks

    def chunk(self, documents: List[Dict]) -> List[Dict]:
        final_chunks = []

        for doc in documents:
            raw_chunks = self._split_text(doc["text"])
            buffer = ""
            chunk_id = 0

            for piece in raw_chunks:
                if len(buffer) + len(piece) <= self.chunk_size:
                    buffer += piece + " "
                else:
                    final_chunks.append({
                        "chunk_id": f"{doc['doc_id']}_{chunk_id}",
                        "text": buffer.strip(),
                        "doc_id": doc["doc_id"],
                        "source": doc["source"],
                        "page": doc["page"],
                        "path": doc["path"]
                    })
                    chunk_id += 1
                    buffer = piece + " "

            if buffer:
                final_chunks.append({
                    "chunk_id": f"{doc['doc_id']}_{chunk_id}",
                    "text": buffer.strip(),
                    "doc_id": doc["doc_id"],
                    "source": doc["source"],
                    "page": doc["page"],
                    "path": doc["path"]
                })

        return final_chunks
