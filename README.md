# 🧠 AI Python Coding Tutor (Streamlit + LangChain + Ollama)

An interactive chatbot that explains Python concepts, gives examples, and provides coding challenges.

## 💡 Features
- Explains Python topics via natural language
- Generates examples using Mistral (via Ollama)
- Gives feedback on small code snippets
- Persistent concept memory via SQLite
- Streamlit interface

## 🛠 Tech Stack
- Python
- Streamlit (UI)
- LangChain (LLM orchestration)
- Ollama + Mistral (local LLM)
- DuckDuckGo Search (for code context)
- SQLite (for memory persistence)

## 🚀 How to Run Locally

```bash
git clone https://github.com/IshaGupta2010/python-ai-tutor.git
cd python-ai-tutor
pip install -r requirements.txt
ollama run mistral
streamlit run main.py
