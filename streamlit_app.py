
import streamlit as st
from simulator import draw_card, monte_carlo_predict

# Session state setup
if 'total_rounds' not in st.session_state:
    st.session_state.total_rounds = 0
    st.session_state.correct_predictions = 0

st.title("🎴 Amar Akbar Anthony — Casino Predictor")

if st.button("🎰 Deal Card"):
    prediction = monte_carlo_predict(10000)
    discarded, drawn, winner = draw_card()

    st.write(f"🃏 **Discarded card**: {discarded}")
    st.write(f"🃏 **Drawn card**: {drawn}")
    st.write(f"🎯 **Predicted winner**: {prediction}")
    st.write(f"🏆 **Actual winner**: {winner}")

    st.session_state.total_rounds += 1
    if prediction == winner:
        st.session_state.correct_predictions += 1

    accuracy = (st.session_state.correct_predictions / st.session_state.total_rounds) * 100
    st.write(f"✅ **Prediction Accuracy:** {accuracy:.2f}%")

st.write(f"🎲 Total Rounds Played: {st.session_state.total_rounds}")
