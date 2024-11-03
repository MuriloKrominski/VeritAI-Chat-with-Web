<a href="https://veritai-chat-with-web.streamlit.app">
<img src="https://raw.githubusercontent.com/MuriloKrominski/VeritAI-Chat-with-Web/refs/heads/main/VeritAI-Chat-with-Web.png" alt="VeritAI - Chat with Web" style="max-width: 1280px; max-height: 640px; width: au
to; height: auto;">
</a>

# VeritAI - Chat with Web
<br>
By <a href="https://murilokrominski.github.io/autor.htm">Murilo Krominski</a>.
 

### Project Description
VeritAI is an AI-based chatbot developed to interact with users using information extracted from the web. This project provides an intuitive and functional interface that utilizes advanced language models to generate responses based on content extracted from a website specified by the user.

The project is developed in Python and leverages powerful libraries like **Streamlit** (for user interface), **LangChain** (for creating conversational AI workflows), and **BeautifulSoup** (for web content extraction). The code is modular and well-documented, allowing for easy expansion for future implementations.

---

### Required Files

1. **requirements.txt**: Specifies the project dependencies.
2. **.env**: Environment file to securely store the API key.

#### requirements.txt

The `requirements.txt` file contains the essential dependencies for the project. After creating a virtual environment, install these dependencies with the command `pip install -r requirements.txt`.

```plaintext
streamlit==1.39.0
langchain==0.3.7
langchain-groq==0.2.1
langchain-community==0.3.5
bs4
python-dotenv
```

---

### Code Structure and Explanation

#### Importing Modules

```python
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
```

These imports include essential modules:

- **Streamlit**: For building a user interface accessible via browser.
- **os** and **dotenv**: For secure environment variable management.
- **LangChain** and **LangChain-Groq**: For creating and managing AI-based conversations.
- **WebBaseLoader**: To load and convert web content into text.

#### Loading Environment Variables

```python
# Load environment variables from the .env file
load_dotenv()
```

Here, `load_dotenv()` is used to load environment variables from the `.env` file, which contains the API key for the model.

#### API and Model Configuration

```python
# API and model configuration
api_key = os.getenv('GROQ_API_KEY')  # Use your API key here!
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')
```

This segment sets up the model and API key. The model `llama-3.1-70b-versatile` is defined here for later use in interactions.

#### Function to Generate Chatbot Responses

```python
def generate_response(messages, document):
    system_message = '''You are an assistant named VeritAI, developed by Murilo Krominski.
    Use the following information to formulate your responses: {information}'''
    message_model = [('system', system_message)] + messages
    template = ChatPromptTemplate.from_messages(message_model)
    chain = template | chat
    return chain.invoke({'information': document}).content
```

The `generate_response()` function generates the chatbot’s response:

1. Defines a custom system message to inform the chatbot about the context of the conversation.
2. Uses the `ChatPromptTemplate` class to combine the system message with user messages.
3. Calls the configured AI model to generate a response based on the extracted information from the document.

#### Function to Load Content from the Website

```python
def load_content(site_url):
    loader = WebBaseLoader(site_url)
    documents = loader.load()
    return ''.join(doc.page_content for doc in documents)
```

The `load_content()` function is responsible for extracting and returning content from a website using the provided URL. It combines the loaded content into a single text, which will then be passed as reference to the chatbot.

#### User Interface with Streamlit

```python
# Application title
st.title('VeritAI - Chat with Web')

# URL input for loading content
site_url = st.text_input("Enter the website URL to retrieve information:", value="https://murilokrominski.github.io/autor.htm")
if site_url:
    document = load_content(site_url)
    st.write("Content loaded successfully!")
```

Here, we build the user interface using Streamlit:

1. `st.title` sets the application title.
2. `st.text_input` creates an input field for the user to enter the website URL.
3. Upon entering a URL, `load_content()` is called to extract the website content, which is then displayed as a confirmation.

#### Session Initialization to Store Messages

```python
if "messages" not in st.session_state:
    st.session_state["messages"] = []
```

This check initializes a list of messages in the session, ensuring that user and chatbot messages are stored throughout the interaction.

#### User Question Input and Response Generation

```python
# User question input and response generation
question = st.text_input('Your question: ')
if question:
    st.session_state["messages"].append(('user', question))
    response = generate_response(st.session_state["messages"], document)
    st.session_state["messages"].append(('assistant', response))
    st.write(f"VeritAI: {response}")
    st.markdown("---")
```

Here, the user can input their question. The `generate_response()` function is then called to generate the chatbot’s response based on the question and the information loaded from the website. The response is displayed on the user interface.

#### Thank You Message and Credits

```python
# Thank you message and credits
st.markdown("---")
st.write("Thank you for using VeritAI - Chat with Web.")
st.write("This open-source AI chatbot was developed by me to interact with the user based on information extracted from user-provided websites, offering a concise and efficient solution for developers who will see simple, streamlined, and effective code.")
st.write("This code will also serve as a base for future advanced applications that you can check out on the [Author's Repository](https://murilokrominski.github.io).")
st.write("Developed by Murilo Krominski.")
st.write("https://murilokrominski.github.io")
```

Finally, a thank-you and credits section is displayed to the user, with links to the developer’s repository.

---

### Final Project Structure

To ensure the project functions correctly, the file structure should be as follows:

```
VeritAI
├── veritai_app.py       # Main chatbot code
├── requirements.txt     # List of project dependencies
├── .env                 # Contains the variable GROQ_API_KEY=<your_api_key>
└── README.md            # Project documentation
```

### Running the Project

After configuring the project, run the chatbot with the command:

```bash
streamlit run veritai_app.py
```

This command will initialize the application on Streamlit, where users can interact with VeritAI by providing URLs and asking questions to receive informed responses directly from the specified website content.

---

### Conclusion

The VeritAI project demonstrates a practical and professional application of chatbots that use AI and web content extraction. This code serves as a solid foundation for developers who want to build interactive chatbots with dynamic information retrieval from online sources.
