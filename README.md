# 🎵 AI Music Recommendation Platform

An AI-powered music recommendation web application that recommends similar Bollywood songs using Machine Learning. The project uses a FastAPI backend and a responsive frontend built with HTML, CSS and JavaScript.

---

## 🚀 Features

- 🎵 AI-based Bollywood song recommendation
- 🔍 Case-insensitive song search
- ✨ Autocomplete search suggestions
- ⌨️ Press Enter to search
- 🎶 Displays the selected song
- 🎧 Shows similar recommended songs
- ⚡ FastAPI REST API
- 💻 Responsive frontend using HTML, CSS and JavaScript

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- FastAPI
- Python

### Machine Learning
- Pandas
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```text
AI Music Recommendation System
│
├── backend/
│   ├── routers/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── Bollywood_Songs_With_Album_Genre.csv
│
├── ml/
│   ├── songs_df.pkl
│   ├── similarity_df.pkl
│   ├── tfidf_df.pkl
│   └── model.ipynb
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory

```bash
cd AI-Music-Recommendation-System
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Backend

```bash
uvicorn backend.main:app --reload
```

The backend will start at

```
http://127.0.0.1:8000
```

---

## ▶️ Run the Frontend

Open the **frontend** folder using **Live Server** in Visual Studio Code.

The frontend will open in your browser.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home |
| GET | `/recommend/songs` | Returns all songs |
| GET | `/recommend/{song_name}` | Returns similar songs |

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### Recommendation Result

(Add screenshot here)

---

## 🔮 Future Enhancements

- Playlist recommendation
- Artist-based recommendation
- Genre filtering
- User authentication
- Cloud deployment

---

## 👩‍💻 Author

**Purabi Baghasingh**

Electrical & Electronics Engineering

Silicon University