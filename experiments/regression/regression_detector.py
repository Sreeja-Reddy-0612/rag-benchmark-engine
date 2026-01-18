def detect_regression(current: dict, baseline: dict) -> dict:
    """
    Compare current metrics with baseline and detect regressions.
    """

    regressions = {}

    regressions["recall_regressed"] = (
        current["recall@5"] < baseline["recall@5"] * 0.95
    )

    regressions["mrr_regressed"] = (
        current["mrr"] < baseline["mrr"] * 0.95
    )

    regressions["qa_regressed"] = (
        current["qa_score"] < baseline["qa_score"] * 0.90
    )

    regressions["cost_regressed"] = (
        current["avg_cost"] > baseline["avg_cost"] * 1.20
    )

    regressions["any_regression"] = any(regressions.values())

    return regressions
