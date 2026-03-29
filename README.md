# 🎧 Spotify Vibe Classifier

A machine learning project to **classify songs based on vibes**, not genres.

Instead of just labeling songs as "pop", "rock", etc., this project focuses on the **feeling of the music**:

* Energetic
* Party
* Chill

---

## 🚀 Overview

This project uses **Spotify audio features** to group songs into clusters using **KMeans Clustering**.

The final output is a **vibe/segment classification** for each song.

---

## 🧠 How It Works

1. Extract audio features from Spotify
2. Normalize the data using a scaler
3. Feed the data into a KMeans model
4. The model assigns the song to a cluster
5. The cluster is mapped into a **vibe label**

### Cluster Mapping

| Cluster ID | Vibe      |
| ---------- | --------- |
| 0          | Party     |
| 1          | Chill     |
| 2          | Energetic |

---

## 🎼 Features Used

The model uses the following Spotify audio features:

* danceability
* energy
* loudness
* speechiness
* acousticness
* instrumentalness
* liveness
* valence
* tempo

---

## ⚡ API Usage

### 🔹 Base URL

```
http://127.0.0.1:5000
```

---

### 🔹 GET `/`

Health check endpoint

**Response**

```json
"Spotify clustering API running"
```

---

### 🔹 POST `/predict`

Predict the vibe of a song based on its audio features

**Request**

```json
{
  "danceability": 0.30,
  "energy": 0.09,
  "loudness": -21.3,
  "speechiness": 0.03,
  "acousticness": 0.97,
  "instrumentalness": 0.88,
  "liveness": 0.12,
  "valence": 0.10,
  "tempo": 99
}
```

**Response**

```json
{
  "cluster_id": 1,
  "segment": "Chill",
  "input": {
    "danceability": 0.30,
    "energy": 0.09,
    "loudness": -21.3,
    "speechiness": 0.03,
    "acousticness": 0.97,
    "instrumentalness": 0.88,
    "liveness": 0.12,
    "valence": 0.10,
    "tempo": 99
  }
}
```

---

## 🛠️ Installation

Install dependencies:

```bash
pip install flask pandas scikit-learn joblib
```

---

## ▶️ Run Locally

```bash
python app.py
```

The server will run at:

```
http://127.0.0.1:5000
```

---

## 🧪 Example Test

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d @data.json
```

---

## 📊 Dataset Notes

The dataset is built from:

* 🎧 Songs that are liked
* 🚫 Songs that are disliked
* 📈 Spotify audio features

This means the model is not a traditional genre classifier, but rather:

> **"What vibe does this song give?"**

---

## 🤔 Why This Project?

Sometimes we don’t look for music by genre, but by mood:

* “I want something chill”
* “I need party vibes”
* “I need energy”

This project aims to answer that using a data-driven approach.

---

## 🔮 Future Improvements

* 🎯 Better cluster labeling (auto-labeling)
* 📊 Cluster visualization (PCA / t-SNE)
* 🎵 Input using Spotify track ID
* 📦 Batch prediction
* ☁️ Cloud deployment (Render / Railway / AWS)

---

## 🧰 Tech Stack

* Python
* Flask
* Pandas
* Scikit-learn
* Joblib

---

## 👀 Notes

This project is still experimental, so:

* results may vary depending on the dataset
* vibe classification is subjective, not absolute 

---

**Made with vibes 🎶**
