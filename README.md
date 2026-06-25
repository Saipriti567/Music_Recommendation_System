# 🎵 Music Recommendation System

A Machine Learning-based Music Recommendation System built using Python and Streamlit that recommends Bollywood songs based on similarity and user preferences.

## 📌 Overview

This project uses content-based filtering techniques to recommend songs similar to the user's selected song. The recommendation engine analyzes song metadata and similarity scores to provide relevant music suggestions.

The application is built with Streamlit, providing an interactive and user-friendly interface.

---

## 🚀 Features

- Search songs by name
- Get similar song recommendations
- Interactive Streamlit web interface
- Fast recommendation generation
- Content-based filtering approach
- Uses precomputed similarity matrices for efficient predictions

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Pickle

---

## 📂 Project Structure

```text
Music_Recommendation_System/
│
├── app.py
├── model.ipynb
├── Bollywood_Songs_With_Album_Genre.csv
├── songs_df.pkl
├── similarity_df.pkl
├── tfidf_df.pkl
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset contains Bollywood songs along with metadata such as:

- Song Name
- Album Name
- Genre

The recommendation engine uses this information to calculate song similarity and generate recommendations.

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Music_Recommendation_System.git
cd Music_Recommendation_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running the command, open the local URL displayed in the terminal.

---

## 🧠 Machine Learning Approach

1. Data Preprocessing
2. Text Cleaning
3. TF-IDF Vectorization
4. Similarity Matrix Generation
5. Content-Based Recommendation

The system identifies songs that are most similar to the selected song and displays personalized recommendations.

---

## 📈 Future Improvements

- Spotify API Integration
- Artist-Based Recommendations
- Mood-Based Recommendations
- Album Recommendations
- Personalized User Profiles
- Music Preview Support

---


## ⭐ If you found this project useful, consider giving it a star!