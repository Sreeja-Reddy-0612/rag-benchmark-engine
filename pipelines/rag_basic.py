# pipelines/rag_basic.py

from typing import List, Dict
from vectorstore.retriever import Retriever


class BasicRAGPipeline:
    def __init__(self, retriever: Retriever, llm_client):
        self.retriever = retriever
        self.llm = llm_client

    def _build_prompt(self, query: str, contexts: List[str]) -> str:
        context_block = "\n\n".join(contexts)

        return f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context_block}

Question:
{query}

Answer:
""".strip()

    def run(self, query: str, top_k: int = 5) -> Dict:
        retrieved = self.retriever.retrieve(query, top_k=top_k)

        contexts = [r["metadata"]["text"] for r in retrieved]
        sources = [r["metadata"]["doc_id"] for r in retrieved]

        prompt = self._build_prompt(query, contexts)

        result = self.llm.generate(prompt)

        return {
            "answer": result["text"],
            "sources": list(set(sources)),
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
            "cost": result["cost"]
        }
