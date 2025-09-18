# 🏗️ Concrete Compressive Strength

---

## 📌 Project Overview  
Concrete is the most widely used construction material in the world, and its compressive strength is a critical property for structural design and safety. Traditionally, testing concrete strength requires **laboratory experiments** that are time-consuming and costly.  

This project builds a **machine learning model** that predicts the compressive strength of concrete based on its mix proportions (cement, water, aggregates, etc.). The solution is deployed on **Streamlit Cloud** and **Render**, so anyone can try it online without specialized lab equipment. 

---

## 🚀 Live Demo  

- [🌍 Render App](https://cement-compressive-strength-prediction.onrender.com)  
- [⚡ Streamlit Cloud App](https://cement-compressive-strength-prediction-expfvdryzmvleb7ar7fadp.streamlit.app/)  

### Demo Screenshots / Videos  
[![Streamlit Demo](images/streamlit_demo.png)](YOUR_STREAMLIT_LINK)  
 
---

## 📂 Table of Contents  
1. [Dataset](#-dataset)  
2. [Project Workflow](#-project-workflow)  
3. [Installation & Usage](#-installation--usage)  
4. [How to Use the App](#-how-to-use-the-app)   
5. [License](#-license)  

---

## 📊 Dataset  
- **Source:** [UCI Machine Learning Repository – Concrete Compressive Strength Dataset](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength)  
- **Description:**  
  - Features (ingredients in kg/m³):  
    - Cement  
    - Blast Furnace Slag  
    - Fly Ash  
    - Water  
    - Superplasticizer  
    - Coarse Aggregate  
    - Fine Aggregate  
    - Age (in days)  
  - Target: **Compressive Strength (MPa)**  

---

## ⚙️ Project Workflow  
1. **Data Collection** → UCI dataset.  
2. **Data Preprocessing** → Checked for missing values, normalized features.  
3. **Model Training** → Trained regression models (e.g., Random Forest, Gradient Boosting).  
4. **Model Evaluation** → Evaluated using MAE, RMSE, R² score.  
5. **Deployment** → Deployed interactive app using Streamlit on Streamlit Cloud & Render.  

---

## 💻 Installation & Usage  

Clone the repository:  
`bash
git clone git@github.com:Calaabdul/Cement-compressive-strength-prediction.git
cd concrete-compressive-strength`

---

Run locally with Streamlit:
`streamlit run app.py`

Or access the live demos above.

## 🖱️ How to Use the App

- Open the deployed app on Render or Streamlit Cloud.
- Enter the physical measurements of an abalone (Length, Diameter, Weight, etc.).
- Click Predict.

The model will output the estimated age (in years) of the abalone.


## 🛠 Tech Stack

Language: Python 3.9+

Libraries: Pandas, NumPy, Scikit-learn, Streamlit, Matplotlib/Seaborn

Deployment: Streamlit Cloud, Render


## Create a virtual environment and install dependencies:
`pip install -r requirements.txt`

