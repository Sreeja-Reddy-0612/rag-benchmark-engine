# evaluation/retrieval_metrics.py

from typing import List


def recall_at_k(retrieved_doc_ids: List[str],
                relevant_doc_ids: List[str],
                k: int) -> float:
    """
    Recall@K = (# relevant docs in top K) / (total relevant docs)
    """
    retrieved_k = retrieved_doc_ids[:k]
    hits = len(set(retrieved_k) & set(relevant_doc_ids))
    return hits / len(relevant_doc_ids) if relevant_doc_ids else 0.0


def mean_reciprocal_rank(retrieved_doc_ids: List[str],
                         relevant_doc_ids: List[str]) -> float:
    """
    MRR = 1 / rank of first relevant document
    """
    for rank, doc_id in enumerate(retrieved_doc_ids, start=1):
        if doc_id in relevant_doc_ids:
            return 1.0 / rank
    return 0.0
