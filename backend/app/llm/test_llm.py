from app.llm.ollama_client import generate_answer


def main():

    question = "What is deep learning?"

    context = """
    Deep Learning is a subfield of Machine Learning
    that uses artificial neural networks with multiple
    layers to learn complex patterns from data.
    """

    answer = generate_answer(
        question=question,
        context=context
    )

    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")
    print(answer)


if __name__ == "__main__":
    main()