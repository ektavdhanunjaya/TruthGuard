import re


def split_into_sentences(text: str) -> list[str]:
    """
    Split text into sentences using basic punctuation rules.
    """

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text.strip()
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
) -> list[str]:
    """
    Create sentence-aware overlapping chunks.
    """

    sentences = split_into_sentences(text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:

        if not current_chunk:

            current_chunk = sentence

        elif len(current_chunk) + len(sentence) + 1 <= chunk_size:

            current_chunk += " " + sentence

        else:

            chunks.append(current_chunk.strip())

            # Keep some previous context
            overlap_text = current_chunk[-overlap:]

            current_chunk = (
                overlap_text + " " + sentence
            )

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks