# evaluation/answer_quality.py

def simple_answer_match(generated: str, expected: str) -> float:
    """
    Very simple overlap-based QA score (0–1).
    """
    generated = generated.lower()
    expected = expected.lower()

    expected_tokens = set(expected.split())
    generated_tokens = set(generated.split())

    if not expected_tokens:
        return 0.0

    overlap = expected_tokens & generated_tokens
    return len(overlap) / len(expected_tokens)
