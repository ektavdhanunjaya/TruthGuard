from app.rag.pipeline import RAGPipeline


DOCUMENT_PATH = "../data/documents/ai_basics.txt"


def main():

    pipeline = RAGPipeline()

    # Index document
    result = pipeline.index_document(
        document_path=DOCUMENT_PATH,
        source="ai_basics.txt"
    )

    print("\nINDEXING RESULT:")
    print(result)

    # Ask a question
    query = "What is deep learning?"

    evidence = pipeline.retrieve(
        query=query,
        top_k=3
    )

    print("\nQUESTION:")
    print(query)

    print("\nRETRIEVED EVIDENCE:")

    for i, item in enumerate(evidence):

        print(f"\n--- Evidence {i + 1} ---")

        print(f"Source: {item['source']}")

        print(
            f"Chunk: {item['chunk_index']}"
        )

        print(
            f"Distance: {item['distance']:.4f}"
        )

        print(f"Text: {item['text']}")


if __name__ == "__main__":
    main()