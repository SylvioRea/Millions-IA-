
import streamlit as st
import pandas as pd
from fpdf import FPDF

st.header("Historique des Combinaisons Générées")

if "history" not in st.session_state:
    st.session_state.history = []

# Afficher l'historique
if st.session_state.history:
    df_history = pd.DataFrame(st.session_state.history, columns=["Num1", "Num2", "Num3", "Num4", "Num5", "Star1", "Star2"])
    st.dataframe(df_history)

    if st.button("Exporter en Excel"):
        df_history.to_excel("historique_euromillions.xlsx", index=False)
        st.success("Export Excel effectué.")

    if st.button("Exporter en PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Historique EuroMillions - IA", ln=True, align='C')
        for i, row in df_history.iterrows():
            pdf.cell(200, 10, txt=f"Tirage {i+1}: {row.values[:5].tolist()} | Étoiles: {row.values[5:].tolist()}", ln=True)
        pdf.output("historique_euromillions.pdf")
        st.success("Export PDF effectué.")
else:
    st.info("Aucune combinaison enregistrée pour le moment.")
