from app.verification.claim_verifier import ClaimVerifier


def main():

    verifier = ClaimVerifier(
        support_threshold=0.65
    )

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
        """
    ]

    results = verifier.verify(
        answer=answer,
        evidence=evidence
    )

    print("\nCLAIM VERIFICATION")
    print("=" * 60)

    for i, result in enumerate(results):

        status = (
            "SUPPORTED"
            if result["supported"]
            else "UNSUPPORTED"
        )

        print(f"\nClaim {i + 1}:")
        print(result["claim"])

        print(
            f"Similarity: "
            f"{result['similarity']:.4f}"
        )

        print(
            f"Status: {status}"
        )


if __name__ == "__main__":
    main()