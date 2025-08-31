# Employee-Attrition-Prediction-Application
Overview:

*Item 1This project is a web-based application that predicts whether an employee is likely to leave a company (attrition) using a machine learning model (Random Forest).
*Item 2The app is built using Python, Scikit-learn, Pandas, and Streamlit for the front-end interface.
*Item 3The app is user-friendly and designed for non-developers, with human-readable input fields and probability of leaving displayed.

Features

Predicts if an employee will stay or leave the company.

Uses 10 key features:

Age

Daily Rate

Education

Job Role

Marital Status

Monthly Income

OverTime

Job Satisfaction

Environment Satisfaction

Work-Life Balance

Shows probability of leaving.

Easy-to-use dropdowns and sliders for input.

Trained with Random Forest Classifier with class balancing.

Requirements

Python 3.10 or higher

Libraries:

pandas

numpy

scikit-learn

streamlit

You can install the requirements using:

pip install pandas numpy scikit-learn streamlit

Project Files

main.py – Trains the Random Forest model on the HR dataset and saves model.pkl.

app.py – Streamlit web app that loads the trained model and takes user input to predict attrition.

WA_Fn-UseC_-HR-Employee-Attrition.csv – Sample HR dataset.

How to Run
1. Clone the repository
git clone <your-repo-url>
cd Employee-Attrition-Prediction

2. Create a virtual environment (optional but recommended)
python -m venv venv

3. Activate the virtual environment

Windows:

.\venv\Scripts\activate


Linux/MacOS:

source venv/bin/activate

4. Install dependencies
pip install pandas numpy scikit-learn streamlit

5. Train the model
python main.py


This will train the Random Forest model and create model.pkl in the project folder.

6. Run the Streamlit app
streamlit run app.py


The app will open in your browser (usually at http://localhost:8501
).

Fill in the fields and click Predict Attrition to see the result.

Notes

The model uses manual mappings for categorical fields, so dropdown selections are human-readable.

Model predictions are more realistic because key attrition-related features are included, and class imbalance is handled.

Example inputs for predicting an employee likely to leave:

Age: 25

Daily Rate: 400

Education: Bachelor

Job Role: Sales Executive

Marital Status: Single

Monthly Income: 3000

OverTime: Yes

Job Satisfaction: Low

Environment Satisfaction: Low

Work-Life Balance: Bad
