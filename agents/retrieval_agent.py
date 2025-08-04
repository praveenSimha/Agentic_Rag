# agents/retrieval_agent.py

from vector_store.store import VectorStore
from mcp.protocol import create_mcp_message

vector_store = VectorStore()

def ingest_documents_to_store(doc_chunks):
    vector_store.add_chunks(doc_chunks)

def retrieve_context(query):
    chunks = vector_store.search(query, top_k=5)
    return chunks

def handle_retrieval_request(mcp_msg):
    query = mcp_msg["payload"]["query"]
    context = retrieve_context(query)
    return create_mcp_message(
        sender="RetrievalAgent",
        receiver="LLMResponseAgent",
        type_="CONTEXT_RESPONSE",
        payload={"retrieved_context": context, "query": query}
    )
