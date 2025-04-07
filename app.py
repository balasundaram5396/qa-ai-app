import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredFileLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os # No need for dotenv anymore in deployed environment

openai_api_key = st.secrets["OPENAI_API_KEY"]

if not openai_api_key:
    st.error("OpenAI API key not found in Streamlit Secrets.")
    st.stop()

llm = OpenAI(openai_api_key=openai_api_key)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

st.title("AI Agent for Document & Text Q&A")
st.sidebar.header("Configuration")
st.sidebar.markdown("Enter your OpenAI API key in the `.env` file.")

# Document Q&A Section
st.subheader("Ask Questions About a Document")
uploaded_file = st.file_uploader("Upload a text or PDF document", type=["txt", "pdf"])
question_doc = st.text_input("Your Question:", key="question_doc")
if uploaded_file is not None and question_doc:
    with st.spinner("Processing document and generating answer..."):
        try:
            file_extension = uploaded_file.name.split(".")[-1].lower()
            if file_extension == "pdf":
                loader = PyPDFLoader(uploaded_file)
                documents = loader.load()
            elif file_extension == "txt":
                loader = TextLoader(uploaded_file)
                documents = loader.load()
            else:
                loader = UnstructuredFileLoader(uploaded_file)
                documents = loader.load()

            db = Chroma.from_documents(documents, embeddings)
            qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
            response = qa.run(question_doc)
            st.success(f"Answer: {response}")

        except Exception as e:
            st.error(f"Error processing the document: {e}")

st.markdown("---")

# Direct Text Q&A Section
st.subheader("Ask Questions About Direct Text")
direct_text = st.text_area("Enter your text here:", height=150)
direct_question = st.text_input("Your Question:", key="question_direct")
if direct_text and direct_question:
    with st.spinner("Generating answer..."):
        try:
            response = llm(f"{direct_text}\n\nQuestion: {direct_question}\nAnswer:")
            st.success(f"Answer: {response}")
        except Exception as e:
            st.error(f"Error generating answer: {e}")