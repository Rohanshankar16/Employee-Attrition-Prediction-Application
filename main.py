import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Select key features for realistic attrition prediction
features = ["Age", "DailyRate", "Education", "JobRole", "MaritalStatus",
            "MonthlyIncome", "OverTime", "JobSatisfaction", "EnvironmentSatisfaction", "WorkLifeBalance"]
X = df[features]
y = df["Attrition"]

# --- Manual mappings for categorical features ---
education_map = {
    "Below College": 1,
    "College": 2,
    "Bachelor": 3,
    "Master": 4,
    "Doctor": 5
}

jobrole_map = {
    "Sales Executive": 1,
    "Research Scientist": 2,
    "Laboratory Technician": 3,
    "Manufacturing Director": 4,
    "Healthcare Representative": 5,
    "Manager": 6,
    "Sales Representative": 7,
    "Research Director": 8,
    "Human Resources": 9
}

marital_map = {
    "Single": 1,
    "Married": 2,
    "Divorced": 3
}

overtime_map = {"Yes": 1, "No": 0}
satisfaction_map = {"Low": 1, "Medium": 2, "High": 3, "Very High": 4}
worklife_map = {"Bad": 1, "Good": 2, "Better": 3, "Best": 4}

# Apply mappings
X["Education"] = X["Education"].map(education_map)
X["JobRole"] = X["JobRole"].map(jobrole_map)
X["MaritalStatus"] = X["MaritalStatus"].map(marital_map)
X["OverTime"] = X["OverTime"].map(overtime_map)
X["JobSatisfaction"] = X["JobSatisfaction"].map(satisfaction_map)
X["EnvironmentSatisfaction"] = X["EnvironmentSatisfaction"].map(satisfaction_map)
X["WorkLifeBalance"] = X["WorkLifeBalance"].map(worklife_map)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest with class balance to detect leave employees
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as 'model.pkl'.")
