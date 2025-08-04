from mcp.protocol import create_mcp_message
from transformers import pipeline

# Load the QA model from Hugging Face (you can swap with a local model if needed)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def handle_llm_request(mcp_message):
    # Deduplicate context chunks to avoid repeated content
    retrieved_chunks = mcp_message["payload"].get("retrieved_context", [])
    unique_chunks = list(dict.fromkeys(retrieved_chunks))  # Removes duplicates, preserves order

    # Join the context
    context = "\n".join(unique_chunks)
    question = mcp_message["payload"].get("query", "")

    # Perform Question Answering
    response = qa_pipeline(question=question, context=context)

    # Return new MCPMessage
    return create_mcp_message(
        sender="LLMResponseAgent",
        receiver="UI",
        type_="LLM_RESPONSE",
        payload={
            "answer": response["answer"],
            "context": context
        }
    )
