
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Statistiques des Numéros")

if "history" not in st.session_state or not st.session_state.history:
    st.info("Pas encore de données pour analyser.")
else:
    df_stats = pd.DataFrame(st.session_state.history, columns=["Num1", "Num2", "Num3", "Num4", "Num5", "Star1", "Star2"])
    
    main_numbers = pd.concat([df_stats[col] for col in ["Num1", "Num2", "Num3", "Num4", "Num5"]])
    star_numbers = pd.concat([df_stats["Star1"], df_stats["Star2"]])
    
    st.subheader("Fréquence des numéros principaux")
    fig1, ax1 = plt.subplots()
    main_numbers.value_counts().sort_index().plot(kind="bar", ax=ax1)
    st.pyplot(fig1)

    st.subheader("Fréquence des étoiles")
    fig2, ax2 = plt.subplots()
    star_numbers.value_counts().sort_index().plot(kind="bar", ax=ax2, color="orange")
    st.pyplot(fig2)
