import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Streamlit page configuration
st.set_page_config(page_title="Gemini Vision Chatbot")

st.title("🖼️ Gemini Vision Chatbot")
st.write("Upload an image and ask Gemini anything about it.")

# User input
prompt = st.text_input("Enter your prompt")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

image = None

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Submit button
if st.button("Generate Response"):

    if image is None:
        st.warning("Please upload an image.")
    else:
        with st.spinner("Generating response..."):

            if prompt.strip():
                contents = [prompt, image]
            else:
                contents = [image]

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents
            )

            st.subheader("Gemini Response")
            st.write(response.text)