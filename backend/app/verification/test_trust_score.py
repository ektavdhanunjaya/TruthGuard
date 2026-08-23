from app.verification.trust_score import calculate_trust_score


def main():

    claim_results = [
        {
            "claim": "Deep Learning is a subfield of Machine Learning.",
            "similarity": 0.91,
            "supported": True
        },
        {
            "claim": "Deep Learning uses artificial neural networks.",
            "similarity": 0.89,
            "supported": True
        },
        {
            "claim": "Deep Learning uses multiple layers.",
            "similarity": 0.87,
            "supported": True
        },
        {
            "claim": "Deep Learning was invented in 1986.",
            "similarity": 0.31,
            "supported": False
        }
    ]

    evidence_similarity = 0.82

    result = calculate_trust_score(
        claim_results=claim_results,
        evidence_similarity=evidence_similarity
    )

    print("\nTRUTHGUARD TRUST SCORE")
    print("=" * 60)

    print(
        f"\nClaim Support: "
        f"{result['claim_support']:.4f}"
    )

    print(
        f"Average Claim Similarity: "
        f"{result['average_claim_similarity']:.4f}"
    )

    print(
        f"Evidence Similarity: "
        f"{result['evidence_similarity']:.4f}"
    )

    print(
        f"Trust Score: "
        f"{result['trust_score']:.4f}"
    )

    print(
        f"Trust Score (%): "
        f"{result['trust_score'] * 100:.2f}%"
    )

    print(
        f"Status: "
        f"{result['status']}"
    )


if __name__ == "__main__":
    main()