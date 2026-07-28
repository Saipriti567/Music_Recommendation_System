const API_URL = "";

const songInput = document.getElementById("songInput");
const recommendBtn = document.getElementById("recommendBtn");
const resultDiv = document.getElementById("result");
const suggestionsDiv = document.getElementById("suggestions");

let songs = [];

// Load all songs
async function loadSongs() {
    try {
        const response = await fetch(`${API_URL}/recommend/songs`);

        if (!response.ok) {
            throw new Error("Failed to load songs");
        }

        const data = await response.json();
        songs = data.songs;

        console.log("Songs Loaded");
        console.log(songs);

    } catch (error) {
        console.error("Error loading songs:", error);
    }
}

// Recommend Button
recommendBtn.addEventListener("click", async () => {

    const selectedSong = songInput.value.trim();

    if (selectedSong === "") {
        alert("Please enter a song name.");
        return;
    }

    resultDiv.innerHTML = "<p>Loading recommendations...</p>";

    try {

        const response = await fetch(
            `${API_URL}/recommend/${encodeURIComponent(selectedSong)}`
        );

        if (!response.ok) {
            throw new Error("Failed to fetch recommendations");
        }

        const data = await response.json();

        if (data.message) {
            resultDiv.innerHTML = `<h3>${data.message}</h3>`;
            return;
        }

        displayResults(data.selected_song, data.recommendations);

    } catch (error) {

        console.error(error);

        resultDiv.innerHTML =
            "<p>Something went wrong.</p>";
    }

});

// ======================
// Autocomplete
// ======================

function showSuggestions(value) {

    suggestionsDiv.innerHTML = "";

    if (value.length === 0) {
        suggestionsDiv.style.display = "none";
        return;
    }

    const filteredSongs = songs.filter(song =>
        song.toLowerCase().includes(value.toLowerCase())
    ).slice(0, 6);

    if (filteredSongs.length === 0) {
        suggestionsDiv.style.display = "none";
        return;
    }

    filteredSongs.forEach(song => {

        const item = document.createElement("div");

        item.className = "suggestion-item";

        item.textContent = song;

        item.addEventListener("click", () => {

            songInput.value = song;

            suggestionsDiv.innerHTML = "";
            suggestionsDiv.style.display = "none";

            // Automatically search after selecting
            recommendBtn.click();

        });

        suggestionsDiv.appendChild(item);

    });

    suggestionsDiv.style.display = "block";

}

// ======================
// Display Results
// ======================

function displayResults(selectedSong, recommendations) {

    resultDiv.innerHTML = "";

    // Selected Song
    const selectedDiv = document.createElement("div");

    selectedDiv.className = "selected-song";

    selectedDiv.innerHTML = `
        <h2>🎵 Selected Song</h2>

        <div class="song-card">
            <img src="${selectedSong.thumbnail}" alt="${selectedSong.song_name}">
            <h3>${selectedSong.song_name}</h3>
            <p><strong>Artist:</strong> ${selectedSong.artist}</p>
            <p><strong>Album:</strong> ${selectedSong.album}</p>
            <p><strong>Genre:</strong> ${selectedSong.genre}</p>
        </div>
    `;

    resultDiv.appendChild(selectedDiv);

    // Recommendation Title
    const title = document.createElement("h2");

    title.className = "recommendation-title";
    title.innerHTML = "🎶 Recommended Songs";

    resultDiv.appendChild(title);

    // Recommendation Grid
    const grid = document.createElement("div");

    grid.className = "recommendation-grid";

    recommendations.forEach(song => {

        const card = document.createElement("div");

        card.className = "song-card";

        card.innerHTML = `
            <img src="${song.thumbnail}" alt="${song.song_name}">
            <h3>${song.song_name}</h3>
            <p><strong>Artist:</strong> ${song.artist}</p>
            <p><strong>Album:</strong> ${song.album}</p>
            <p><strong>Genre:</strong> ${song.genre}</p>
        `;

        grid.appendChild(card);

    });

    resultDiv.appendChild(grid);

}

// ======================
// Initial Load
// ======================

loadSongs();

// Show suggestions while typing
songInput.addEventListener("input", () => {
    showSuggestions(songInput.value);
});

// Hide suggestions when clicking outside
document.addEventListener("click", (e) => {

    if (
        !songInput.contains(e.target) &&
        !suggestionsDiv.contains(e.target)
    ) {
        suggestionsDiv.style.display = "none";
    }

});

// Press Enter to Search
songInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter") {

        event.preventDefault();

        recommendBtn.click();

    }

});