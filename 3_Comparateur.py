
import streamlit as st

st.header("Comparateur de Résultats")

if "history" not in st.session_state or not st.session_state.history:
    st.info("Aucune grille enregistrée pour comparaison.")
else:
    st.subheader("Entrez les résultats officiels")
    official_nums = st.multiselect("Numéros gagnants (5)", list(range(1, 51)), max_selections=5)
    official_stars = st.multiselect("Étoiles gagnantes (2)", list(range(1, 13)), max_selections=2)

    if len(official_nums) == 5 and len(official_stars) == 2:
        for i, combo in enumerate(st.session_state.history, 1):
            matched_nums = len(set(combo[:5]) & set(official_nums))
            matched_stars = len(set(combo[5:]) & set(official_stars))
            st.write(f"Tirage {i}: {combo[:5]} | Étoiles: {combo[5:]} => {matched_nums} numéros & {matched_stars} étoiles")
