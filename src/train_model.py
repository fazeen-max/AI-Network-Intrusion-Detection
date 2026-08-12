import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)


DATA_PATH = "data/processed_nids.csv"
MODEL_PATH = "models/random_forest_nids.joblib"


def load_processed_data():

    print("📂 Loading processed dataset...")

    df = pd.read_csv(DATA_PATH)

    print(f"Dataset shape: {df.shape}")

    return df


def train_model(df):

    print("\n🤖 Preparing training data...")

    X = df.drop("Label", axis=1)
    y = df["Label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    print("\n🌲 Training Random Forest model...")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)

    print("✅ Model training completed!")

    # Save trained model
    joblib.dump(
        model,
        MODEL_PATH
    )

    print(f"💾 Model saved to {MODEL_PATH}")

    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):

    print("\n📊 Evaluating model...")

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"\nAccuracy: {accuracy:.4f}")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=[
                "NORMAL",
                "ATTACK"
            ]
        )
    )

    print("Confusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )


if __name__ == "__main__":

    print("=" * 50)
    print("🛡️ AI NETWORK INTRUSION DETECTION SYSTEM")
    print("🤖 Feature 2 - Random Forest Model")
    print("=" * 50)

    dataset = load_processed_data()

    model, X_test, y_test = train_model(
        dataset
    )

    evaluate_model(
        model,
        X_test,
        y_test
    )

    print("\n🎉 Feature 2 model test completed!")