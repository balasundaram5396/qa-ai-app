import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    st.error("OpenAI API key not found. Please create a .env file with your OPENAI_API_KEY.")
    st.stop()

llm = OpenAI(openai_api_key=openai_api_key)

st.title("Simple Text Q&A Agent")

user_input = st.text_area("Enter your text here:", height=200)
question = st.text_input("Ask a question about the text:")

if st.button("Get Answer"):
    if user_input and question:
        try:
            response = llm(f"{user_input}\n\nQuestion: {question}\nAnswer:")
            st.success(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter text and a question.")