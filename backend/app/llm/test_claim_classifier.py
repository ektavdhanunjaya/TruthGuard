from app.llm.ollama_client import classify_claim


def main():

    claim = (
        "Deep Learning was invented in 1986 "
        "by Geoffrey Hinton."
    )

    evidence = (
        "Deep Learning developed through research "
        "over several decades and does not have "
        "a single inventor."
    )

    result = classify_claim(
        claim,
        evidence
    )

    print("\nTRUTHGUARD CLAIM CLASSIFIER")
    print("=" * 60)

    print("\nCLAIM:")
    print(claim)

    print("\nEVIDENCE:")
    print(evidence)

    print("\nCLASSIFICATION:")
    print(result)


if __name__ == "__main__":
    main()