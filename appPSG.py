import streamlit as st
import requests
import datetime
from streamlit_autorefresh import st_autorefresh

# 🧠 Initialisation des états
if 'running' not in st.session_state:
    st.session_state.running = False
if 'count' not in st.session_state:
    st.session_state.count = 0

# 🧾 Titre de l'application
st.title("🕵️ Détecteur de mot-clé CCAS")

# 🌍 Entrée dynamique de l'URL
url = st.text_input("🌐 URL de la page à surveiller :", value="https://portail-culture-et-loisirs.ccas.fr/10501-football#/lieu-parc_des_princes")

# 🔑 Mot-clé à rechercher
mot_clef = st.text_input("🔑 Mot-clé à rechercher :", value="aston")

# 🔘 Boutons de contrôle
col1, col2 = st.columns(2)
with col1:
    if st.button("🟢 Démarrer la recherche automatique"):
        st.session_state.running = True
with col2:
    if st.button("🔴 Arrêter la recherche"):
        st.session_state.running = False

# 🕒 Afficher l'heure actuelle
st.caption(f"⏱️ Heure actuelle : {datetime.datetime.now().strftime('%H:%M:%S')}")

# 🔁 Si la recherche automatique est activée
if st.session_state.running:
    st_autorefresh(interval=60000, key="refresh")
    st.session_state.count += 1
    st.success(f"🔄 Recherche automatique en cours... ({st.session_state.count} vérifications)")
else:
    st.warning("⏸️ Recherche automatique arrêtée")

# 🔍 Recherche du mot-clé dans la page
if mot_clef and url:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            if mot_clef.lower() in res.text.lower():
                st.success(f"✅ Le mot-clé **{mot_clef}** a été trouvé sur la page !")
            else:
                st.error(f"❌ Le mot-clé **{mot_clef}** n'est pas présent.")
        else:
            st.error(f"⚠️ Erreur HTTP : {res.status_code}")
    except Exception as e:
        st.error(f"💥 Erreur de connexion : {e}")
