import streamlit as st
from main import call_ui

st.set_page_config(page_title="Bhagwat Gita Chatbot", page_icon="📜", layout="centered")

st.title("🕉 Bhagwat Gita Chatbot 🕉")

user_input = st.text_input("📜Discover clarity and peace – ask your question to the Geeta...")

if st.button("Ask to Devote"):
    if user_input:
        answer = call_ui(user_input)    
        st.write(f"**Hare Krishna🌸🪷**\n\n {answer}")

    else:
        user_input = None
        st.warning("Please Ask Your Query")

