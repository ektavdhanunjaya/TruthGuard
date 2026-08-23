from app.verification.engine import VerificationEngine


def main():

    engine = VerificationEngine()

    answer = """
    Deep Learning is a subfield of Machine Learning.

    It uses artificial neural networks with multiple layers.

    Deep Learning was invented in 1986 by Geoffrey Hinton.
    """

    evidence = [
        """
        Deep Learning is a subfield of Machine Learning
        that uses artificial neural networks with multiple
        layers to learn complex patterns from data.

        Deep learning developed through research over several
        decades and does not have a single inventor. Geoffrey
        Hinton is one of the important researchers who
        contributed significantly to the development of
        deep learning.
        """
    ]

    result = engine.verify(
        answer=answer,
        evidence=evidence
    )

    print("\n" + "=" * 60)
    print("TRUTHGUARD VERIFICATION ENGINE")
    print("=" * 60)

    print(
        f"\nClaim Support: "
        f"{result['claim_support']:.2%}"
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
        f"{result['trust_score']:.2%}"
    )

    print(
        f"Status: "
        f"{result['status']}"
    )

    print("\nSEMANTIC + NLI + LLM VERIFICATION")
    print("-" * 60)

    for i, claim in enumerate(
        result["claim_results"]
    ):

        print(f"\nClaim {i + 1}:")
        print(claim["claim"])

        print(
            f"Semantic Similarity: "
            f"{claim['similarity']:.4f}"
        )

        print(
            f"Semantic Status: "
            f"{claim['semantic_status']}"
        )

        print(
            f"NLI Status: "
            f"{claim['nli_status']}"
        )

        print(
            f"FINAL STATUS: "
            f"{claim['final_status']}"
        )

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()