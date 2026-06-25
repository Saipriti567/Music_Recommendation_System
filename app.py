from difflib import get_close_matches
import re
import yt_dlp
import streamlit as st
import pickle

st.title("Bollywood Music Recommendation System")

# ── Load pickle files ──────────────────────────────────────────
try:
    df = pickle.load(open("songs_df.pkl", "rb"))
    similarity = pickle.load(open("similarity_df.pkl", "rb"))
except Exception as e:
    st.error(e)
    st.stop()

# ── Session state init ─────────────────────────────────────────
for key in ["results", "matched_song", "idx", "main_audio", "rec_audios"]:
    if key not in st.session_state:
        st.session_state[key] = None

# ── Helper functions ───────────────────────────────────────────
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def recommend(song):
    try:
        index = df[df['song_name'] == song].index[0]
    except:
        return []
    distance = similarity[index]
    songs_list = sorted(list(enumerate(distance)),
                        reverse=True, key=lambda x: x[1])[1:6]
    rec = []
    for i, score in songs_list:
        rec.append({
            "song": df.iloc[i]["song_name"],
            "artist": df.iloc[i]["artist"],
            "thumbnail": df.iloc[i]["thumbnail"] if "thumbnail" in df.columns else None
        })
    return rec

def get_youtube_url_from_thumbnail(thumbnail_url):
    try:
        video_id = thumbnail_url.split("/vi/")[1].split("/")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    except:
        return None

def get_audio_url(youtube_url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            return info['url']
    except:
        return None

def run_search(user_input):
    """Runs search and saves everything to session state"""
    if not user_input.strip():
        return

    user_clean = clean_text(user_input)

    partial_matches = df[
        df['song_name_clean'].str.contains(user_clean, na=False) |
        df['lyrics_clean'].str.contains(user_clean, na=False)
    ]

    if not partial_matches.empty:
        matched_song = partial_matches.iloc[0]["song_name"]
    else:
        matches = get_close_matches(user_input, df["song_name"].tolist(), n=1, cutoff=0.3)
        if not matches:
            st.error("Song not Found. Try typing more letters.")
            return
        matched_song = matches[0]

    idx = df[df["song_name"] == matched_song].index[0]
    results = recommend(matched_song)

    # ── Preload ALL audio URLs at search time ──────────────────
    with st.spinner("Loading songs... please wait"):
        main_yt = get_youtube_url_from_thumbnail(df.iloc[idx]["thumbnail"])
        main_audio = get_audio_url(main_yt)

        rec_audios = []
        for item in results:
            yt = get_youtube_url_from_thumbnail(item["thumbnail"])
            audio = get_audio_url(yt)
            rec_audios.append(audio)

    # ── Save everything to session state ──────────────────────
    st.session_state.matched_song = matched_song
    st.session_state.idx = idx
    st.session_state.results = results
    st.session_state.main_audio = main_audio
    st.session_state.rec_audios = rec_audios

# ── Search UI ──────────────────────────────────────────────────
# This is the KEY fix — on_change triggers when user presses Enter
user_input = st.text_input(
    "Enter a song name or lyrics:",
    key="search_input",
    on_change=lambda: run_search(st.session_state.search_input)  # ✅ Enter key fix
)

# Also keep a click button as backup
if st.button("🔍 Recommend"):
    run_search(user_input)

# ── Display results from session state ────────────────────────
# Results stay visible even when play button is clicked ✅
if st.session_state.matched_song:
    matched_song = st.session_state.matched_song
    idx = st.session_state.idx
    result = st.session_state.results
    main_audio = st.session_state.main_audio
    rec_audios = st.session_state.rec_audios

    st.info(f"Showing results for: **{matched_song}**")

    # ── Searched song ──────────────────────────────────────────
    st.subheader("You Searched for:")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(df.iloc[idx]["thumbnail"], width=120)
    with col2:
        st.write("**Song:**", df.iloc[idx]["song_name"])
        st.write("**Artist:**", df.iloc[idx]["artist"])
        # ✅ Audio already loaded — no reload needed
        if main_audio:
            st.audio(main_audio, format="audio/mp4")
        else:
            st.warning("Audio unavailable.")

    # ── Recommended songs ──────────────────────────────────────
    st.subheader("Recommended Songs")
    for i, item in enumerate(result):
        col1, col2 = st.columns([1, 3])
        with col1:
            if item["thumbnail"]:
                st.image(item["thumbnail"], width=120)
        with col2:
            st.write("**" + item["song"] + "**")
            st.write(item["artist"])
            # ✅ Audio already loaded — no reload needed
            if rec_audios[i]:
                st.audio(rec_audios[i], format="audio/mp4")
            else:
                st.warning("Audio unavailable.")