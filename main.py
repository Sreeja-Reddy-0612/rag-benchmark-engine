from evaluation.retrieval_metrics import recall_at_k, mean_reciprocal_rank
from evaluation.answer_quality import simple_answer_match
from evaluation.hallucination import is_hallucinated


def test_evaluation():
    retrieved_docs = ["offer", "policy","intern@"]
    relevant_docs = ["offer"]

    print("Recall@1:", recall_at_k(retrieved_docs, relevant_docs, k=1))
    print("MRR:", mean_reciprocal_rank(retrieved_docs, relevant_docs))

    generated = "This is an internship offer letter"
    expected = "internship offer"

    print("QA Score:", simple_answer_match(generated, expected))
    print(
        "Hallucinated:",
        is_hallucinated(generated, ["This is an internship offer letter"])
    )


test_evaluation()
