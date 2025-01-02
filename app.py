import streamlit as st
from chatbot import chatbot_page
from documentation import documentation_page

# Configuration de la barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Chatbot", "Documentation"])

# Appeler les pages en fonction du choix
if page == "Chatbot":
    chatbot_page()
elif page == "Documentation":
    documentation_page()
