
from agents.ingestion_agent import handle_ingestion
from agents.retrieval_agent import handle_retrieval_request
from agents.llm_response_agent import handle_llm_request

def run_query_pipeline(file_paths, query):
    from mcp.protocol import create_mcp_message

    all_chunks = []

    for path in file_paths:
        mcp_ingestion = create_mcp_message(
            sender="CoordinatorAgent",
            receiver="IngestionAgent",
            type_="DOC_INGESTION",
            payload={"file_path": path}
        )
        ingestion_response = handle_ingestion(mcp_ingestion)

        # FIX HERE:
        all_chunks.extend(ingestion_response["payload"]["chunks"])

    mcp_retrieval = create_mcp_message(
        sender="CoordinatorAgent",
        receiver="RetrievalAgent",
        type_="RETRIEVE_CONTEXT",
        payload={"query": query}
    )

    # Store chunks first (since it's semantic retrieval)
    from agents.retrieval_agent import ingest_documents_to_store
    ingest_documents_to_store(all_chunks)

    mcp_retrieval_response = handle_retrieval_request(mcp_retrieval)
    mcp_llm_response = handle_llm_request(mcp_retrieval_response)

    return mcp_llm_response