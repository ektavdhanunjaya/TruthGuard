from app.verification.claim_extractor import extract_claims


def main():

    answer = """
    Deep Learning is a subfield of Machine Learning.
    It uses artificial neural networks with multiple layers.
    These networks learn complex patterns from data.
    """

    claims = extract_claims(answer)

    print("\nCLAIM EXTRACTION")
    print("=" * 50)

    for i, claim in enumerate(claims):

        print(
            f"\nClaim {i + 1}: {claim}"
        )


if __name__ == "__main__":
    main()