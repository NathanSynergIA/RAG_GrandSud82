import streamlit as st
import requests

# URL du webhook dans n8n
N8N_WEBHOOK_URL = "https://nathansynergiaa.app.n8n.cloud/webhook/9ba11544-5c4e-4f91-818a-08a4ecb596c5"


# Définir le mot de passe
PASSWORD = "test"  # Changez ce mot de passe pour sécuriser l'accès

def check_password():
    """Vérifie si le mot de passe est correct."""
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        # Champ de saisie du mot de passe
        password = st.text_input("🔒 Entrez le mot de passe pour accéder au chatbot :", type="password")
        if st.button("Valider"):
            if password == PASSWORD:
                st.session_state.password_correct = True
                st.success("✅ Accès autorisé ! Bienvenue dans le Chatbot.")
            else:
                st.error("❌ Mot de passe incorrect. Veuillez réessayer.")
        return False
    else:
        return True
if check_password():

    # Initialiser l'historique dans st.session_state
    if "history" not in st.session_state:
        st.session_state.history = []
        
        # Interface utilisateur
    
    col1, col2, col3 = st.columns([1, 2, 1])  # Ajuster les proportions si nécessaire
    
        # Afficher le logo de SynergIA
    with col1:
        st.image("LogoSynergIA.png", width=800)
    
        # Afficher le texte au centre
    with col2:
        st.markdown(
                """
                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <span style="font-size: 18px; font-weight: bold;"></span>
                </div>
                """,
                unsafe_allow_html=True,
            )
    
        # Afficher le logo de GrandSudTarnetGaronne
    with col3:
        st.image("GrandSud.png", width=700)
        
    st.title("Chatbot GrandSud82")
    
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
    # Rendre invisible l'historique et les discussions lorsqu'on affiche la documentation
        
        st.title("Documentation / README")
        st.markdown(
            """
           
            Ce chatbot est conçu pour répondre à vos questions en se basant sur les délibérations hebdomadaires du conseil de la communauté de communes.
    
            ### Fonctionnement du Chatbot
            Le chatbot utilise une base de données constituée de fichiers PDF contenant les délibérations hebdomadaires.
            - Vous posez une question.
            - Le bot recherche la réponse dans la base de données et vous la fournit.
    
            ### Maintenance hebdomadaire
            Chaque dimanche, l'administrateur général, **Nathan Bruyere** (nathan.bruyere@synergiaa.fr), met à jour la base de données en ajoutant les nouveaux fichiers PDF des délibérations.
            - Si un ou plusierus fichiers doivent être ajoutés en urgence, contactez **Nathan Bruyere** (nathan.bruyere@synergiaa.fr) par e-mail.
    
            ### Rédiger une bonne question (prompt)
            Une bonne question, ou "prompt", est essentielle pour obtenir une réponse précise. Voici quelques conseils :
            1. Soyez précis : Donnez un maximum de détails pertinents dans votre question.
            2. Formulez votre question clairement : Évitez les formulations vagues.
            3. Incluez des mots-clés : Mentionnez les éléments importants comme des noms, des dates ou des montants.
    
            #### Exemples de bons prompts :
            - "De combien était le montant du contrat de 2022 avec l'entreprise X ?"
            - "Quel est le contenu de la délibération du 15 janvier 2023 concernant le budget ?"
            - "Quels sont les partenaires mentionnés dans la délibération du 10 mars 2023 ?"
            - "Quel est le coût global HT de la proposition de programme de travaux des ponts pour 2025 ?"
            - "Peux tu me dire de combien était le montant TTC de l'achat de panneaux cyclables à la société SIGNAUX GIROD ?"
    
            #### Exemples de prompts vagues :
            - "Parle-moi des contrats."
            - "Qu'est-ce qui s'est passé en 2022 ?"
    
            Si le bot ne comprend pas votre question ou donne une réponse imprécise, reformulez en ajoutant plus de contexte ou de détails.
    
            ### Questions fréquentes
            - **Q : De combien était le montant du contrat de 2022 avec l'entreprise X ?**
              - R : Le bot cherchera ce montant dans les délibérations et vous fournira la réponse exacte.
            - **Q : Quels projets ont été approuvés en janvier 2023 ?**
              - R : Le bot listera les projets mentionnés dans les délibérations de cette période.
    
            ### Support technique
            Si vous rencontrez un problème ou avez des questions concernant l'utilisation du chatbot, contactez l'administrateur général :
            **Nathan Bruyere (nathan.bruyere@synergiaa.fr)**.
            """
        )
        
    # Configuration de la barre latérale
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Afficher :", ["Chatbot", "Documentation"])
    
    # Appeler les pages en fonction du choix
    if page == "Documentation":
        documentation_page()
