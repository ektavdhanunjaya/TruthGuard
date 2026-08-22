import re


def extract_claims(answer: str) -> list[str]:
    """
    Split an answer into individual claims/sentences.
    """

    sentences = re.split(
        r"(?<=[.!?])\s+",
        answer.strip()
    )

    claims = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        # Ignore very short fragments
        if len(sentence.split()) < 4:
            continue

        claims.append(sentence)

    return claims