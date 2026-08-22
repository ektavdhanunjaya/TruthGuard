from app.rag.loader import load_text_file
from app.rag.chunker import chunk_text
from app.rag.retriever import Retriever


DOCUMENT_PATH = "../data/documents/ai_basics.txt"


def main():

    # 1. Load document
    text = load_text_file(DOCUMENT_PATH)

    print("Document loaded.")

    # 2. Split document
    chunks = chunk_text(
        text,
        chunk_size=500,
        overlap=100
    )

    print(f"Created {len(chunks)} chunks.")

    # 3. Create retriever
    retriever = Retriever()

    # 4. Store chunks
    retriever.add_documents(
        chunks,
        source="ai_basics.txt"
    )

    # 5. Search
    query = "What is deep learning?"

    results = retriever.search(
        query,
        top_k=3
    )

    print("\nQUESTION:")
    print(query)

    print("\nRETRIEVED EVIDENCE:")

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for i, document in enumerate(documents):

        print(f"\n--- Evidence {i + 1} ---")

        print(
            f"Source: {metadatas[i]['source']}"
        )

        print(
            f"Chunk: {metadatas[i]['chunk_index']}"
        )

        print(
            f"Distance: {distances[i]:.4f}"
        )

        print(document)


if __name__ == "__main__":
    main()