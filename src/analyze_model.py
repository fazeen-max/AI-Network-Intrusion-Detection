import pandas as pd
import joblib

from sklearn.metrics import classification_report


DATA_PATH = "data/processed_nids.csv"
MODEL_PATH = "models/random_forest_nids.joblib"


def load_model():

    print("🤖 Loading trained model...")

    model = joblib.load(MODEL_PATH)

    print("✅ Model loaded successfully.")

    return model


def load_data():

    print("\n📂 Loading processed data...")

    df = pd.read_csv(DATA_PATH)

    print(f"Dataset shape: {df.shape}")

    return df


def test_predictions(model, df):

    print("\n🔍 Testing model predictions...")

    X = df.drop("Label", axis=1)
    y = df["Label"]

    predictions = model.predict(X)

    probabilities = model.predict_proba(X)

    print("\nFirst 10 predictions:")

    for i in range(10):

        prediction = predictions[i]

        confidence = max(probabilities[i]) * 100

        if prediction == 0:
            result = "🟢 NORMAL"
        else:
            result = "🔴 ATTACK"

        print(
            f"Record {i + 1}: "
            f"{result} | "
            f"Confidence: {confidence:.2f}%"
        )

    print("\n📊 Prediction performance:")

    print(
        classification_report(
            y,
            predictions,
            target_names=[
                "NORMAL",
                "ATTACK"
            ]
        )
    )


def show_feature_importance(model, df):

    print("\n🔎 Top 10 important network features:")

    X = df.drop("Label", axis=1)

    importance = pd.Series(
        model.feature_importances_,
        index=X.columns
    )

    importance = importance.sort_values(
        ascending=False
    )

    for feature, score in importance.head(10).items():

        print(
            f"{feature}: {score:.4f}"
        )


if __name__ == "__main__":

    print("=" * 55)
    print("🛡️ AI NETWORK INTRUSION DETECTION SYSTEM")
    print("🔎 Feature 3 - Model Analysis & Prediction Testing")
    print("=" * 55)

    model = load_model()

    data = load_data()

    test_predictions(
        model,
        data
    )

    show_feature_importance(
        model,
        data
    )

    print("\n🎉 Feature 3 analysis completed!")