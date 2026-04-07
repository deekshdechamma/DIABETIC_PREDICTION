# 🩺 Diabetes Prediction System

A simple and interactive **Machine Learning web application** built using **Streamlit** that predicts the likelihood of diabetes based on user input symptoms and basic patient information.

---

## 📌 Project Overview

The goal of this project is to provide a **quick and user-friendly tool** to estimate diabetes risk using basic health indicators and symptoms.

Diabetes prediction systems are widely used in healthcare to assist in **early detection and preventive care** :contentReference[oaicite:1]{index=1}.

This application demonstrates:
- Machine Learning concepts  
- Web app deployment using Streamlit  
- Model integration using Pickle  

> ⚠️ Disclaimer: This is a demo project for educational purposes only.

---

## 🚀 Features

- 🖥️ Interactive Streamlit UI  
- 📊 Input patient details (Age, Gender)  
- 🧾 14 symptom-based inputs  
- ⚡ Instant prediction result  
- 🔄 Automatic fallback model if no trained model is found  
- 🎯 Simple and easy-to-use interface  

---

## 🧠 How It Works

The system takes input features such as:
- Age  
- Gender  
- Symptoms (Yes/No converted into binary values)

### Prediction Logic:
- If number of symptoms ≥ 3 → **High Risk**
- Else → **Low Risk**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **NumPy**
- **Pickle**

---

## 📂 Project Structure
