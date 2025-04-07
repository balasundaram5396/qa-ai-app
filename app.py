import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredFileLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    st.error("OpenAI API key not found. Please create a .env file with your OPENAI_API_KEY.")
    st.stop()

llm = OpenAI(openai_api_key=openai_api_key)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

st.title("Document Q&A Agent")

uploaded_file = st.file_uploader("Upload a text or PDF document", type=["txt", "pdf"])
question = st.text_input("Ask a question about the document:")

if uploaded_file is not None and question:
    try:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "pdf":
            loader = PyPDFLoader(uploaded_file)
            documents = loader.load()
        elif file_extension == "txt":
            loader = TextLoader(uploaded_file)
            documents = loader.load()
        else:
            loader = UnstructuredFileLoader(uploaded_file.name) # Try unstructured as a fallback
            documents = loader.load()

        # Create embeddings and store in a vector database
        db = Chroma.from_documents(documents, embeddings)

        # Create a retrieval-based question answering system
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())

        response = qa.run(question)
        st.success(response)

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("Alternatively, enter text directly:")
direct_text = st.text_area("Enter your text here for direct Q&A:", height=150)
direct_question = st.text_input("Ask a question about the direct text:")

if direct_text and direct_question:
    try:
        response = llm(f"{direct_text}\n\nQuestion: {direct_question}\nAnswer:")
        st.success(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")