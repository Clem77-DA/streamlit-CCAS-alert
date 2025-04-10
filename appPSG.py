import streamlit as st
import requests
import datetime
from streamlit_autorefresh import st_autorefresh

# 🌍 URL cible
url = "https://portail-culture-et-loisirs.ccas.fr/10501-football#/lieu-parc_des_princes"

st.title("🕵️ Détecteur de mot-clé CCAS)
mot_clef = st.text_input("🔑 Mot-clé à rechercher :", value="aston")

# 🔘 Boutons de contrôle
col1, col2 = st.columns(2)
with col1:
    start = st.button("🟢 Démarrer la recherche automatique")
with col2:
    stop = st.button("🔴 Arrêter la recherche")

# 🧠 Mémoriser l'état (marche ou arrêt)
if 'running' not in st.session_state:
    st.session_state.running = False
if start:
    st.session_state.running = True
if stop:
    st.session_state.running = False

# 🕒 Heure de vérification
st.caption(f"⏱️ Heure actuelle : {datetime.datetime.now().strftime('%H:%M:%S')}")

# 🔄 Affichage du compteur de rafraîchissements
if 'count' not in st.session_state:
    st.session_state.count = 0

# 🔁 Rafraîchissement toutes les 60 sec si activé
if st.session_state.running:
    st_autorefresh(interval=60000, key="refresh")
    st.session_state.count += 1
    st.success(f"🔄 Recherche en cours... ({st.session_state.count} vérifications)")
else:
    st.warning("⏸️ Recherche automatique arrêtée")

# 🔍 Recherche du mot-clé
if mot_clef:
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
