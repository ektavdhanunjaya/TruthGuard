from app.verification.claim_extractor import extract_claims
from app.verification.similarity import SimilarityChecker


class ClaimVerifier:

    def __init__(
        self,
        support_threshold: float = 0.65
    ):

        self.similarity_checker = SimilarityChecker()

        self.support_threshold = support_threshold

    def verify(
        self,
        answer: str,
        evidence: list[str]
    ):

        claims = extract_claims(answer)

        results = []

        combined_evidence = "\n".join(
            evidence
        )

        for claim in claims:

            score = self.similarity_checker.calculate(
                claim,
                combined_evidence
            )

            supported = (
                score >= self.support_threshold
            )

            results.append(
                {
                    "claim": claim,
                    "similarity": score,
                    "supported": supported
                }
            )

        return results