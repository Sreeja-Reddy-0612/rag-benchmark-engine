# vectorstore/retriever.py

from typing import List, Dict
import numpy as np

from embeddings.embedder import Embedder
from vectorstore.index import VectorIndex


class Retriever:
    def __init__(self, embedder: Embedder, index: VectorIndex):
        self.embedder = embedder
        self.index = index

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Retrieve top_k relevant chunks for a query.
        """
        query_embedding = self.embedder.embed_texts([query])
        return self.index.search(query_embedding, top_k=top_k)
