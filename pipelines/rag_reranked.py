# pipelines/rag_reranked.py

import numpy as np
from typing import List, Dict
from vectorstore.retriever import Retriever


class RerankedRAGPipeline:
    def __init__(self, retriever: Retriever, llm_client):
        self.retriever = retriever
        self.llm = llm_client

    def _rerank(self, query_embedding, candidates: List[Dict], top_k: int):
        scored = []

        for c in candidates:
            chunk_emb = self.retriever.embedder.embed_texts(
                [c["metadata"]["text"]]
            )[0]

            score = np.dot(query_embedding[0], chunk_emb)
            scored.append((score, c))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [c for _, c in scored[:top_k]]

    def _build_prompt(self, query: str, contexts: List[str]) -> str:
        context_block = "\n\n".join(contexts)
        return f"""
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context_block}

Question:
{query}

Answer:
""".strip()

    def run(self, query: str, retrieve_k: int = 20, rerank_k: int = 5):
        query_embedding = self.retriever.embedder.embed_texts([query])

        initial = self.retriever.index.search(query_embedding, top_k=retrieve_k)

        reranked = self._rerank(query_embedding, initial, rerank_k)

        contexts = [r["metadata"]["text"] for r in reranked]
        sources = [r["metadata"]["doc_id"] for r in reranked]

        prompt = self._build_prompt(query, contexts)
        result = self.llm.generate(prompt)

        return {
    "answer": result["text"],
    "sources": list(set(sources)),
    "input_tokens": result["input_tokens"],
    "output_tokens": result["output_tokens"],
    "cost": result["cost"]
}
