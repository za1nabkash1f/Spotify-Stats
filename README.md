# 🎧 Spotify Streaming Dashboard

This interactive dashboard visualizes your personal Spotify streaming data, helping you explore trends in music and podcast listening over time.

Built with [Streamlit](https://streamlit.io/), the app lets you view insights like top artists, most played tracks, listening patterns by hour or month, and time spent on music vs. podcasts.

---

## 📊 Features

- **Top Artists & Tracks**: See your 20 most streamed artists and songs.
- **Podcasts Overview**: Discover which podcasts you’ve listened to most.
- **Music vs Podcast Time**: Compare hours spent on music vs podcasts.
- **Listening Patterns**:
  - By **hour of the day**
  - By **month of the year**

---

## 🚀 Getting Started

### 1. Clone the Repository

<pre> 
git clone https://github.com/yourusername/spotify-dashboard.git
cd spotify-dashboard
</pre>

### 2. Create a Virtual Environment (Recommended)

<pre> 
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
</pre>

### 3. Install Requirements

<pre> 
pip install -r requirements.txt
</pre>
 
### 4. Add you spotify data

Download your Spotify Streaming History data (from Spotify's Privacy page).

Place the following JSON files in the project directory:

<pre> 
StreamingHistory_music_0.json

StreamingHistory_music_1.json

StreamingHistory_podcast_0.json
</pre>

🛑 Important: Do NOT upload your actual data to GitHub. Add these files to .gitignore to keep them private.

### 5. Make theme changes

Create a new folder .streamlit in you root file

Save config.toml file in .streamlit file

You should now get a new theme 
### 6. Run the App
<pre>
streamlit run filename.py
</pre>
🛡️ Privacy Note
This project uses your personal Spotify streaming data locally only. Ensure you do not commit any personal data files when sharing this project publicly.

---

📌 Credits

This dashboard was built with ❤️ using:

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- Data from personal Spotify Streaming History export

---

📄 License

This project is licensed under the MIT License.
