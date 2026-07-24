# 🌱 Smart Crop Recommendation System using Machine Learning

A Machine Learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The system helps users make informed agricultural decisions by analyzing soil and weather parameters using the **Random Forest Classifier**.

---

## 📖 Project Overview

Selecting the right crop is an important factor in improving agricultural productivity. This project uses Machine Learning to predict the most suitable crop based on essential soil nutrients and climatic conditions.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, providing an interactive interface for real-time crop recommendation.

---

## 🚀 Features

- 🌱 Crop recommendation based on soil and weather conditions
- 🤖 Machine Learning-based prediction
- 🌾 Random Forest Classifier
- 📊 Prediction confidence score
- 📋 Crop information display
- 💻 Interactive Streamlit web application
- ⚡ Real-time prediction

---

## 📂 Dataset

**Source:** Kaggle

**Dataset Name:** Crop Recommendation Dataset

### Dataset Information

- Total Records: **2200**
- Input Features: **7**
- Target Classes: **22 Crops**

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

### Target

- Recommended Crop

---

## 🛠 Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

### Final Selected Model

**Random Forest Classifier**

The Random Forest model achieved the highest prediction accuracy and was selected for deployment.

---

## 📊 Machine Learning Workflow

```
Crop Recommendation Dataset
            │
            ▼
     Data Preprocessing
            │
            ▼
 Exploratory Data Analysis
            │
            ▼
   Train-Test Split
            │
            ▼
 Machine Learning Models
            │
            ▼
 Model Evaluation
            │
            ▼
 Random Forest Selected
            │
            ▼
 Streamlit Web Application
            │
            ▼
 Crop Recommendation
```

---

## 📁 Project Structure

```
Smart-Crop-Recommendation-System/
│
├── app.py
├── crop_info.py
├── crop_recommendation_model.pkl
├── label_encoder.pkl
├── scaler.pkl
├── Crop_recommendation.csv
├── requirements.txt
├── README.md
├── Project_Report.pdf
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Aakash-R18/Smart-Crop-Recommendation-System.git
```

### Navigate to the Project Folder

```bash
cd Smart-Crop-Recommendation-System
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📈 Results

- Successfully compared five Machine Learning algorithms.
- Random Forest achieved the best prediction performance.
- Developed an interactive Streamlit application for real-time crop recommendation.
- Displays prediction confidence and crop information.

---

## 🔮 Future Scope

- Live Weather API Integration
- Fertilizer Recommendation System
- Soil Health Analysis
- Mobile Application Development
- Cloud Deployment
- Multi-language Support

---

## 📚 References

1. Kaggle – Crop Recommendation Dataset
2. Scikit-learn Documentation
3. Streamlit Documentation
4. Python Documentation

---

## 👨‍💻 Author

**Aakash R**

B.Tech Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Presidency University

NVIDIA Machine Learning Project

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
