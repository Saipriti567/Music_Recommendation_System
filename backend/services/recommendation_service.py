import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ML_DIR = BASE_DIR / "ml"

songs = pickle.load(open(ML_DIR / "songs_df.pkl", "rb"))
similarity = pickle.load(open(ML_DIR / "similarity_df.pkl", "rb"))


def get_all_songs():
    """
    Returns the list of all song names.
    """
    return songs["song_name"].tolist()


def get_song_details(song_name):
    """
    Returns the details of the searched song.
    """

    song_name = song_name.strip().lower()
    songs_lower = songs["song_name"].str.lower()

    if song_name not in songs_lower.values:
        return None

    song = songs[songs_lower == song_name].iloc[0]

    return {
        "song_name": song["song_name"],
        "artist": song["artist"],
        "album": song["album"],
        "genre": song["genre"],
        "thumbnail": song["thumbnail"]
    }


def recommend_songs(song_name):
    """
    Returns top 4 recommended songs.
    """

    song_name = song_name.strip().lower()
    songs_lower = songs["song_name"].str.lower()

    if song_name not in songs_lower.values:
        return []

    index = songs[songs_lower == song_name].index[0]

    distances = similarity[index]

    song_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:5]

    recommendations = []

    for song in song_list:
        recommendations.append({
            "song_name": songs.iloc[song[0]]["song_name"],
            "artist": songs.iloc[song[0]]["artist"],
            "album": songs.iloc[song[0]]["album"],
            "genre": songs.iloc[song[0]]["genre"],
            "thumbnail": songs.iloc[song[0]]["thumbnail"]
        })

    return recommendations