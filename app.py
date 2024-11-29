"""
Project: VeritAI - Chat with Web
Author: Murilo Krominski
Description: Chatbot interface with AI for interaction based on information extracted from the web.
"""

# requirements.txt contains:
# streamlit==1.39.0       # Streamlit is a library for creating interactive web applications in Python.
# langchain==0.3.7        # LangChain facilitates integration of language models in applications.
# langchain-groq==0.2.1   # Tools to use Groq's language model with LangChain.
# langchain-community==0.3.5 # Community module of LangChain with additional plugins.
# bs4                     # BeautifulSoup, for web scraping.
# python-dotenv           # Library to load environment variables from a .env file.

import streamlit as st             # Imports the Streamlit library for the user interface.
import os                           # Imports the os module for environment variable handling.
from langchain_groq import ChatGroq # Imports the ChatGroq model for AI interactions.
from langchain.prompts import ChatPromptTemplate # Prompt templates for conversations with AI.
from langchain_community.document_loaders import WebBaseLoader # Loads data from web pages.
from dotenv import load_dotenv      # Loads environment variables from the .env file.

# Load environment variables from the .env file
load_dotenv()

# API key and model configuration
api_key = os.getenv('GROQ_API_KEY') # Retrieves the API key from the .env file
os.environ['GROQ_API_KEY'] = api_key # Sets the API key as an environment variable

# Initializes the AI model for chat with the model "llama-3.1-70b-versatile"
chat = ChatGroq(model='llama-3.1-70b-versatile')

# Function to generate chatbot response
def generate_response(messages, document):
    # Initial system message defining the assistant's role
    system_message = '''You are an assistant named VeritAI, developed by Murilo Krominski.
    Use the following information to formulate your responses: {information}'''
    
    # Models the input messages for the prompt
    message_model = [('system', system_message)] + messages
    
    # Creates a prompt template using LangChain
    template = ChatPromptTemplate.from_messages(message_model)
    
    # Defines the execution chain of the template for the chat model
    chain = template | chat
    
    # Invokes the model with the information and returns the generated content
    return chain.invoke({'information': document}).content

# Function to load content from a website with the provided URL
def load_content(site_url):
    loader = WebBaseLoader(site_url)  # Initializes the loader with the URL
    documents = loader.load()         # Loads the page content
    return ''.join(doc.page_content for doc in documents) # Joins the content into a single string

# User interface with Streamlit
st.title('🌐VeritAI - Chat with Web')  # Sets the application title

# Input field for the user to provide the website URL to load
site_url = st.text_input("Enter the website URL to retrieve information:", value="https://murilokrominski.github.io/autor.htm")
if site_url:
    document = load_content(site_url)   # Loads the site's content
    st.write("Content loaded successfully!") # Displays a success message

# Session initialization to store chat messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []   # Creates an empty list for messages in the session

# User question input and response generation
question = st.text_input('Your question: ') # Input field for the question
if question:
    st.session_state["messages"].append(('user', question)) # Adds the question to the session
    response = generate_response(st.session_state["messages"], document) # Generates the response using the loaded document
    st.session_state["messages"].append(('assistant', response)) # Stores the response
    st.write(f"VeritAI: {response}")  # Displays the chatbot response
    st.markdown("---")                # Divider line

# Thank-you message and credits
st.markdown("---")   # Divider line
st.write("Thank you for using VeritAI - Chat with Web.")  # Thank-you message
st.write("This open-source AI chatbot was developed by me to interact with the user based on information extracted from user-provided websites, offering a concise and efficient solution for developers who will see simple, streamlined, and effective code.") # Project description
st.write("This code will also serve as a base for future advanced applications that you can check out on the [Author's Repository](https://murilokrominski.github.io).") # Link to the repository
st.write("Developed by Murilo Krominski.")  # Credit to the author
st.write("https://murilokrominski.github.io") # Link to the author's website