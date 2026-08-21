from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="TruthGuard API",
    description="Self-Verifying RAG Engine for Hallucination Detection and Mitigation",
    version="0.1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "TruthGuard API"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": "This is the initial TruthGuard backend response.",
        "status": "warning",
        "truth_probability": 0.5,
        "evidence": []
    }