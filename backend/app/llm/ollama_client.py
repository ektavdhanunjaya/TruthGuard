import ollama


MODEL_NAME = "qwen2.5:3b"


def generate_answer(
    question: str,
    context: str
) -> str:

    prompt = f"""
You are an AI assistant.

Answer the user's question using the provided context.

IMPORTANT RULES:
1. Use only the information provided in the context.
2. Do not invent facts.
3. If the context does not contain enough information, say:
   "I don't have enough information in the provided context."
4. Give a clear and concise answer.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]