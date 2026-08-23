from sentence_transformers import SentenceTransformer
import re


MODEL_NAME = "all-MiniLM-L6-v2"


class SimilarityChecker:

    def __init__(self):

        self.model = SentenceTransformer(
            MODEL_NAME
        )

    def calculate(
        self,
        answer: str,
        evidence: str
    ) -> float:

        embeddings = self.model.encode(
            [answer, evidence],
            normalize_embeddings=True
        )

        similarity = float(
            embeddings[0] @ embeddings[1]
        )

        return similarity

    def find_best_evidence(
        self,
        claim: str,
        evidence: str
    ) -> tuple[str, float]:

        sentences = re.split(
            r"(?<=[.!?])\s+",
            evidence.strip()
        )

        sentences = [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

        if not sentences:
            return "", 0.0

        embeddings = self.model.encode(
            [claim] + sentences,
            normalize_embeddings=True
        )

        claim_embedding = embeddings[0]

        evidence_embeddings = embeddings[1:]

        similarities = (
            evidence_embeddings @ claim_embedding
        )

        best_index = int(
            similarities.argmax()
        )

        return (
            sentences[best_index],
            float(similarities[best_index])
        )

    def calculate_claim_similarity(
        self,
        claim: str,
        evidence: str
    ) -> float:

        _, score = self.find_best_evidence(
            claim,
            evidence
        )

        return score