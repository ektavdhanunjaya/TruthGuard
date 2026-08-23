from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.rag.qa_pipeline import QAPipeline
from app.verification.engine import VerificationEngine


app = FastAPI(
    title="TruthGuard API",
    description="Self-Verifying RAG Engine for Hallucination Detection and Mitigation",
    version="0.1.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Request model
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str


# --------------------------------------------------
# Initialize pipelines
# --------------------------------------------------

qa_pipeline = QAPipeline()
verification_engine = VerificationEngine()


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "TruthGuard API"
    }


# --------------------------------------------------
# Ask question
# --------------------------------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):

    # 1. Retrieve evidence and generate answer
    qa_result = qa_pipeline.answer_question(
        question=request.question,
        top_k=3
    )

    answer = qa_result["answer"]
    evidence = qa_result["evidence"]

    # 2. Extract evidence text for verification
    evidence_text = [
        item["text"]
        for item in evidence
    ]

    # 3. Verify generated answer
    verification_result = verification_engine.verify(
        answer=answer,
        evidence=evidence_text
    )

    # 4. Return complete TruthGuard result
    return {
        "question": request.question,

        "answer": answer,

        "status": verification_result["status"],

        "trust_score": verification_result["trust_score"],

        "claim_support": verification_result["claim_support"],

        "average_claim_similarity": (
            verification_result["average_claim_similarity"]
        ),

        "evidence_similarity": (
            verification_result["evidence_similarity"]
        ),

        "claims": verification_result["claim_results"],

        "llm_verification": verification_result["llm_results"],

        "evidence": evidence
    }