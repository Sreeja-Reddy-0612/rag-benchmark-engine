# cost/token_counter.py

def estimate_tokens(text: str) -> int:
    """
    Rough token estimation (1 token ≈ 4 chars).
    Good enough for cost benchmarking.
    """
    return max(1, len(text) // 4)
