import pandas as pd
import numpy as np


def load_dataset(file_path, sample_size=10000):
    print("📂 Loading dataset...")

    df = pd.read_csv(file_path)

    print(f"Original dataset shape: {df.shape}")

    if len(df) > sample_size:
        df = df.sample(
            n=sample_size,
            random_state=42
        )

    print(f"Sample shape: {df.shape}")

    return df


def clean_dataset(df):
    print("\n🧹 Cleaning dataset...")

    df.columns = df.columns.str.strip()

    # Replace infinite values with NaN
    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    # Remove missing rows
    df.dropna(inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    print(f"Cleaned dataset shape: {df.shape}")

    return df


def prepare_features(df):
    print("\n⚙️ Preparing ML features...")

    # Make a copy so the original dataframe is not changed
    data = df.copy()

    # Convert labels:
    # BENIGN = 0
    # Anything else = 1 (ATTACK)
    data["Label"] = data["Label"].apply(
        lambda x: 0 if str(x).strip().upper() == "BENIGN" else 1
    )

    # Remove columns that should not be used directly
    columns_to_remove = [
        "Src IP dec",
        "Dst IP dec",
        "Timestamp",
        "Attempted Category"
    ]

    data.drop(
        columns=columns_to_remove,
        errors="ignore",
        inplace=True
    )

    # Convert all remaining values to numeric
    data = data.apply(
        pd.to_numeric,
        errors="coerce"
    )

    # Replace any newly-created infinite values
    data.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    # Remove rows with invalid values
    data.dropna(inplace=True)

    print("✅ Features prepared.")
    print(f"Final feature shape: {data.shape}")

    print("\nClass distribution:")
    print(
        data["Label"].value_counts()
        .rename({
            0: "NORMAL",
            1: "ATTACK"
        })
    )

    return data


if __name__ == "__main__":

    print("🛡️ AI Network Intrusion Detection System")

    file_path = "data/thursday.csv"

    df = load_dataset(
        file_path,
        sample_size=10000
    )

    df = clean_dataset(df)

    processed_data = prepare_features(df)

    processed_data.to_csv(
        "data/processed_nids.csv",
        index=False
    )

    print("💾 Processed dataset saved.")

    print("\n🎉 Feature 1 preprocessing test completed!")

    print("\nFirst 5 processed rows:")
    print(processed_data.head())