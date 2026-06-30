from dotenv import load_dotenv
import os
import streamlit as st
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.set_page_config(page_title="Gemini Chatbot")
st.header("Gemini Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything")

if st.button("Submit") and user_input:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    answer = response.text

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Gemini", answer))

st.subheader("Chat History")

for role, message in st.session_state.chat_history:
    st.write(f"**{role}:** {message}")