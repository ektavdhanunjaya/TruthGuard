from app.verification.claim_verifier import ClaimVerifier
from app.verification.trust_score import calculate_trust_score
from app.verification.similarity import SimilarityChecker
from app.llm.ollama_client import classify_claim


class VerificationEngine:

    def __init__(self):

        self.claim_verifier = ClaimVerifier()
        self.similarity_checker = SimilarityChecker()

    def verify(
        self,
        answer: str,
        evidence: list[str]
    ) -> dict:

        # --------------------------------------------------
        # 1. Semantic claim verification
        # --------------------------------------------------

        claim_results = self.claim_verifier.verify(
            answer=answer,
            evidence=evidence
        )

        # --------------------------------------------------
        # 2. Combine evidence
        # --------------------------------------------------

        combined_evidence = "\n".join(
            evidence
        )

        # --------------------------------------------------
        # 3. Calculate answer-to-evidence similarity
        # --------------------------------------------------

        evidence_similarity = (
            self.similarity_checker.calculate(
                answer,
                combined_evidence
            )
        )

        # --------------------------------------------------
        # 4. LLM-based claim classification
        # --------------------------------------------------

        llm_results = []

        for claim_result in claim_results:

            classification = classify_claim(
                claim=claim_result["claim"],
                evidence=combined_evidence
            )

            llm_results.append(
                {
                    "claim": claim_result["claim"],
                    "classification": classification
                }
            )

        # --------------------------------------------------
        # 5. Combine semantic + LLM verification
        # --------------------------------------------------

        final_claim_results = []

        for semantic_result, llm_result in zip(
            claim_results,
            llm_results
        ):

            semantic_status = (
                "SUPPORTED"
                if semantic_result["similarity"] >= 0.75
                else (
                    "UNCERTAIN"
                    if semantic_result["similarity"] >= 0.50
                    else "UNSUPPORTED"
                )
            )

            llm_status = llm_result["classification"]

            
            # --------------------------------------------------
            # Combine semantic + LLM verification
            # --------------------------------------------------

            # Strong semantic evidence should protect against
            # false LLM contradictions.
            if (
                semantic_result["similarity"] >= 0.65
                and llm_status == "CONTRADICTED"
            ):
                final_status = "SUPPORTED"

            elif llm_status == "CONTRADICTED":
                final_status = "CONTRADICTED"

            elif llm_status == "SUPPORTED":
                final_status = "SUPPORTED"

            elif semantic_status == "SUPPORTED":
                final_status = "SUPPORTED"
 
            elif semantic_status == "UNSUPPORTED":
                final_status = "UNSUPPORTED"

            else:
                final_status = "UNCERTAIN"

        # --------------------------------------------------
        # 6. Calculate final claim support
        # --------------------------------------------------

        total_claims = len(final_claim_results)

        if total_claims == 0:

            claim_support = 0.0

        else:

            supported_claims = sum(
                1
                for result in final_claim_results
                if result["final_status"] == "SUPPORTED"
            )

            claim_support = (
                supported_claims / total_claims
            )

        # --------------------------------------------------
        # 7. Calculate average semantic similarity
        # --------------------------------------------------

        if total_claims == 0:

            average_claim_similarity = 0.0

        else:

            average_claim_similarity = sum(
                result["similarity"]
                for result in final_claim_results
            ) / total_claims

        # --------------------------------------------------
        # 8. Calculate overall trust score
        # --------------------------------------------------

        trust_score = (
            0.6 * claim_support
            +
            0.4 * evidence_similarity
        )

        # --------------------------------------------------
        # 9. Determine overall status
        # --------------------------------------------------

        contradicted_count = sum(
            1
            for result in final_claim_results
            if result["final_status"] == "CONTRADICTED"
        )

        uncertain_count = sum(
            1
            for result in final_claim_results
            if result["final_status"] == "UNCERTAIN"
        )

        if contradicted_count > 0:

            overall_status = "WARNING"

        elif trust_score >= 0.75:

            overall_status = "RELIABLE"

        elif uncertain_count > 0:

            overall_status = "UNCERTAIN"

        else:

            overall_status = "WARNING"

        # --------------------------------------------------
        # 10. Return complete verification result
        # --------------------------------------------------

        return {

            "claim_results": final_claim_results,

            "llm_results": llm_results,

            "evidence_similarity": evidence_similarity,

            "claim_support": claim_support,

            "average_claim_similarity": average_claim_similarity,

            "trust_score": trust_score,

            "status": overall_status

        }