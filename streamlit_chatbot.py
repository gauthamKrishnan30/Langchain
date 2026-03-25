import streamlit as st
from langchain_chatbot import get_response

st.set_page_config(page_title="Langchain Chatbot")

st.title("Langchain Chatbot")

user_input= st.text_input("Enter the topic:")


if  st.button("Search"):
    if user_input:
        response=get_response(user_input)
        st.write(response)

    else:
        st.warning("Please enter a topic to search.")