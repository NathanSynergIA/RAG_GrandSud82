import streamlit as st
import requests

# URL du webhook dans n8n
N8N_WEBHOOK_URL = "https://nathansynergiaa.app.n8n.cloud/webhook/9ba11544-5c4e-4f91-818a-08a4ecb596c5"

# Initialiser l'historique dans st.session_state
if "history" not in st.session_state:
    st.session_state.history = []
    
    # Interface utilisateur
st.title("Le Chatbot GrandSud82")
question = st.text_input("Posez votre question :", key="question")
    
if st.button("Envoyer"):
    if question.strip():
        # Envoyer la question au workflow n8n
        response = requests.post(N8N_WEBHOOK_URL, json={"question": question})
    
        # Vérifier la réponse
        if response.status_code == 200:
            answer = response.json().get("output", "Aucune réponse reçue.")
            st.write("Chatbot : ", answer)
    
            # Ajouter la question et la réponse à l'historique
            st.session_state.history.append({"question": question, "answer": answer})
    
        else:
            st.error("Erreur dans le traitement : " + response.text)
    
    # Afficher l'historique
    
st.markdown("---")  # Ligne de séparation
st.write("## Historique de la conversation")
for interaction in st.session_state.history:
    st.markdown(f"**Vous :** {interaction['question']}")
    st.markdown(f"**Chatbot :** {interaction['answer']}")
    
    # Effacer l'historique
if st.button("Effacer l'historique"):
    st.session_state.history = []

# Configuration de la barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Chatbot", "Documentation"])
