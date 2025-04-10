import streamlit as st
import requests

# 🌍 URL cible (fixe)
url = "https://portail-culture-et-loisirs.ccas.fr/10501-football#/lieu-parc_des_princes"

# Titre de l'application
st.title("🔍 Détecteur de mot-clé")

# Champ pour entrer le mot-clé
mot_clef = st.text_input("Entre le mot-clé à rechercher 👇")

# Quand tu cliques sur le bouton
if st.button("🔎 Vérifier la page") and mot_clef:

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            html_content = res.text
            if mot_clef.lower() in html_content.lower():
                st.success(f"✅ Le mot-clé **{mot_clef}** a été trouvé sur la page !")
            else:
                st.warning(f"❌ Le mot-clé **{mot_clef}** n'est pas présent.")
        else:
            st.error(f"⚠️ Erreur HTTP : {res.status_code}")
    except Exception as e:
        st.error(f"💥 Erreur de connexion : {e}")
