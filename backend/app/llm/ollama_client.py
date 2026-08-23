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

Determine whether the EVIDENCE supports the CLAIM.

Return exactly ONE label:

SUPPORTED
CONTRADICTED
UNCERTAIN

Definitions:

SUPPORTED:
The evidence directly states or clearly implies the claim.

CONTRADICTED:
The evidence explicitly conflicts with the claim.

UNCERTAIN:
The evidence does not provide enough information.

IMPORTANT:

1. Use ONLY the provided evidence.
2. Do NOT use outside knowledge.
3. Missing information is NOT contradiction.
4. Similar wording is NOT contradiction.
5. Do not guess.
6. Return ONLY one label.

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
        ],
        options={
            "temperature": 0
        }
    )

    result = (
        response["message"]["content"]
        .strip()
        .upper()
    )

    if result == "SUPPORTED":
        return "SUPPORTED"

    if result == "CONTRADICTED":
        return "CONTRADICTED"

    return "UNCERTAIN"

def check_contradiction(
    claim: str,
    evidence: str
) -> bool:

    prompt = f"""
You are a strict contradiction detector.

Determine whether the EVIDENCE directly contradicts the CLAIM.

Return exactly one word:

YES
NO

YES means:
The evidence contains information that conflicts with the claim.

NO means:
The evidence does not directly contradict the claim.

Important rules:

1. Use ONLY the provided evidence.
2. Do NOT use outside knowledge.
3. Do NOT treat missing information as a contradiction.
4. Do NOT treat similar wording as a contradiction.
5. Look specifically for factual conflicts.
6. If the evidence explicitly says something that cannot be true
   at the same time as the claim, return YES.
7. Otherwise return NO.
8. Return ONLY YES or NO.

CLAIM:
{claim}

EVIDENCE:
{evidence}

ANSWER:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0
        }
    )

    result = (
        response["message"]["content"]
        .strip()
        .upper()
    )

    return result == "YES"