# 💄 GlowAI Cosmetic Assistant

An AI-powered cosmetic shop assistant built using OpenAI's GPT API and Streamlit.

This application demonstrates structured LLM outputs, modular architecture, conversational state management, and cloud deployment.

---

## 🚀 Features

- Conversational AI product assistant
- Structured JSON responses from GPT
- Smart product pre-filtering before LLM call
- Add-to-cart simulation
- Session-based memory
- Modular project architecture
- Secure API key handling
- Deployed via Streamlit Cloud

---

## 🧠 Architecture Overview

User Input  
→ Product Filtering (Python logic)  
→ LLM Call (GPT-4o-mini with structured output)  
→ Parsed JSON Response  
→ Dynamic UI Rendering  

---

## 📂 Project Structure

glowai-cosmetic-assistant/
│
├── app.py
├── ai/
│ └── assistant.py
├── data/
│ └── products.py
├── utils/
│ └── filter.py
│
├── requirements.txt
└── .gitignore


---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenAI GPT-4o-mini
- Modular architecture
- Cloud deployment

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

https://glowai-cosmetic-assistant-bootrun1a.streamlit.app/

---

