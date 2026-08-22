from pathlib import Path


def load_text_file(file_path: str) -> str:
    """
    Load a text document and return its contents.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    document_path = "../data/documents/ai_basics.txt"

    text = load_text_file(document_path)

    print("Document loaded successfully.")
    print(f"Characters: {len(text)}")
    print("\nFirst 500 characters:\n")
    print(text[:500])