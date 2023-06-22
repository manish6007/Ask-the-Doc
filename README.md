# Ask-the-Doc

## Ask the Doc App

This code represents an "Ask the Doc" application using Streamlit, which allows users to upload a text document and ask questions related to the document. The application utilizes various components from the `langchain` library to process the document and generate responses to user queries.

### Code Explanation

The code can be divided into two main parts: the `generate_response` function and the Streamlit application itself.

#### `generate_response` Function

The `generate_response` function takes three parameters: `uploaded_file`, `openai_api_key`, and `query_text`. Here is a breakdown of what the function does:

1. If a file is uploaded (`uploaded_file` is not `None`), it reads the file contents and decodes it using the UTF-8 encoding.
2. The function splits the document into smaller chunks using the `CharacterTextSplitter` from the `langchain` library. Each chunk has a size of 1000 characters with no overlap.
3. It selects the embeddings using the `OpenAIEmbeddings` class from `langchain`, providing the OpenAI API key.
4. The function creates a vectorstore (`db`) from the document chunks using the `Chroma` class from `langchain`.
5. A retriever interface is created from the vectorstore using the `as_retriever` method.
6. Finally, a retrieval-based question answering (QA) chain is created using the `RetrievalQA` class from `langchain`, providing the OpenAI API key, chain type, and the retriever. The function then runs the QA chain on the given query text and returns the response.

#### Streamlit Application

The Streamlit application is as follows:

1. The page title is set to "🦜🔗 Ask the Doc App" using `st.set_page_config` and displayed as a level-one title using `st.title`.
2. The user is prompted to upload a text document using `st.file_uploader`.
3. A text input field is provided for the user to enter their question using `st.text_input`.
4. The OpenAI API key is requested using `st.text_input` with the password type.
5. A form is created using `st.form` to handle the submission of the OpenAI API key and the query text.
6. Upon form submission, if the OpenAI API key starts with "sk-", the `generate_response` function is called, and the response is stored in the `result` list.
7. If a response is available, it is displayed as an info message using `st.info`.

### Usage

To use the "Ask the Doc" application:

1. Install the required dependencies, including Streamlit and the `langchain` library.
2. Run the code in a Python environment that supports Streamlit.
3. Access the application through the provided URL.
4. Upload a text document by clicking on the "Upload an article" button.
5. Enter your question in the text input field.
6. Provide your OpenAI API key in the corresponding text input field.
7. Click the "Submit" button.
8. Wait for the response to be generated and displayed on the page.

Note: Make sure to handle the API key securely, as it is currently being entered as a password input but can be further enhanced based on security requirements.

This application can be customized and extended to meet specific requirements by modifying the code as needed.

<img width="398" alt="image" src="https://github.com/manish6007/Ask-the-Doc/assets/41223158/7e965cbc-2777-4740-a805-3d6c0cc61474">

