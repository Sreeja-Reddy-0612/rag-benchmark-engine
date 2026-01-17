# evaluation/hallucination.py

from typing import List


def is_hallucinated(answer: str, contexts: List[str]) -> bool:
    """
    Detect hallucination by checking if answer tokens
    appear in retrieved context.
    """
    context_text = " ".join(contexts).lower()
    answer_tokens = answer.lower().split()

    unsupported = [
        token for token in answer_tokens
        if token not in context_text
    ]

    # If too many unsupported tokens → hallucination
    return len(unsupported) / max(len(answer_tokens), 1) > 0.4
