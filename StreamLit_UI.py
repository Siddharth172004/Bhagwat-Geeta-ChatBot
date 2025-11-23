import streamlit as st
from main import call_ui

st.set_page_config(page_title="Bhagwat Geeta Chatbot", page_icon="📜", layout="centered")

st.title("🕉 Bhagwat Geeta Chatbot 🕉")
st.markdown("Ask your query and seek wisdom from the Bhagwat Geeta.")

user_input = st.text_input("📜Discover clarity and peace – ask your question to the Geeta...")

if st.button("Ask to Devote"):
    
    answer = call_ui(user_input)    
    st.write(f"**Hare Krishna🌸🪷**\n\n {answer}")

else:
    st.warning("Please Ask Your Query")

