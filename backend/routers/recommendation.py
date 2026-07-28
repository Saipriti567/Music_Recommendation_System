from fastapi import APIRouter

from backend.services.recommendation_service import (
    get_all_songs,
    get_song_details,
    recommend_songs
)

router = APIRouter(
    prefix="/recommend",
    tags=["Recommendation"]
)


@router.get("/songs")
def get_songs():
    return {
        "songs": get_all_songs()
    }


@router.get("/{song_name}")
def recommend(song_name: str):

    selected_song = get_song_details(song_name)
    recommendations = recommend_songs(song_name)

    if not selected_song:
        return {
            "message": "Song not found."
        }

    return {
        "selected_song": selected_song,
        "recommendations": recommendations
    }