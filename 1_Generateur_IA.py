
import streamlit as st
import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

st.header("Générateur de Combinaisons Optimisées avec IA")

# Génération de données simulées
df_draws = pd.DataFrame([sorted(random.sample(range(1, 51), 5)) + sorted(random.sample(range(1, 13), 2)) for _ in range(1000)],
                        columns=[f'N{i+1}' for i in range(5)] + [f'S{i+1}' for i in range(2)])

def predict_next_sum(dataframe):
    dataframe['Main_Sum'] = dataframe[[f'N{i+1}' for i in range(5)]].sum(axis=1)
    sequence_data = dataframe['Main_Sum'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(sequence_data)
    def create_sequences(data, seq_length):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            y.append(data[i+seq_length])
        return np.array(X), np.array(y)
    seq_length = 10
    X, y = create_sequences(normalized_data, seq_length)
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(seq_length, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=30, verbose=0)
    last_sequence = normalized_data[-seq_length:].reshape((1, seq_length, 1))
    predicted_sum_norm = model.predict(last_sequence, verbose=0)
    predicted_sum = scaler.inverse_transform(predicted_sum_norm)[0][0]
    return predicted_sum

predicted = predict_next_sum(df_draws)
st.success(f"Prédiction IA - Somme estimée des 5 numéros : {predicted:.2f}")

main_scores = pd.Series(range(1, 51)).sample(15).tolist()
star_scores = pd.Series(range(1, 13)).sample(6).tolist()

def generate_combinations(n):
    combos = []
    for _ in range(n):
        main = sorted(random.sample(main_scores, 5))
        stars = sorted(random.sample(star_scores, 2))
        combos.append((main, stars))
    return combos

n = st.slider("Nombre de combinaisons à générer", 1, 10, 5)
if st.button("Générer"):
    results = generate_combinations(n)
    for i, (main, stars) in enumerate(results, 1):
        st.write(f"**Combinaison {i}:** Numéros: {main} | Étoiles: {stars}")
