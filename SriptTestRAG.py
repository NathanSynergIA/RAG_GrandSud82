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

def documentation_page():
    st.title("Documentation / README")
    st.markdown("""
    ## Bienvenue sur la documentation de l'application
    Voici quelques informations utiles pour vous guider dans l'utilisation de ce chatbot :
    
    ### Fonctionnalités
    - Posez vos questions dans l'onglet "Chatbot".
    - Obtenez des réponses basées sur un workflow intelligent grâce à n8n.
    - Suivez l'historique de vos interactions.

    ### Conseils d'utilisation
    - Posez des questions claires et précises pour des réponses optimales.
    - Si une réponse semble incorrecte, reformulez votre question.

    ### À propos
    Développé par [Votre Nom ou Entreprise], avec une intégration entre Streamlit et n8n.
    """)
    
# Configuration de la barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Chatbot", "Documentation"])

# Appeler les pages en fonction du choix
if page == "Documentation":
    documentation_page()
