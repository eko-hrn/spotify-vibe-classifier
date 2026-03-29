#  Spotify Vibe Classifier

Machine learning project buat **ngelompokin lagu berdasarkan vibes**, bukan genre.

Daripada cuma "pop", "rock", dll — project ini fokus ke **feeling dari lagunya**:

* Energetic
* Party
* Chill

---

## 🚀 Overview

Project ini menggunakan **audio features dari Spotify** untuk mengelompokkan lagu ke dalam beberapa cluster menggunakan **KMeans Clustering**.

Output akhirnya berupa **segment/vibe** dari lagu tersebut.

---

## 🧠 How It Works

1. Ambil audio features lagu dari Spotify
2. Normalize data pakai scaler
3. Masukin ke model KMeans
4. Model assign ke cluster tertentu
5. Cluster dikonversi jadi **vibe label**

Mapping cluster:

| Cluster ID | Vibe      |
| ---------- | --------- |
| 0          | Party     |
| 1          | Chill     |
| 2          | Energetic |

---

## 🎼 Features Used

Model pakai fitur audio dari Spotify:

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

Predict vibe dari lagu berdasarkan audio features

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

Server akan jalan di:

```
http://127.0.0.1:5000
```

## 🧪 Example Test

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d @data.json
```

---

## 📊 Dataset Notes

Dataset dibuat dari:

* 🎧 Playlist lagu yang disukai
* 🚫 Playlist lagu yang tidak disukai
* 📈 Audio features dari Spotify API

Jadi model ini bukan genre classifier biasa, tapi lebih ke:

> **"Ini lagu vibes-nya kayak gimana?"**

---

## 🤔 Why This Project?

Kadang kita nyari lagu bukan berdasarkan genre, tapi:

* "lagi pengen chill"
* "lagi pengen party"
* "lagi butuh energy"

Project ini bantu ngejawab itu dengan pendekatan data.

---

## 🔮 Future Improvements

* 🎯 Label cluster lebih akurat (auto-labeling)
* 📊 Visualisasi cluster (PCA / t-SNE)
* 🎵 Input langsung dari Spotify track ID
* 📦 Batch prediction
* ☁️ Deploy ke cloud (Render / Railway / AWS)

---

## 🧰 Tech Stack

* Python
* Flask
* Pandas
* Scikit-learn
* Joblib

---


## 👀 Notes

Project ini masih eksploratif, jadi:

* hasil cluster bisa berubah tergantung dataset
* vibe = interpretasi, bukan kebenaran absolut 😄

---

**Made with vibes 🎶**
