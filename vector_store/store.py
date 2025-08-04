import faiss
import os
import pickle
from vector_store.embedder import embed_texts

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []
        self.embeddings = []

    def add_chunks(self, chunks):
        vectors = embed_texts(chunks)
        self.embeddings.extend(vectors)
        self.text_chunks.extend(chunks)
        self.index.add(vectors)

    def search(self, query, top_k=5):
        query_vec = embed_texts([query])
        D, I = self.index.search(query_vec, top_k)
        results = [self.text_chunks[i] for i in I[0] if i < len(self.text_chunks)]
        return results


