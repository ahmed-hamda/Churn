# 🔮 Churn Prediction System  
**Machine Learning · Flask API · Swagger · Angular Dashboard**

This project is a **complete customer churn prediction application**, composed of:

- 🔙 Flask backend exposing a REST API documented with Swagger  
- 🧠 Machine Learning models (Random Forest / XGBoost)  
- 🔜 Angular frontend for visualization and prediction  
- 📊 Interactive dashboard  
- 🖼️ Demonstration screenshots  

---

## 🎯 Project Objectives

- Predict whether a customer is likely to churn  
- Expose a Machine Learning model through a REST API  
- Visualize statistics and prediction results in an Angular interface  
- Easily test endpoints using Swagger UI  
- Clearly separate frontend and backend layers  

---

## 📁 Global Project Structure

```

CHURN/
│
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── random_forest_tuned.joblib
│   │   └── scaler.joblib
│   └── venv/                # ignored
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── angular.json
│   ├── package.json
│   ├── tsconfig.json
│   └── node_modules/        # ignored
│
├── Demo/
│   ├── customer info.png
│   ├── dashboard.png
│   ├── predicted features.png
│   └── prediction result.png
│
├── .gitignore
└── README.md

````

---

## 🚀 Installation and Execution

### 🔙 Backend (Flask API)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
````

📍 API: [http://localhost:5000](http://localhost:5000)
📘 Swagger: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

### 🔜 Frontend (Angular)

```bash
cd frontend
npm install
ng serve --open
```

📍 Application: [http://localhost:4200](http://localhost:4200)

---

## 📡 API – Main Endpoints

### ✔ /api/health

```json
{ "status": "ok" }
```

### ✔ /api/dashboard

* Dataset statistics
* ML model performance
* Best performing model
* Most important features

### ✔ /api/predict (POST)

```json
{
  "CreditScore": 650,
  "Gender": 0,
  "Age": 40,
  "Tenure": 5,
  "Balance": 60000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 80000,
  "Geography_Germany": 0,
  "Geography_Spain": 1
}
```

```json
{
  "success": true,
  "result": {
    "prediction": 1,
    "label": "Churn",
    "probability": 0.67
  }
}
```

---

## 🌐 Angular Integration

```ts
this.http.get("http://localhost:5000/api/dashboard");
this.http.post("http://localhost:5000/api/predict", payload);
```

✔ CORS is enabled on the Flask backend.

---

## 🖼️ Demo – Screenshots

### 🔹 Dashboard

![Dashboard](Demo/dashboard.png)

### 🔹 Predicted Features

![Predicted Features](Demo/predicted%20features.png)

### 🔹 Customer Info

![Customer Info](Demo/customer%20info.png)

### 🔹 Prediction Result

![Prediction Result](Demo/prediction%20result.png)

---

## 🛠️ Technologies Used

* Backend: Python, Flask, Swagger (Flasgger)
* Machine Learning: Scikit-learn, Random Forest, XGBoost
* Frontend: Angular, TypeScript, HTML, CSS
* Tools: Git, GitHub, Swagger UI

---

## 👤 Author

Ahmed Hamda
Engineering Student – Web & Multimedia Technologies (TWM)
ISIMS – Sfax
[https://github.com/ahmed-hamda](https://github.com/ahmed-hamda)

