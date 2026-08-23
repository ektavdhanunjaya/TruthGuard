from app.verification.similarity import SimilarityChecker


class ContradictionDetector:

    def __init__(
        self,
        contradiction_threshold: float = 0.70
    ):

        self.similarity_checker = SimilarityChecker()

        self.contradiction_threshold = (
            contradiction_threshold
        )

    def check(
        self,
        claim: str,
        evidence: list[str]
    ):

        if not evidence:

            return {
                "contradicted": False,
                "contradiction_score": 0.0
            }

        combined_evidence = "\n".join(evidence)

        score = self.similarity_checker.calculate(
            claim,
            combined_evidence
        )

        return {
            "contradicted": False,
            "contradiction_score": score
        }