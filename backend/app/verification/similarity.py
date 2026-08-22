from sentence_transformers import SentenceTransformer


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