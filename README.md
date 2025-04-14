
# 🎴 Amar Akbar Anthony — Casino Predictor (Streamlit)

Welcome to **Amar Akbar Anthony**, a live casino-style prediction game built with **Streamlit**.  
Predict which group the drawn card belongs to — Amar, Akbar, or Anthony — and track your success rates and streaks.

## 📊 Features
- 🎰 Real-time card draw simulation
- 🔮 Live prediction strategy (currently Amar-focused)
- 📈 Win distribution bar and pie charts
- 🔥 Current streak and win rate tracker
- 🏅 Player leaderboard
- 📥 Downloadable fairness audit logs

## 🎥 Demo
[Live Streamlit App](https://amar-akbar-anthony-app-h94sxtheua7vhdxkb7bfvs.streamlit.app/)

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deploy on Streamlit Cloud
1. Fork or upload this repo to your GitHub account.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Click **New app**.
4. Connect your repo `jerry61014/amar-akbar-anthony-streamlit`.
5. Set **Main file** to `app.py`.
6. Click **Deploy**.

## 📝 Game Rules
- 52-card deck split into:
  - **Amar** → A, 2, 3, 4, 5, 6 (24 cards)
  - **Akbar** → 7, 8, 9, 10 (16 cards)
  - **Anthony** → J, Q, K (12 cards)
- Deck is shuffled, split into two parts, first card discarded, second card scanned — result declared.
- Every round starts with a fresh shuffle.

---

**Built by Jerry61014 🎨**
