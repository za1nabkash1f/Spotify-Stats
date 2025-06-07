import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json  # For working with JSON files
import streamlit as st  # For building interactive dashboards

# === Sidebar Controls ===
st.sidebar.title("Spotify Streaming Dashboard")
view_option = st.sidebar.selectbox("Choose a view:", [
    "Top Artists", "Top Tracks", "Music vs Podcast Time",
    "Top Podcasts", "Listening by Hour", "Listening by Month"
])

# === Load data from JSON files ===
@st.cache_data  # Cache the function to improve performance
def load_data():
    with open("StreamingHistory_music_0.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open("StreamingHistory_music_1.json", "r", encoding="utf-8") as f2:
        data2 = json.load(f2)
    with open("StreamingHistory_podcast_0.json", "r", encoding="utf-8") as f3:
        data3 = json.load(f3)
    return data, data2, data3

# Load and prepare DataFrames
data, data2, data3 = load_data()
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
podcast_df = pd.DataFrame(data3)
songs_df = pd.concat([df1, df2], ignore_index=True)

# Convert endTime to datetime for time-based analysis
songs_df['endTime'] = pd.to_datetime(songs_df['endTime'])

# === View 1: Top 20 Artists by Number of Songs Streamed ===
if view_option == "Top Artists":
    st.subheader("Top 20 Artists by Songs Streamed")
    artist_counts = songs_df['artistName'].value_counts().reset_index()
    artist_counts.columns = ['artistName', 'playCount']
    artist_counts = artist_counts.sort_values(by='playCount', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='artistName', y='playCount', hue='artistName', data=artist_counts.head(20), palette='Set2', legend=False)
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 20 Artists by Number of Songs Streamed")
    st.pyplot(fig)

# === View 2: Top 20 Tracks by Number of Streams ===
elif view_option == "Top Tracks":
    st.subheader("Top 20 Tracks by Streams")
    track_counts = songs_df['trackName'].value_counts().reset_index()
    track_counts.columns = ['trackName', 'playCount']
    track_counts = track_counts.sort_values(by='playCount', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='trackName', y='playCount', hue='trackName', data=track_counts.head(20), palette='Set3', legend=False)
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 20 Tracks by Number of Streams")
    st.pyplot(fig)

# === View 3: Total Time Spent Streaming Music vs Podcasts ===
elif view_option == "Music vs Podcast Time":
    st.subheader("Time Spent Listening")
    music_seconds = songs_df['msPlayed'].sum() / 1000
    music_hours = music_seconds / 3600
    podcast_seconds = podcast_df['msPlayed'].sum() / 1000
    podcast_hours = podcast_seconds / 3600
    total_seconds = music_seconds + podcast_seconds
    total_hours = total_seconds / 3600

    st.metric("Music", f"{round(music_hours, 2)} hours")
    st.metric("Podcasts", f"{round(podcast_hours, 2)} hours")
    st.metric("Total", f"{round(total_hours, 2)} hours")

# === View 4: Top Podcasts by Time Listened ===
elif view_option == "Top Podcasts":
    st.subheader("Top 5 Podcasts by Time Streamed (minutes)")
    podcast_counts = podcast_df.groupby("podcastName")['msPlayed'].sum().reset_index()
    podcast_counts = podcast_counts.sort_values(by='msPlayed', ascending=False)
    podcast_counts['minutesPlayed'] = podcast_counts['msPlayed'] / (1000 * 60)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='podcastName', y='minutesPlayed', hue='podcastName', data=podcast_counts.head(5), palette='muted', legend=False)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Minutes Played")
    plt.title("Top 5 Podcasts by Time Streamed")
    st.pyplot(fig)

# === View 5: Listening Time by Hour of Day ===
elif view_option == "Listening by Hour":
    st.subheader("Listening Time by Hour of Day")
    songs_df['hour'] = songs_df['endTime'].dt.hour
    hourly_counts = songs_df.groupby('hour')['msPlayed'].sum() / (1000 * 60)  # in minutes
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o')
    plt.title("Listening Time by Hour of Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Minutes Played")
    plt.xticks(range(0, 24))
    st.pyplot(fig)

# === View 6: Listening Time by Month ===
elif view_option == "Listening by Month":
    st.subheader("Listening Time by Month")
    songs_df['month'] = songs_df['endTime'].dt.month_name()
    monthly_minutes = songs_df.groupby('month')['msPlayed'].sum() / (1000 * 60)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    monthly_minutes = monthly_minutes.reindex(month_order)
    monthly_df = pd.DataFrame({
        "month": monthly_minutes.index,
        "minutesPlayed": monthly_minutes.values
    })
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='month', y='minutesPlayed', hue='month', data=monthly_df, palette='coolwarm', legend=False)
    plt.title("Total Listening Time by Month")
    plt.xlabel("Month")
    plt.ylabel("Minutes Played")
    plt.xticks(rotation=45)
    st.pyplot(fig)
