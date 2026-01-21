<img width="1916" height="1033" alt="image" src="https://github.com/user-attachments/assets/7cec1290-8220-443c-86c0-014303c5816e" />

# Enterprise Jarvis

### Self-Hosted AI Assistant for Enterprise Knowledge

Enterprise Jarvis is a **self-hosted, AI-powered enterprise assistant** inspired by tools like ChatGPT and internal copilots used in modern organizations.
It allows users to query internal knowledge using **Retrieval-Augmented Generation (RAG)** powered by a local LLM and a vector database.

---

##  Features

*  **Self-Hosted LLM** using LLaMA (via Ollama)
*  **Semantic Search** with Pinecone Vector Database
*  **Retrieval-Augmented Generation (RAG)**
*  **FastAPI Backend** for scalable APIs
*  **Modern Chat UI** built with Streamlit
*  **Knowledge Ingestion Pipeline**
*  **Offline UI fallback** for greetings (demo-safe)
*  Secure configuration using environment variables

---

##  Architecture Overview

```
User (Streamlit UI)
        |
        v
FastAPI Backend (REST API)
        |
        v
Query Embeddings (SentenceTransformers)
        |
        v
Pinecone Vector Database
        |
        v
Relevant Context Retrieval
        |
        v
LLaMA (Local LLM via Ollama)
        |
        v
Final Response to User
```

---

##  Tech Stack

| Layer       | Technology           |
| ----------- | -------------------- |
| Frontend    | Streamlit            |
| Backend     | FastAPI              |
| LLM         | LLaMA (Ollama)       |
| Embeddings  | SentenceTransformers |
| Vector DB   | Pinecone             |
| Language    | Python               |
| Environment | Python 3.9+          |

---

##  Project Structure

```
enterprise-jarvis/
│
├── backend/
│   ├── app.py              # FastAPI application
│   ├── llm.py              # LLM interaction logic
│   ├── vector_store.py     # Pinecone vector operations
│   ├── ingest.py           # Knowledge ingestion script
│   ├── config.py           # Configuration loader
│   └── requirements.txt
│
├── frontend/
│   ├── chat_ui.py          # Streamlit chat interface
│   └── requirements.txt
│
├── data/
│   └── knowledge.txt       # Sample enterprise knowledge
│
├── .env                    # Environment variables (not committed)
├── README.md
└── run.sh                  # Optional run helper
```

---

##  Setup Instructions

### 1️ Clone the Repository

```bash
git clone https://github.com/your-username/enterprise-jarvis.git
cd enterprise-jarvis
```

---

### 2️ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️ Install Dependencies

#### Backend

```bash
cd backend
pip install -r requirements.txt
```

#### Frontend

```bash
cd ../frontend
pip install -r requirements.txt
```

---

### 4️ Configure Environment Variables

Create `.env` in project root:

```env
PINECONE_API_KEY=your_api_key_here
PINECONE_ENV=us-east-1
PINECONE_INDEX=enterprise-jarvis
```

---

### 5️ Start LLaMA (Ollama)

```bash
ollama pull llama3
ollama run llama3
```

---

### 6️ Ingest Knowledge

```bash
cd backend
python ingest.py
```

---

### 7️ Run Backend API

```bash
uvicorn app:app --reload
```

Check:

```
http://localhost:8000/docs
```

---

### 8️ Run Frontend UI

```bash
cd frontend
streamlit run chat_ui.py
```

Open:

```
http://localhost:8501
```

---

##  Example Usage

**User:**

```
hello
```

**Jarvis (offline-safe):**

```
Hello  I’m Enterprise Jarvis. How can I help you today?
```

**User:**

```
What is this platform about?
```

**Jarvis:**

```
This platform is an enterprise AI assistant designed to query internal knowledge using semantic search and a local LLM.
```

---

##  Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector embeddings and similarity search
* Self-hosted LLMs
* API-driven architecture
* Enterprise-ready AI design patterns

---

##  Use Cases

* Internal company knowledge assistant
* Governance, Risk & Compliance copilots
* Document Q&A systems
* AI helpdesk assistant
* Secure, offline AI deployments

---

##  Security Notes

* API keys stored in `.env`
* `.env` excluded via `.gitignore`
* No sensitive data committed

---


