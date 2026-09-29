# 🚗 MPG Predictor

A Machine Learning project that predicts **vehicle fuel efficiency (MPG — Miles Per Gallon)** based on **horsepower** using **Polynomial Regression**.

The project demonstrates an end-to-end Machine Learning workflow, from data preprocessing and exploratory data analysis to model deployment using **FastAPI** and **Streamlit**.

---

## 📸 Demo

### 🚗 MPG Predictor — Streamlit Application

<img width="1916" height="841" alt="Image" src="https://github.com/user-attachments/assets/a04a87d5-931a-4e42-8c11-204cba52b33b" />

> Enter the vehicle's horsepower and click **Predict MPG** to get the estimated fuel efficiency.

### 🔄 Prediction Workflow

```text
User
 │
 ▼
Enter Horsepower
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
Polynomial Regression Model
 │
 ▼
Predicted MPG
 │
 ▼
Streamlit Result
```

### 📁 Add the Screenshot

Place your screenshot inside the `assets` folder:

```text
MPG-Predicter/
│
├── assets/
│   └── mpg-predictor-demo.png
│
├── Data/
├── Notebook/
├── backend/
├── frontend/
├── requirements.txt
└── README.md
```

**Recommended screenshot:** Capture the complete Streamlit application showing the horsepower input, **Predict MPG** button, prediction result, and model information.

---

# 📌 Project Overview

The **Auto MPG dataset** contains information about different vehicles and their fuel efficiency.

In this project, **horsepower** is used as the input feature to predict **MPG**.

### Problem Statement

> Can we predict a vehicle's fuel efficiency based on its engine horsepower?

### Solution

A **Polynomial Regression** model is trained to capture the nonlinear relationship between horsepower and MPG.

The trained model is integrated with:

* **FastAPI** → Backend prediction API
* **Streamlit** → Interactive frontend
* **Scikit-learn** → Machine Learning
* **Joblib** → Model serialization

---

# 🎯 Project Objectives

* Understand the relationship between horsepower and MPG.
* Clean and preprocess the dataset.
* Perform Exploratory Data Analysis.
* Analyze potential outliers.
* Build a Linear Regression baseline.
* Build a Polynomial Regression model.
* Evaluate the model using regression metrics.
* Save the trained model using Joblib.
* Build a prediction API using FastAPI.
* Create an interactive UI using Streamlit.

---

# 🧠 Machine Learning Workflow

```text
                Auto MPG Dataset
                       │
                       ▼
                Data Exploration
                       │
                       ▼
                Data Preprocessing
                       │
                       ▼
             Exploratory Data Analysis
                       │
                       ▼
            Horsepower → MPG Analysis
                       │
                       ▼
                Linear Regression
                  (Baseline)
                       │
                       ▼
              Polynomial Features
                  Degree = 3
                       │
                       ▼
             Polynomial Regression
                       │
                       ▼
                Model Evaluation
                       │
                       ▼
              Save Model with Joblib
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              FastAPI     Streamlit
              Backend     Frontend
                 │           │
                 └─────┬─────┘
                       ▼
                 MPG Prediction
```

---

# 📂 Project Structure

```text
MPG-Predicter/
│
├── assets/
│   └── mpg-predictor-demo.png
│
├── Data/
│   ├── auto-mpg.csv
│   └── processed_data.csv
│
├── Notebook/
│   └── MPG.ipynb
│
├── backend/
│   ├── main.py
│   └── polynomial_regression_model.pkl
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project uses the **Auto MPG dataset**.

The dataset contains **398 vehicle records** with information about vehicle specifications and fuel efficiency.

| Feature        | Description                |
| -------------- | -------------------------- |
| `mpg`          | Miles per gallon           |
| `cylinders`    | Number of engine cylinders |
| `displacement` | Engine displacement        |
| `horsepower`   | Engine horsepower          |
| `weight`       | Vehicle weight             |
| `acceleration` | Vehicle acceleration       |
| `model year`   | Vehicle model year         |
| `origin`       | Vehicle origin             |
| `car name`     | Vehicle name               |

### Selected Features

For the final prediction application:

```text
Input Feature  → Horsepower
Target Variable → MPG
```

---

# 🧹 Data Preprocessing

The dataset was inspected and cleaned before model training.

### Preprocessing Steps

1. Checked dataset structure.
2. Checked data types.
3. Checked duplicate records.
4. Checked missing values.
5. Converted `horsepower` from object/string to numeric.
6. Converted invalid/non-numeric values into missing values.
7. Handled missing values.
8. Generated statistical summaries.
9. Analyzed potential outliers using the IQR method.

---

# 🔎 Exploratory Data Analysis

The relationship between **horsepower** and **MPG** was analyzed using visualizations.

A general negative relationship was observed:

```text
Horsepower ↑
     │
     │
     ▼
   MPG ↓
```

This means that vehicles with higher horsepower generally tend to have lower fuel efficiency.

However, the relationship is not perfectly linear.

Therefore, Polynomial Regression was investigated to capture the nonlinear pattern.

---

# 📈 Outlier Analysis

The **IQR (Interquartile Range)** method was used to identify potential outliers.

Potential outliers were identified in the horsepower feature.

These observations were not automatically removed because high horsepower values can represent legitimate high-performance vehicles rather than incorrect data.

The goal was to distinguish between:

```text
Actual Data Error
       vs
Legitimate Extreme Value
```

---

# 🤖 Machine Learning Model

## 1. Linear Regression

Linear Regression was initially used as a baseline model.

The dataset was split into:

```text
80% → Training Data
20% → Testing Data
```

with:

```python
random_state = 42
```

The baseline model helps understand how well a simple linear relationship performs.

---

# 2. Polynomial Regression

Polynomial Regression was used because the relationship between horsepower and MPG is not perfectly linear.

The project uses:

```python
PolynomialFeatures(degree=3)
```

The final model pipeline is:

```text
Horsepower
     │
     ▼
PolynomialFeatures
     │
     │ Degree = 3
     ▼
LinearRegression
     │
     ▼
Predicted MPG
```

The trained pipeline is saved using Joblib:

```text
backend/polynomial_regression_model.pkl
```

This allows the application to load the trained model without retraining it every time.

---

# 📏 Model Evaluation

The model is evaluated using common regression metrics.

## MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

```text
MAE = Average |Actual - Predicted|
```

Lower values indicate smaller average prediction errors.

---

## MSE — Mean Squared Error

MSE squares the prediction errors, giving greater weight to larger errors.

```text
MSE = Average (Actual - Predicted)²
```

---

## RMSE — Root Mean Squared Error

RMSE is the square root of MSE.

```text
RMSE = √MSE
```

It is expressed in the same unit as MPG.

---

## R² Score

R² measures how much of the variation in MPG is explained by the model.

```text
R² = 1 - (Residual Sum of Squares / Total Sum of Squares)
```

The complete model evaluation can be reproduced using:

```text
Notebook/MPG.ipynb
```

---

# ⚙️ FastAPI Backend

The trained Machine Learning model is exposed through a **FastAPI REST API**.

### API Endpoint

```text
POST /predict
```

The API accepts horsepower as a query parameter.

### Example Request

```text
/predict?horsepower=150
```

### Example Response

```json
{
  "horsepower": 150,
  "predicted_mpg": 20.XX
}
```

The backend loads the trained model from:

```text
backend/polynomial_regression_model.pkl
```

---

# 🎨 Streamlit Frontend

The project includes an interactive Streamlit frontend.

The interface allows users to:

1. Enter vehicle horsepower.
2. Click **Predict MPG**.
3. Send the input to the FastAPI backend.
4. Run the trained Polynomial Regression model.
5. Display the predicted MPG.

### Frontend Flow

```text
┌─────────────────────┐
│      Streamlit      │
│      Frontend       │
└──────────┬──────────┘
           │
           │ HTTP Request
           ▼
┌─────────────────────┐
│       FastAPI       │
│       Backend       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Polynomial Regression│
│     Degree = 3      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Predicted MPG     │
└─────────────────────┘
```

---

# 🛠️ Tech Stack

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| **Python**           | Programming language      |
| **Pandas**           | Data manipulation         |
| **NumPy**            | Numerical computation     |
| **Matplotlib**       | Data visualization        |
| **Seaborn**          | Exploratory visualization |
| **Scikit-learn**     | Machine Learning          |
| **Joblib**           | Model serialization       |
| **FastAPI**          | Backend API               |
| **Uvicorn**          | ASGI server               |
| **Streamlit**        | Frontend                  |
| **Requests**         | API communication         |
| **Jupyter Notebook** | ML experimentation        |

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/rat7050/MPG-Predicter.git
```

Move into the project directory:

```bash
cd MPG-Predicter
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

The application requires two services:

```text
FastAPI Backend
       +
Streamlit Frontend
```

---

## Step 1 — Start FastAPI Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### FastAPI Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI allows you to test the prediction API directly from your browser.

---

# Step 2 — Start Streamlit Frontend

Open another terminal.

Activate your virtual environment and run:

```bash
streamlit run frontend/app.py
```

Streamlit will display the local application URL in the terminal.

Usually:

```text
http://localhost:8501
```

---

# 🧪 Test the API

You can test the API using:

* FastAPI Swagger UI
* Postman
* cURL
* Python Requests

### Swagger

Open:

```text
http://127.0.0.1:8000/docs
```

### Example Endpoint

```text
POST /predict?horsepower=150
```

Example response:

```json
{
  "horsepower": 150,
  "predicted_mpg": 20.XX
}
```

---

# 📓 Notebook

The complete Machine Learning workflow is available in:

```text
Notebook/MPG.ipynb
```

The notebook includes:

* Dataset loading
* Data inspection
* Missing-value analysis
* Data cleaning
* Statistical analysis
* Exploratory Data Analysis
* Horsepower vs MPG analysis
* Outlier analysis
* Linear Regression
* Polynomial Regression
* Model evaluation
* Model serialization

---

# 💡 Key Learning Outcomes

This project demonstrates practical Machine Learning concepts including:

* Data cleaning
* Exploratory Data Analysis
* Feature selection
* Regression
* Polynomial Features
* Train-test splitting
* Model evaluation
* MAE
* MSE
* RMSE
* R²
* Model serialization
* REST API development
* Frontend-backend integration
* ML model deployment architecture

The project demonstrates the transition from:

```text
Jupyter Notebook
       ↓
Machine Learning Model
       ↓
Saved Model
       ↓
FastAPI
       ↓
Streamlit
       ↓
End-User Application
```

---

# 🔮 Future Improvements

Some possible improvements for the project:

* Add more vehicle features such as weight and displacement.
* Compare multiple regression algorithms.
* Add Random Forest Regression.
* Add Gradient Boosting.
* Add model comparison visualizations.
* Add prediction error visualization.
* Improve API validation.
* Add automated unit tests.
* Add Docker support.
* Add GitHub Actions CI/CD.
* Deploy the FastAPI backend.
* Deploy the Streamlit frontend.
* Add a prediction history feature.

---

# 📌 Current Architecture

```text
                  ┌──────────────────────┐
                  │    Streamlit UI      │
                  │      Frontend        │
                  └──────────┬───────────┘
                             │
                             │ HTTP Request
                             ▼
                  ┌──────────────────────┐
                  │       FastAPI        │
                  │       Backend        │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Polynomial Regression│
                  │      Degree = 3      │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    Predicted MPG     │
                  └──────────────────────┘
```

---

# 📁 Important Files

| File                                      | Purpose               |
| ----------------------------------------- | --------------------- |
| `Data/auto-mpg.csv`                       | Original dataset      |
| `Data/processed_data.csv`                 | Processed dataset     |
| `Notebook/MPG.ipynb`                      | ML experimentation    |
| `backend/main.py`                         | FastAPI backend       |
| `backend/polynomial_regression_model.pkl` | Trained model         |
| `frontend/app.py`                         | Streamlit application |
| `requirements.txt`                        | Python dependencies   |

---

# 👨‍💻 Author

## Ratnesh Kumar

**B.Tech — Artificial Intelligence & Data Science**

GitHub: **[@rat7050](https://github.com/rat7050)**

---

# ⭐ Support

If you found this project useful for learning Machine Learning, consider giving the repository a ⭐ on GitHub.

---

### 🚗 Built With

```text
Python
Scikit-learn
Pandas
NumPy
FastAPI
Streamlit
Joblib
```

**From Machine Learning notebook → API → Interactive application.**
