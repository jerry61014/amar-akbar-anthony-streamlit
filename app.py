
import streamlit as st
import pandas as pd
import simulator
import leaderboard
from datetime import datetime
import os

st.set_page_config(page_title="Amar Akbar Anthony V2", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: gold;'>🎰 Amar Akbar Anthony — Casino Predictor 🎴</h1>",
    unsafe_allow_html=True
)

# Player section
player = st.text_input("🎲 Enter your name:", value="Player")

# Load or create fairness log
if os.path.exists("fairness_log.csv"):
    log_df = pd.read_csv("fairness_log.csv")
else:
    log_df = pd.DataFrame(columns=["timestamp", "player", "discarded", "scanned", "result", "prediction", "win"])

# Predict Amar every time
prediction = "Amar"
st.markdown(f"### 🔮 Prediction for Next Round: **{prediction}**")

# Run simulation
if st.button("🎲 Run Next Round"):
    log_entry = simulator.simulate_round()
    if log_entry:
        log_entry['player'] = player
        log_entry['prediction'] = prediction
        log_entry['win'] = "Yes" if log_entry['result'] == prediction else "No"
        log_df = pd.concat([log_df, pd.DataFrame([log_entry])], ignore_index=True)
        log_df.to_csv("fairness_log.csv", index=False)

# Stats
total = len(log_df)
wins = (log_df['win'] == "Yes").sum()
streak = leaderboard.get_current_streak(log_df, prediction)
success_rate = (wins / total * 100) if total > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("✅ Total Rounds", total)
col2.metric("🏆 Total Wins", wins)
col3.metric("🔥 Current Streak", streak)

# Charts
st.markdown("### 📊 Win Distribution")
if total > 0:
    st.bar_chart(log_df['result'].value_counts())

    st.markdown("### 🥧 Win Percentage")
    st.pyplot(leaderboard.plot_pie_chart(log_df))

# Last 5 rounds
st.markdown("### 📋 Last 5 Rounds")
st.dataframe(log_df.tail(5).sort_index(ascending=False))

# Leaderboard
st.markdown("### 🏅 Leaderboard")
st.dataframe(leaderboard.get_leaderboard(log_df))

# Download logs
st.download_button("📥 Download Fairness Log (CSV)", data=log_df.to_csv(index=False), file_name="fairness_log.csv")
