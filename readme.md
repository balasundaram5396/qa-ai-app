# AskMeText-AI Agent for Document & Text Q&A

This application allows users to upload text documents (TXT, PDF) or paste text directly and ask questions about the content using the power of Large Language Models (LLMs).

## Features

* **Document Upload:** Supports TXT and PDF file uploads.
* **Direct Text Input:** Allows users to paste text directly for Q&A.
* **Question Answering:** Uses Langchain and OpenAI to generate answers based on the provided text.
* **Simple and Clean UI:** Built with Streamlit for an easy-to-use interface.
* **Free Deployment:** Deployed using the free tier of Streamlit Community Cloud.

## Technologies Used

* **Python:** The primary programming language.
* **Langchain:** A framework for building LLM applications.
* **OpenAI API:** Provides the powerful language models.
* **Streamlit:** A library for creating interactive web applications in Python.
* **pypdf:** For processing PDF files.
* **unstructured:** For processing various document types.
* **Chroma:** For creating and managing vector embeddings.
* **python-dotenv:** For managing environment variables locally.

## Setup (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_GITHUB_REPOSITORY_URL>
    cd ai_agent_qa_app
    ```
    (Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository URL)

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```
    (Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key)

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

## Deployment (Streamlit Cloud)

1.  **Push your code to a public GitHub repository.**
2.  **Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign up/log in.**
3.  **Click "New app" and follow the instructions to deploy from your GitHub repository.**
4.  **Add your OpenAI API key as a secret in the Streamlit Cloud dashboard with the key `OPENAI_API_KEY`.**

## Further Improvements

* Support for more document types (e.g., DOCX).
* More sophisticated prompt engineering.
* User authentication and data privacy considerations.
* Options for different LLM models.
* Saving chat history.

