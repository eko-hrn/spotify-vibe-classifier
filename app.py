from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("kmeans_spotify.pkl")
scaler = joblib.load("scaler_spotify.pkl")

features = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo'
]

cluster_names = {
    0: "Party",
    1: "Chill",
    2: "Energetic"
}

@app.route("/")
def home():
    return "Spotify clustering API running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_df = pd.DataFrame([{
        "danceability": data["danceability"],
        "energy": data["energy"],
        "loudness": data["loudness"],
        "speechiness": data["speechiness"],
        "acousticness": data["acousticness"],
        "instrumentalness": data["instrumentalness"],
        "liveness": data["liveness"],
        "valence": data["valence"],
        "tempo": data["tempo"]
    }])

    input_scaled = scaler.transform(input_df[features])
    cluster = model.predict(input_scaled)
    cluster_id = int(cluster[0])

    return jsonify({
        "cluster_id": cluster_id,
        "segment": cluster_names[cluster_id],
        "input": data
    })

if __name__ == "__main__":
    app.run(debug=True)

#curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d @data.json