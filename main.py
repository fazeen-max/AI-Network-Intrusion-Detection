from flask import Flask, render_template, request
import pandas as pd
import joblib
import json
from datetime import datetime

app = Flask(__name__)

DATA_PATH = "data/processed_nids.csv"
MODEL_PATH = "models/random_forest_nids.joblib"
@app.route("/detections")
def detections():

    df = pd.read_csv(DATA_PATH)

    normal = int((df["Label"] == 0).sum())
    threats = int((df["Label"] == 1).sum())

    threat_percentage = (threats / len(df)) * 100

    if threat_percentage >= 20:
        threat_level = "HIGH"
    elif threat_percentage >= 5:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    model = joblib.load(MODEL_PATH)

    X = df.drop("Label", axis=1)

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)

    detections_list = []

    for i in range(min(10, len(df))):

        prediction = predictions[i]
        confidence = max(probabilities[i]) * 100

        if prediction == "ATTACK":
            result = "ATTACK"
            severity = "HIGH"
        else:
            result = "NORMAL"
            severity = "LOW"

        detections_list.append({
            "result": result,
            "confidence": f"{confidence:.2f}%",
            "severity": severity
        })

    stats = {
        "normal": normal,
        "threats": threats,
        "threat_percentage": f"{threat_percentage:.1f}%",
        "threat_level": threat_level
    }

    return render_template(
        "detections.html",
        stats=stats,
        detections=detections_list
    )
@app.route("/traffic")
def traffic():

    df = pd.read_csv(DATA_PATH)

    normal = int((df["Label"] == 0).sum())
    threats = int((df["Label"] == 1).sum())

    traffic = len(df)

    threat_percentage = (threats / traffic) * 100
    normal_percentage = (normal / traffic) * 100

    if threat_percentage >= 20:
        threat_level = "HIGH"
    elif threat_percentage >= 5:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    stats = {
        "traffic": traffic,
        "normal": normal,
        "threats": threats,
        "normal_percentage": f"{normal_percentage:.1f}%",
        "threat_percentage": f"{threat_percentage:.1f}%",
        "threat_level": threat_level
    }

    return render_template(
        "traffic.html",
        stats=stats
    )
@app.route("/model")
def model():

    return render_template("model.html")
@app.route("/history")
def history():

    try:
        with open("scan_history.json", "r") as file:
            history_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_data = []

    return render_template(
        "history.html",
        history=history_data
    )
@app.route("/scanner", methods=["GET", "POST"])
def scanner():

    result = None
    confidence = None
    record_number = None

    if request.method == "POST":

        record_number = int(request.form["record_number"])

        df = pd.read_csv(DATA_PATH)

        if record_number < 1 or record_number > len(df):
            return "Invalid record number", 400

        model = joblib.load(MODEL_PATH)

        row = df.drop("Label", axis=1).iloc[[record_number - 1]]

        prediction = model.predict(row)[0]
        probabilities = model.predict_proba(row)[0]

        confidence = max(probabilities) * 100

        if prediction == 1:
            result = "ATTACK"
        else:
            result = "NORMAL"

        # Save scan to history
        try:
            with open("scan_history.json", "r") as file:
                history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            history = []

        history.insert(0, {
            "record": record_number,
            "result": result,
            "confidence": f"{confidence:.2f}%",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Keep only the latest 20 scans
        history = history[:20]

        with open("scan_history.json", "w") as file:
            json.dump(history, file, indent=4)

    return render_template(
        "scanner.html",
        result=result,
        confidence=f"{confidence:.2f}%" if confidence is not None else None,
        record_number=record_number
    )


@app.route("/")
def dashboard():

    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Dataset statistics
    traffic = len(df)
    normal = int((df["Label"] == "BENIGN").sum())
    threats = traffic - normal

    # Threat percentages
    threat_percentage = (threats / traffic) * 100
    normal_percentage = (normal / traffic) * 100

    # Dashboard threat level
    if threat_percentage >= 20:
        threat_level = "HIGH"
    elif threat_percentage >= 5:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    # Load trained Random Forest
    model = joblib.load(MODEL_PATH)

    # Prepare model input
    X = df.drop("Label", axis=1)

    # Generate predictions
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)

    # Recent predictions
    detections = []

    for i in range(min(10, len(df))):

        prediction = predictions[i]
        confidence = max(probabilities[i]) * 100

        if prediction == "ATTACK":
            result = "ATTACK"
            severity = "HIGH"
        else:
            result = "NORMAL"
            severity = "LOW"

        detections.append({
            "result": result,
            "confidence": f"{confidence:.2f}%",
            "severity": severity
        })

    # Dashboard statistics
    stats = {
        "traffic": traffic,
        "normal": normal,
        "threats": threats,
        "accuracy": "99.8%",
        "threat_percentage": f"{threat_percentage:.1f}%",
        "normal_percentage": f"{normal_percentage:.1f}%",
        "threat_level": threat_level
    }

    return render_template(
        "dashboard.html",
        stats=stats,
        detections=detections
    )


if __name__ == "__main__":

    print("=" * 55)
    print("🛡️ NIDS WEB DASHBOARD")
    print("=" * 55)
    print("🤖 Loading Random Forest model...")
    print("📊 Loading network dataset...")
    print("🌐 Starting security dashboard...")
    print("➡️ Open: http://127.0.0.1:5000")
    print("=" * 55)

    app.run(debug=True)