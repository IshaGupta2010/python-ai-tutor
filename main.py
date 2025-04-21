import streamlit as st
from tutor_logic import ask_tutor

st.set_page_config(page_title="Python AI Tutor", layout="wide")
st.title("👨‍🏫 Python AI Coding Tutor")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a Python question:")

if user_input:
    response = ask_tutor(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Tutor", response))

for role, text in st.session_state.chat_history[::-1]:
    st.markdown(f"**{role}:** {text}")
