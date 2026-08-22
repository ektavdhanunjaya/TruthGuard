from app.verification.similarity import SimilarityChecker


def main():

    checker = SimilarityChecker()

    answer = """
    Deep Learning is a subfield of Machine Learning
    that uses artificial neural networks with multiple
    layers to learn complex patterns.
    """

    supporting_evidence = """
    Deep Learning is a subfield of Machine Learning
    that uses artificial neural networks with multiple
    layers to learn complex patterns from data.
    """

    unrelated_evidence = """
    Natural Language Processing enables computers
    to process and understand human language.
    """

    support_score = checker.calculate(
        answer,
        supporting_evidence
    )

    unrelated_score = checker.calculate(
        answer,
        unrelated_evidence
    )

    print("\nSIMILARITY TEST")

    print(
        f"\nSupporting evidence: "
        f"{support_score:.4f}"
    )

    print(
        f"Unrelated evidence: "
        f"{unrelated_score:.4f}"
    )


if __name__ == "__main__":
    main()