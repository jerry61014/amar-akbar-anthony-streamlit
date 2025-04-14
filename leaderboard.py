
import pandas as pd
import matplotlib.pyplot as plt

def get_current_streak(log_df, prediction):
    streak = 0
    for result in reversed(log_df['win']):
        if result == "Yes":
            streak += 1
        else:
            break
    return streak

def get_leaderboard(log_df):
    leaderboard = log_df.groupby('player')['win'].apply(lambda x: (x == "Yes").sum()).reset_index()
    leaderboard.columns = ['Player', 'Wins']
    leaderboard = leaderboard.sort_values(by='Wins', ascending=False).reset_index(drop=True)
    return leaderboard

def plot_pie_chart(log_df):
    result_counts = log_df['result'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    return fig
