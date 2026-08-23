import re

from sentence_transformers import CrossEncoder


MODEL_NAME = "cross-encoder/nli-deberta-v3-base"


class ContradictionChecker:

    def __init__(self):

        self.model = CrossEncoder(
            MODEL_NAME
        )

    def classify(
        self,
        claim: str,
        evidence: str
    ) -> str:

        # --------------------------------------------------
        # 1. NLI classification
        # --------------------------------------------------

        scores = self.model.predict(
            [(evidence, claim)]
        )

        labels = [
            "CONTRADICTION",
            "ENTAILMENT",
            "NEUTRAL"
        ]

        nli_result = labels[
            int(scores.argmax())
        ]

        # --------------------------------------------------
        # 2. Explicit contradiction detection
        # --------------------------------------------------

        if self.detect_explicit_contradiction(
            claim,
            evidence
        ):

            return "CONTRADICTION"

        return nli_result

    def detect_explicit_contradiction(
        self,
        claim: str,
        evidence: str
    ) -> bool:

        claim_lower = claim.lower()
        evidence_lower = evidence.lower()

        # --------------------------------------------------
        # Pattern 1:
        # "X was invented by Y"
        # vs
        # "does not have a single inventor"
        # --------------------------------------------------

        invention_claim = (
            "invented" in claim_lower
            or "inventor" in claim_lower
        )

        no_single_inventor = (
            "does not have a single inventor" in evidence_lower
            or "no single inventor" in evidence_lower
            or "not have a single inventor" in evidence_lower
        )

        if invention_claim and no_single_inventor:

            return True

        # --------------------------------------------------
        # Pattern 2:
        # "X was created by Y"
        # vs
        # evidence says there was no single creator
        # --------------------------------------------------

        creation_claim = (
            "created by" in claim_lower
            or "created in" in claim_lower
        )

        no_single_creator = (
            "does not have a single creator" in evidence_lower
            or "no single creator" in evidence_lower
        )

        if creation_claim and no_single_creator:

            return True

        # --------------------------------------------------
        # Pattern 3:
        # "X was founded by Y"
        # vs evidence explicitly says otherwise
        # --------------------------------------------------

        founder_match = re.search(
            r"founded by ([a-z\s]+)",
            claim_lower
        )

        if founder_match:

            founder = founder_match.group(1).strip()

            if (
                "not founded by" in evidence_lower
                or f"was not founded by {founder}" in evidence_lower
            ):

                return True

        return False

    def is_contradicted(
        self,
        claim: str,
        evidence: str
    ) -> bool:

        return (
            self.classify(
                claim,
                evidence
            )
            == "CONTRADICTION"
        )