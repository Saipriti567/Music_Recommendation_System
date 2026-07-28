from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import recommendation

app = FastAPI(
    title="AI Music Recommendation Platform",
    description="A Full Stack AI Music Recommendation System",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include Recommendation Router
app.include_router(recommendation.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Music Recommendation Platform 🚀"
    }