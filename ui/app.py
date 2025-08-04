import streamlit as st
import tempfile
import os
import sys

# ✅ Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Try importing the pipeline
try:
    from main import run_query_pipeline
except Exception as e:
    run_query_pipeline = None
    st.warning(f"⚠️ Couldn't import pipeline: {e}")

# Streamlit UI setup
st.set_page_config(page_title="📄 Agentic RAG Chatbot", layout="wide")
st.title("📄 Agentic RAG Chatbot with Agentic Architecture")

# Debug confirmation
st.markdown("✅ Streamlit loaded successfully.")

# File uploader
uploaded_files = st.file_uploader(
    "📁 Upload your documents (PDF, DOCX, PPTX, TXT, CSV, Markdown):",
    type=["pdf", "docx", "pptx", "txt", "csv", "md"],
    accept_multiple_files=True
)

# Query input
query = st.text_input("🧠 Ask a question from the documents:")

# Button
if st.button("🔍 Get Answer"):
    if not uploaded_files:
        st.warning("Please upload at least one document.")
    elif not query:
        st.warning("Please enter a question.")
    elif run_query_pipeline is None:
        st.error("Pipeline not available (check import of main.py).")
    else:
        with st.spinner("💬 Processing your query..."):
            file_paths = []

            # Save uploaded files temporarily
            for uploaded_file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.name}") as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    file_paths.append(tmp_file.name)

            try:
                # Run the pipeline
                result = run_query_pipeline(file_paths, query)

                # ✅ Fix: Access result from payload
                st.markdown("### ✅ Answer:")
                st.success(result["payload"]["answer"])

                st.markdown("### 📚 Retrieved Context:")
                st.code(result["payload"]["context"])

            except Exception as e:
                st.error("❌ Error during processing.")
                st.exception(e)
