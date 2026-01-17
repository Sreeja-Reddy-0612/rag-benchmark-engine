# vectorstore/index.py

import faiss
import numpy as np
from typing import List, Dict


class VectorIndex:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata: List[Dict] = []

    def add(self, embeddings: np.ndarray, metadatas: List[Dict]):
        """
        Add embeddings and corresponding metadata to the index.
        """
        self.index.add(embeddings)
        self.metadata.extend(metadatas)

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        """
        Search for top_k similar embeddings.
        """
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            results.append({
                "score": float(dist),
                "metadata": self.metadata[idx]
            })

        return results
