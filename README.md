
# 📄 Agentic RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot with an **agentic architecture** and **Model Context Protocol (MCP)**. This system allows users to upload multi-format documents (PDF, DOCX, TXT, etc.) and ask natural language questions. The chatbot uses LLMs to answer based on the retrieved document chunks.

---

## 🧠 Features

- ✅ Agent-based modular design
- ✅ Handles PDFs, DOCX, TXT, CSV, PPTX, Markdown
- ✅ Ingestion, retrieval, and LLM-response agents
- ✅ DistilBERT from HuggingFace for QA
- ✅ Retrieval with semantic similarity (FAISS ready)
- ✅ Streamlit UI for interaction
- ✅ Context flow with Model Context Protocol (MCP)

---

## 🗂️ Project Structure

```bash
Agentic_RAG/
├── agents/
│   ├── ingestion_agent.py
│   ├── retrieval_agent.py
│   └── llm_response_agent.py
├── mcp/
│   └── protocol.py
├── ui/
│   └── app.py
├── main.py
├── README.md
└── requirements.txt
````

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/praveenSimha/Agentic_Rag.git
cd agentic-rag-chatbot
```

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

```bash
streamlit run ui/app.py
```

> You'll get a web-based interface where you can upload documents and ask questions.

---

## 🧩 Core Components

### `mcp/protocol.py`

Defines the `MCPMessage` structure and `create_mcp_message()` function.

### `agents/ingestion_agent.py`

Ingests the documents and chunks their content into manageable pieces.

### `agents/retrieval_agent.py`

Performs basic semantic similarity checks and selects top relevant chunks. Uses `ingest_documents_to_store()` internally.

### `agents/llm_response_agent.py`

Uses Hugging Face’s DistilBERT for question answering over the retrieved context.

### `main.py`

Coordinates all agents and implements the `run_query_pipeline()`.

### `ui/app.py`

Streamlit UI to upload files and input user queries.

---

## 🧪 Supported File Formats

* `.pdf`
* `.docx`
* `.txt`
* `.csv`
* `.md`
* `.pptx`

---

## 🧠 Technologies Used

* Python
* Streamlit
* HuggingFace Transformers (`distilbert-base-uncased-distilled-squad`)
* FastAPI-style modular agents
* FAISS-ready architecture
* WebSockets & async-ready design (backend friendly)
* Model Context Protocol (custom coordination)

---

## 📌 TODO / Improvements

* [ ] Integrate OpenAI / LLaMA-2 for better LLM responses
* [ ] Enable multi-agent coordination using LangChain
* [ ] Add logging and tracing via `trace_id`
* [ ] Add authentication for deployment

---

## 🧑‍💻 Author

**Praveen Gubbala**


📫 Connect: [LinkedIn](https://www.linkedin.com/in/gpln)

---

## 📄 License

This project is licensed under the MIT License.
Feel free to use and modify for educational or personal use.


