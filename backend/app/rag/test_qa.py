from app.rag.qa_pipeline import QAPipeline


DOCUMENT_PATH = "../data/documents/ai_basics.txt"


def main():

    pipeline = QAPipeline()

    # Index document
    result = pipeline.index_document(
        document_path=DOCUMENT_PATH,
        source="ai_basics.txt"
    )

    print("\nINDEXING RESULT:")
    print(result)

    # Ask question
    question = "What is deep learning?"

    result = pipeline.answer_question(
        question=question,
        top_k=3
    )

    print("\n" + "=" * 60)
    print("TRUTHGUARD QUESTION ANSWERING")
    print("=" * 60)

    print("\nQUESTION:")
    print(result["question"])

    print("\nANSWER:")
    print(result["answer"])

    print("\nEVIDENCE:")

    for i, item in enumerate(
        result["evidence"]
    ):

        print(
            f"\n[{i + 1}] "
            f"{item['source']} "
            f"(Chunk {item['chunk_index']})"
        )

        print(item["text"])


if __name__ == "__main__":
    main()