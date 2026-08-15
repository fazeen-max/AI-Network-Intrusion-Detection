

# 🛡️ AI Network Intrusion Detection System (NIDS)

A machine-learning-powered Network Intrusion Detection System that analyzes network-flow data and classifies traffic as **Normal** or **Attack** using a Random Forest classifier.

The project includes a professional Flask-based security dashboard for viewing traffic statistics, detections, model performance, network-flow predictions, and scan history.

---

## 🚀 Features

### 🤖 Machine Learning
- Network-flow data preprocessing
- Random Forest classification
- 84 network-flow input features
- Model evaluation and prediction analysis
- Feature-importance analysis
- **99.8% test accuracy**

### 🖥️ Security Dashboard
- Professional dark-themed security interface
- Network traffic statistics
- Threat and detection monitoring
- Model performance information
- Attack-category statistics
- System-status indicators

### 🔍 Network Flow Scanner
- Select a network-flow record from the processed dataset
- Send the complete feature set to the trained Random Forest model
- Classify traffic as:
  - `NORMAL`
  - `ATTACK`
- Display model confidence

### 📋 Scan History
- Stores recent scanner results
- Records:
  - Dataset record number
  - Classification
  - Confidence
  - Timestamp
- Displays recent scans through a dedicated History page

---

## 🧠 Machine Learning Model

The system uses a **Random Forest classifier** to classify network traffic.

The processed dataset contains **84 input features** and a `Label` target column.

| Label | Meaning |
|---|---|
| `0` | Normal traffic |
| `1` | Attack traffic |

### Model Performance

- **Algorithm:** Random Forest
- **Test Accuracy:** 99.8%
- **Test Samples:** 2,000
- **Training Samples:** 7,996

> Model performance depends on the dataset and preprocessing pipeline used for training and testing.

---

## 📊 Dashboard Pages

| Page | Purpose |
|---|---|
| **Overview** | Overall network-security summary |
| **Detections** | Detected attack statistics and model predictions |
| **Traffic** | Network-flow distribution and traffic statistics |
| **Model** | Random Forest performance and feature importance |
| **Scanner** | Test individual dataset records using the trained model |
| **History** | View recent scanner activity |

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **Joblib**
- **HTML5**
- **CSS3**
- **Random Forest**
- **JSON**

---

## 📁 Project Structure

```text
AI-Network-Intrusion-Detection/
│
├── main.py
├── README.md
├── requirements.txt
├── scan_history.json
│
├── data/
│   └── processed dataset
│
├── models/
│   └── trained Random Forest model
│
├── templates/
│   ├── dashboard.html
│   ├── detections.html
│   ├── traffic.html
│   ├── model.html
│   ├── scanner.html
│   └── history.html
│
└── static/
    └── style.css


---

⚙️ Installation

1. Clone the repository

git clone <YOUR-GITHUB-REPOSITORY-URL>

2. Enter the project directory

cd AI-Network-Intrusion-Detection

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt


---

▶️ Running the Application

Start the Flask application:

.venv\Scripts\python.exe main.py

Then open:

http://127.0.0.1:5000/


---

🔎 Using the Network Scanner

1. Open the Scanner page.


2. Enter a dataset record number.


3. Click Analyze Network Flow.


4. The system passes the record's 84 network features to the trained Random Forest model.


5. The dashboard displays the classification and confidence.


6. The scan is automatically saved to the scan history.




---

🎯 Project Goal

The goal of this project is to demonstrate how machine learning can be applied to network-security data to identify potentially malicious traffic and present the results through an accessible security-monitoring dashboard.


---

⚠️ Disclaimer

This project is intended for educational and research purposes. It demonstrates machine-learning-based classification of network-flow data and should not be considered a complete replacement for a production-grade intrusion detection or security monitoring system.


---

👩‍💻 Project Status

Status: Completed ✅

The project includes the complete machine-learning pipeline, Flask dashboard, network-flow scanner, and scan-history functionality.