from app.verification.contradiction import ContradictionDetector


def main():

    detector = ContradictionDetector()

    claim = (
        "Deep Learning was invented in 1986 "
        "by Geoffrey Hinton."
    )

    evidence = [
        (
            "Deep Learning developed through research "
            "over several decades and does not have "
            "a single inventor."
        )
    ]

    result = detector.check(
        claim,
        evidence
    )

    print("\nTRUTHGUARD CONTRADICTION TEST")
    print("=" * 60)

    print(
        f"\nClaim:\n{claim}"
    )

    print(
        f"\nContradiction Score: "
        f"{result['contradiction_score']:.4f}"
    )

    print(
        f"Contradicted: "
        f"{result['contradicted']}"
    )


if __name__ == "__main__":
    main()