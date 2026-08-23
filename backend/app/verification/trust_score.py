def calculate_trust_score(
    claim_results: list[dict],
    evidence_similarity: float
) -> dict:

    if not claim_results:

        return {
            "claim_support": 0.0,
            "average_claim_similarity": 0.0,
            "evidence_similarity": evidence_similarity,
            "trust_score": 0.0,
            "status": "UNSUPPORTED"
        }

    status_weights = {
        "SUPPORTED": 1.0,
        "UNCERTAIN": 0.5,
        "UNSUPPORTED": 0.0
    }

    weighted_support = sum(
        status_weights.get(
            result.get(
                "status",
                "UNSUPPORTED"
            ),
            0.0
        )
        for result in claim_results
    )

    total_claims = len(claim_results)

    claim_support = (
        weighted_support / total_claims
    )

    average_claim_similarity = sum(
        result["similarity"]
        for result in claim_results
    ) / total_claims

    trust_score = (
        0.40 * claim_support
        +
        0.30 * average_claim_similarity
        +
        0.30 * evidence_similarity
    )

    if trust_score >= 0.75:

        status = "RELIABLE"

    elif trust_score >= 0.45:

        status = "WARNING"

    else:

        status = "UNSUPPORTED"

    return {
        "claim_support": claim_support,
        "average_claim_similarity": average_claim_similarity,
        "evidence_similarity": evidence_similarity,
        "trust_score": trust_score,
        "status": status
    }