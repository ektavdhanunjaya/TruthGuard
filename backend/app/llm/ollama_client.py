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

def classify_claim(
    claim: str,
    evidence: str
) -> str:

    prompt = f"""
You are a strict fact verification system.

Your task is to determine whether the EVIDENCE supports,
contradicts, or is insufficient to verify the CLAIM.

Return exactly ONE label:

SUPPORTED
CONTRADICTED
UNCERTAIN

Definitions:

SUPPORTED:
The evidence directly states or clearly implies that the claim is true.

CONTRADICTED:
The evidence directly states information that conflicts with the claim,
or explicitly says that the claim is false.

UNCERTAIN:
The evidence does not contain enough information to determine whether
the claim is true or false.

IMPORTANT:

1. Use ONLY the evidence provided.
2. Do NOT use outside knowledge.
3. Do NOT assume that missing information means the claim is false.
4. Do NOT assume that a claim is true merely because it sounds plausible.
5. Compare the meaning of the claim with the meaning of the evidence.
6. Return ONLY the classification label.

CLAIM:
{claim}

EVIDENCE:
{evidence}

CLASSIFICATION:
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

    result = response["message"]["content"].strip().upper()

    if "CONTRADICTED" in result:
        return "CONTRADICTED"

    if "SUPPORTED" in result:
        return "SUPPORTED"

    return "UNCERTAIN"