# 💄 GlowAI - RAG Cosmetic Assistant

An AI-powered cosmetic shop assistant built using OpenAI, LangChain, FAISS, and Streamlit.

This project demonstrates Retrieval-Augmented Generation (RAG) with semantic search and structured LLM outputs.
---

## 🧠 What This Project Demonstrates

- Retrieval-Augmented Generation (RAG)
- Vector search with FAISS
- Semantic product retrieval using embeddings
- Structured JSON outputs from GPT
- Conversational memory
- Session state management
- Modular Python architecture
- Secure API key handling
- Cloud deployment via Streamlit

---

## 🏗 Architecture Overview

User Query  
↓  
OpenAI Embeddings  
↓  
FAISS Vector Store (Semantic Search)  
↓  
Top-K Retrieved Products  
↓  
GPT-4o-mini (Structured Response)  
↓  
Streamlit UI + Cart Logic  

---

## 📂 Project Structure

glowai-cosmetic-assistant/
│
├── app.py
├── requirements.txt
│
├── ai/
│ ├── assistant.py # LLM interaction
│ └── rag.py # Vector store + retrieval
│
├── data/
│ └── products.py # Product catalog
│
└── .env


---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenAI GPT-4o-mini
- OpenAI Embeddings (text-embedding-3-small)
- LangChain (v1 architecture)
- FAISS Vector Store

---

## 🔐 Environment Variables

The application requires:

OPENAI_API_KEY


For local development, use a `.env` file.  
For production deployment, configure secrets in Streamlit Cloud.

---

## 📈 What This Project Demonstrates

- Prompt engineering
- Context injection
- Controlled LLM output (JSON enforcement)
- State management in Streamlit
- Production-style secret management
- Deployment workflow with GitHub + Streamlit

---

## 🌍 Live Demo

https://glowai-cosmetic-assistant-bootrun1b.streamlit.app/

---

