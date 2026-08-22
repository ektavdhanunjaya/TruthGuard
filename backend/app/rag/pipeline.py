from app.rag.loader import load_text_file
from app.rag.chunker import chunk_text
from app.rag.retriever import Retriever


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

    def index_document(
        self,
        document_path: str,
        source: str
    ):

        # Load document
        text = load_text_file(document_path)

        # Split into chunks
        chunks = chunk_text(
            text,
            chunk_size=500,
            overlap=100
        )

        # Store chunks
        self.retriever.add_documents(
            chunks,
            source=source
        )

        return {
            "source": source,
            "chunks_created": len(chunks)
        }

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):

        results = self.retriever.search(
            query,
            top_k=top_k
        )

        evidence = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            evidence.append(
                {
                    "text": document,
                    "source": metadata["source"],
                    "chunk_index": metadata["chunk_index"],
                    "distance": distance
                }
            )

        return evidence