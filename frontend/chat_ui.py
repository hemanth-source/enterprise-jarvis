import streamlit as st
import requests

st.set_page_config(page_title="Enterprise Jarvis 🤖")

st.title("🤖 Enterprise Jarvis")
st.write("Your internal AI copilot")

query = st.text_input("Ask me anything...")

if st.button("Send"):
    response = requests.post(
        "http://localhost:8000/chat",
        params={"query": query}
    )
    st.success(response.json()["answer"])
