from app.rag.pipeline import RAGPipeline
from app.llm.ollama_client import generate_answer


class QAPipeline:

    def __init__(self):

        self.rag = RAGPipeline()

    def index_document(
        self,
        document_path: str,
        source: str
    ):

        return self.rag.index_document(
            document_path=document_path,
            source=source
        )

    def answer_question(
        self,
        question: str,
        top_k: int = 3
    ):

        # Retrieve relevant evidence
        evidence = self.rag.retrieve(
            query=question,
            top_k=top_k
        )

        # Build context
        context_parts = []

        for i, item in enumerate(evidence):

            context_parts.append(
                f"""
Evidence {i + 1}
Source: {item['source']}
Chunk: {item['chunk_index']}

{item['text']}
"""
            )

        context = "\n".join(context_parts)

        # Generate answer
        answer = generate_answer(
            question=question,
            context=context
        )

        return {
            "question": question,
            "answer": answer,
            "evidence": evidence
        }