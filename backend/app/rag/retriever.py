import chromadb

from app.rag.embeddings import EmbeddingModel


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.client = chromadb.PersistentClient(
            path="storage/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="truthguard_documents"
        )

    def add_documents(
        self,
        chunks: list[str],
        source: str = "unknown"
    ):

        embeddings = self.embedding_model.encode(chunks)

        ids = [
            f"{source}_chunk_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {
                "source": source,
                "chunk_index": i
            }
            for i in range(len(chunks))
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

        print(
            f"Added {len(chunks)} chunks to ChromaDB."
        )

    def search(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = self.embedding_model.encode(
            [query]
        )[0]

        results = self.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k
        )

        return results