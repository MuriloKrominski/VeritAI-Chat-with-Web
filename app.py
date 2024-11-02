"""
Project: VeritAI - Chat with Web
Author: Murilo Krominski
Description: Chatbot interface with AI for interaction based on information extracted from the web.
"""

# requirements.txt contains:
# streamlit==1.39.0
# langchain==0.3.7
# langchain-groq==0.2.1
# langchain-community==0.3.5
# bs4import os
# python-dotenv

import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# API and model configuration
api_key = os.getenv('GROQ_API_KEY') # Use your API key here! https://console.groq.com/keys
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

# Function to generate chatbot response
def generate_response(messages, document):
    system_message = '''You are an assistant named VeritAI, developed by Murilo Krominski.
    Use the following information to formulate your responses: {information}'''
    message_model = [('system', system_message)] + messages
    template = ChatPromptTemplate.from_messages(message_model)
    chain = template | chat
    return chain.invoke({'information': document}).content

# Function to load content from a website based on the provided URL
def load_content(site_url):
    loader = WebBaseLoader(site_url)
    documents = loader.load()
    return ''.join(doc.page_content for doc in documents)

# User interface with Streamlit
st.title('VeritAI - Chat with Web')

# URL input for loading content
site_url = st.text_input("Enter the website URL to retrieve information:", value="https://murilokrominski.github.io/autor.htm")
if site_url:
    document = load_content(site_url)
    st.write("Content loaded successfully!")

# Session initialization to store messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User question input and response generation
question = st.text_input('Your question: ')
if question:
    st.session_state["messages"].append(('user', question))
    response = generate_response(st.session_state["messages"], document)
    st.session_state["messages"].append(('assistant', response))
    st.write(f"VeritAI: {response}")
    st.markdown("---")

# Thank you message and credits
st.markdown("---")
st.write("Thank you for using VeritAI - Chat with Web.")
st.write("This open-source AI chatbot was developed by me to interact with the user based on information extracted from user-provided websites, offering a concise and efficient solution for developers who will see simple, streamlined, and effective code.")
st.write("This code will also serve as a base for future advanced applications that you can check out on the [Author's Repository](https://murilokrominski.github.io).")
st.write("Developed by Murilo Krominski.")
st.write("https://murilokrominski.github.io")