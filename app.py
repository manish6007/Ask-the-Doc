import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import pdfplumber

import streamlit as st
import pdfplumber
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

def generate_response(document_text, openai_api_key, query_text):
    # Split document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.create_documents([document_text])
    # Select embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    # Create a vectorstore from documents
    db = Chroma.from_documents(texts, embeddings)
    # Create retriever interface
    retriever = db.as_retriever()
    # Create QA chain
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type='stuff', retriever=retriever)
    return qa.run(query_text)

# Page title
st.set_page_config(page_title='🦜🔗 Ask the Doc App')
st.title('🦜🔗 Ask the Doc App')

# File upload
uploaded_file = st.file_uploader('Upload a PDF file upto 4 pages', type='pdf')

# Query text
query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.', key='query')

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password')
    submitted = st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Processing...'):
            if uploaded_file is not None:
                with pdfplumber.open(uploaded_file) as pdf:
                    document_text = ""
                    for page in pdf.pages:
                        document_text += page.extract_text()
                response = generate_response(document_text, openai_api_key, query_text)
                result.append(response)
                del openai_api_key

if len(result) > 0:
    st.info(result[0])