# Employee-Attrition-Prediction-Application

## 📌 Overview
This project is a **web-based application** that predicts whether an employee is likely to leave a company (attrition) using a machine learning model (**Random Forest**).  
The app is built using **Python**, **Scikit-learn**, **Pandas**, and **Streamlit** for the front-end interface.  

The app is user-friendly and designed for **non-developers**, with **human-readable input fields** and **probability of leaving** displayed.

---

## ✨ Features

- Predicts if an employee will **stay** or **leave** the company.  
- Uses **10 key features**:  
  - Age  
  - Daily Rate  
  - Education  
  - Job Role  
  - Marital Status  
  - Monthly Income  
  - OverTime  
  - Job Satisfaction  
  - Environment Satisfaction  
  - Work-Life Balance  
- Shows **probability of leaving**.  
- Easy-to-use **dropdowns and sliders** for input.  
- Trained with **Random Forest Classifier** with class balancing.  

---

## 🛠 Requirements

- Python 3.10 or higher  
- Libraries:  
  - pandas  
  - numpy  
  - scikit-learn  
  - streamlit  

Install the requirements using:

```bash
pip install pandas numpy scikit-learn streamlit
```
### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Employee-Attrition-Prediction.git
   cd Employee-Attrition-Prediction
   ```
2.Create a virtual environment
   ```bash

 python -m venv venv

  ```
3.Activate the virtual environment

Windows:
 ```bash
venv\Scripts\activate
```

Mac/Linux:
 ```bash
source venv/bin/activate
```

4.Install dependencies
 ```bash
pip install -r requirements.txt
```

5.Run the Streamlit app
 ```bash
streamlit run app.py
```
6.The app is usually accessed at ` http://localhost:8501`
  
---

##  Example Prediction

-**Example inputs for predicting an employee likely to leave**:
  
   - Age: 25
   - Daily Rate: 400
   - Education: Bachelor
   - Job Role: Sales Executive
   - Marital Status: Single
   - Monthly Income: 3000
   - OverTime: Yes
   - Job Satisfaction: Low
   - Environment Satisfaction: Low
   - Work-Life Balance: Bad




