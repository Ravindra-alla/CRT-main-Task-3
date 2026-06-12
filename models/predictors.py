import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os

class DiseasePredictor:
    """ML models for disease prediction"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.diabetes_model = None
        self.heart_disease_model = None
        self.kidney_disease_model = None
        self.cancer_risk_model = None
        self.train_models()
    
    def generate_training_data(self, n_samples=1000):
        """Generate synthetic training data"""
        np.random.seed(42)
        
        # Diabetes data
        age = np.random.randint(20, 80, n_samples)
        bmi = np.random.uniform(15, 40, n_samples)
        blood_glucose = np.random.uniform(60, 300, n_samples)
        blood_pressure_systolic = np.random.uniform(90, 180, n_samples)
        family_history = np.random.choice([0, 1], n_samples)
        
        # Create labels based on simple rules
        diabetes_labels = (
            (blood_glucose > 125) | 
            ((bmi > 30) & (blood_glucose > 100)) |
            ((family_history == 1) & (blood_glucose > 110))
        ).astype(int)
        
        X_diabetes = np.column_stack([age, bmi, blood_glucose, blood_pressure_systolic, family_history])
        
        # Heart Disease data
        cholesterol = np.random.uniform(100, 350, n_samples)
        heart_rate = np.random.randint(40, 120, n_samples)
        chest_pain = np.random.randint(0, 4, n_samples)
        
        heart_disease_labels = (
            (cholesterol > 240) | 
            ((blood_pressure_systolic > 140) & (cholesterol > 200)) |
            ((chest_pain > 0) & (cholesterol > 200))
        ).astype(int)
        
        X_heart = np.column_stack([age, cholesterol, blood_pressure_systolic, heart_rate, chest_pain])
        
        # Kidney Disease data
        creatinine = np.random.uniform(0.4, 8, n_samples)
        bun = np.random.uniform(7, 100, n_samples)
        gfr = np.random.uniform(10, 120, n_samples)
        
        kidney_disease_labels = (
            (creatinine > 2.0) | 
            ((bun > 20) & (creatinine > 1.2)) |
            (gfr < 30)
        ).astype(int)
        
        X_kidney = np.column_stack([age, creatinine, bun, gfr, blood_pressure_systolic])
        
        # Cancer Risk data
        age_cancer = np.random.randint(30, 80, n_samples)
        smoking_history = np.random.choice([0, 1], n_samples)
        tumor_size = np.random.uniform(0, 20, n_samples)
        inflammation = np.random.uniform(0, 10, n_samples)
        
        cancer_labels = (
            ((age_cancer > 50) & (smoking_history == 1)) |
            (tumor_size > 10) |
            ((inflammation > 5) & (age_cancer > 40))
        ).astype(int)
        
        X_cancer = np.column_stack([age_cancer, smoking_history, tumor_size, inflammation, bmi])
        
        return (X_diabetes, diabetes_labels), (X_heart, heart_disease_labels), \
               (X_kidney, kidney_disease_labels), (X_cancer, cancer_labels)
    
    def train_models(self):
        """Train all prediction models"""
        (X_diabetes, y_diabetes), (X_heart, y_heart), \
        (X_kidney, y_kidney), (X_cancer, y_cancer) = self.generate_training_data()
        
        # Diabetes Model (Random Forest)
        self.diabetes_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.diabetes_model.fit(X_diabetes, y_diabetes)
        
        # Heart Disease Model (Logistic Regression)
        self.heart_disease_model = LogisticRegression(random_state=42, max_iter=1000)
        self.heart_disease_model.fit(X_heart, y_heart)
        
        # Kidney Disease Model (Random Forest)
        self.kidney_disease_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.kidney_disease_model.fit(X_kidney, y_kidney)
        
        # Cancer Risk Model (Logistic Regression)
        self.cancer_risk_model = LogisticRegression(random_state=42, max_iter=1000)
        self.cancer_risk_model.fit(X_cancer, y_cancer)
    
    def predict_diabetes(self, age, bmi, blood_glucose, blood_pressure_systolic, family_history):
        """Predict diabetes risk"""
        X = np.array([[age, bmi, blood_glucose, blood_pressure_systolic, family_history]])
        probability = self.diabetes_model.predict_proba(X)[0][1]
        risk_score = probability * 100
        
        if risk_score > 70:
            severity = "High"
        elif risk_score > 40:
            severity = "Medium"
        else:
            severity = "Low"
        
        return risk_score, severity
    
    def predict_heart_disease(self, age, cholesterol, blood_pressure_systolic, heart_rate, chest_pain):
        """Predict heart disease risk"""
        X = np.array([[age, cholesterol, blood_pressure_systolic, heart_rate, chest_pain]])
        probability = self.heart_disease_model.predict_proba(X)[0][1]
        risk_score = probability * 100
        
        if risk_score > 70:
            severity = "High"
        elif risk_score > 40:
            severity = "Medium"
        else:
            severity = "Low"
        
        return risk_score, severity
    
    def predict_kidney_disease(self, age, creatinine, bun, gfr, blood_pressure_systolic):
        """Predict kidney disease risk"""
        X = np.array([[age, creatinine, bun, gfr, blood_pressure_systolic]])
        probability = self.kidney_disease_model.predict_proba(X)[0][1]
        risk_score = probability * 100
        
        if risk_score > 70:
            severity = "High"
        elif risk_score > 40:
            severity = "Medium"
        else:
            severity = "Low"
        
        return risk_score, severity
    
    def predict_cancer_risk(self, age, smoking_history, tumor_size, inflammation, bmi):
        """Predict cancer risk"""
        X = np.array([[age, smoking_history, tumor_size, inflammation, bmi]])
        probability = self.cancer_risk_model.predict_proba(X)[0][1]
        risk_score = probability * 100
        
        if risk_score > 70:
            severity = "High"
        elif risk_score > 40:
            severity = "Medium"
        else:
            severity = "Low"
        
        return risk_score, severity

class TreatmentRecommender:
    """Treatment recommendation engine"""
    
    @staticmethod
    def recommend_treatment(disease, severity):
        """Recommend treatment based on disease and severity"""
        treatments = {
            "Diabetes": {
                "High": ["Intensive insulin therapy", "Daily glucose monitoring", "Consult endocrinologist", "Dietary management"],
                "Medium": ["Oral medications", "Regular glucose monitoring", "Exercise routine", "Dietary modification"],
                "Low": ["Lifestyle changes", "Regular checkups", "Weight management", "Stress reduction"]
            },
            "Heart Disease": {
                "High": ["Cardiology consultation", "ECG monitoring", "Cardiac medication", "Consider hospitalization"],
                "Medium": ["Beta-blockers", "ACE inhibitors", "Stress test", "Regular checkups"],
                "Low": ["Lifestyle modifications", "Regular exercise", "Healthy diet", "Blood pressure monitoring"]
            },
            "Kidney Disease": {
                "High": ["Nephrology consultation", "Dialysis preparation", "Medication management", "Regular testing"],
                "Medium": ["Renal diet", "Blood pressure control", "Monitor kidney function", "Medication"],
                "Low": ["Hydration management", "Regular checkups", "Avoid nephrotoxic drugs", "Healthy lifestyle"]
            },
            "Cancer": {
                "High": ["Oncology consultation", "Biopsy", "Advanced imaging", "Consider treatment options"],
                "Medium": ["Specialist consultation", "Screening tests", "Monitoring protocol", "Preventive measures"],
                "Low": ["Regular screening", "Healthy lifestyle", "Avoid risk factors", "Preventive checkups"]
            }
        }
        
        return treatments.get(disease, {}).get(severity, ["Consult healthcare provider"])

class PatientOutcomePredictor:
    """Predict patient outcomes"""
    
    @staticmethod
    def predict_recovery(age, severity, comorbidities):
        """Predict recovery probability"""
        recovery_score = 100
        
        # Age factor
        if age > 70:
            recovery_score -= 20
        elif age > 50:
            recovery_score -= 10
        
        # Severity factor
        if severity == "High":
            recovery_score -= 40
        elif severity == "Medium":
            recovery_score -= 20
        
        # Comorbidities
        recovery_score -= comorbidities * 5
        
        recovery_prob = max(30, recovery_score)
        return recovery_prob
    
    @staticmethod
    def predict_icu_requirement(severity, blood_pressure, oxygen_level):
        """Predict if ICU admission is needed"""
        icu_required = False
        
        if severity == "High":
            icu_required = True
        elif oxygen_level < 95:
            icu_required = True
        elif blood_pressure < 90:
            icu_required = True
        
        return icu_required
    
    @staticmethod
    def predict_hospitalization_duration(age, disease, severity):
        """Predict expected hospitalization duration"""
        base_duration = 5
        
        if severity == "High":
            base_duration = 14
        elif severity == "Medium":
            base_duration = 10
        
        if disease == "Cancer":
            base_duration += 5
        elif disease == "Kidney Disease":
            base_duration += 7
        
        if age > 70:
            base_duration += 3
        
        return base_duration
