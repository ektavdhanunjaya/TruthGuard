from app.verification.claim_extractor import extract_claims
from app.verification.similarity import SimilarityChecker


class ClaimVerifier:

    def __init__(
        self,
        supported_threshold: float = 0.65,
        uncertain_threshold: float = 0.50
    ):

        self.similarity_checker = SimilarityChecker()

        self.supported_threshold = supported_threshold
        self.uncertain_threshold = uncertain_threshold

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

            if score >= self.supported_threshold:

                status = "SUPPORTED"

            elif score >= self.uncertain_threshold:

                status = "UNCERTAIN"

            else:

                status = "UNSUPPORTED"

            results.append(
                {
                    "claim": claim,
                    "similarity": score,
                    "supported": status == "SUPPORTED",
                    "status": status
                }
            )

        return results