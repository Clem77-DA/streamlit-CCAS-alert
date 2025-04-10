import streamlit as st
import requests
import datetime
from streamlit_autorefresh import st_autorefresh

# 🌍 URL fixe
url = "https://portail-culture-et-loisirs.ccas.fr/10501-football#/lieu-parc_des_princes"

# 🔁 Auto-refresh toutes les 60 secondes
st_autorefresh(interval=60000, key="refresh")

# 🔢 Compteur de rafraîchissements
if 'count' not in st.session_state:
    st.session_state.count = 0
st.session_state.count += 1

# 🧾 Interface
st.title("🔁 Détecteur automatique de mot-clé (maj toutes les 60s)")
mot_clef = st.text_input("🔑 Mot-clé à rechercher :", value="aston")

# 🕒 Heure de la dernière vérif
st.caption(f"⏱️ Dernière vérification : {datetime.datetime.now().strftime('%H:%M:%S')}")
st.write(f"🔄 Nombre de rafraîchissements : **{st.session_state.count}**")

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
                st.warning(f"❌ Le mot-clé **{mot_clef}** n'est pas encore présent.")
        else:
            st.error(f"⚠️ Erreur HTTP : {res.status_code}")
    except Exception as e:
        st.error(f"💥 Une erreur est survenue : {e}")
