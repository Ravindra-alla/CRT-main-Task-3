import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from models.predictors import DiseasePredictor, TreatmentRecommender, PatientOutcomePredictor
from utils.database import add_prediction
from utils.styles import create_header, create_alert

def show(user):
    """Disease prediction page"""
    create_header("Disease Prediction", "AI-Powered Disease Risk Assessment")
    
    tab1, tab2, tab3 = st.tabs(["Diabetes Prediction", "Heart Disease", "Kidney Disease"])
    
    predictor = DiseasePredictor()
    
    with tab1:
        show_diabetes_prediction(predictor, user)
    
    with tab2:
        show_heart_disease_prediction(predictor, user)
    
    with tab3:
        show_kidney_disease_prediction(predictor, user)

def show_diabetes_prediction(predictor, user):
    """Diabetes prediction"""
    st.subheader("🩺 Diabetes Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=150, value=40)
        bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
        blood_glucose = st.number_input("Blood Glucose Level (mg/dL)", min_value=50, max_value=500, value=100)
    
    with col2:
        blood_pressure = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=120)
        family_history = st.selectbox("Family History of Diabetes", [0, 1], format_func=lambda x: "Yes" if x else "No")
    
    if st.button("🔍 Predict Diabetes Risk", use_container_width=True):
        risk_score, severity = predictor.predict_diabetes(
            age, bmi, blood_glucose, blood_pressure, family_history
        )
        
        # Display results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            color = "red" if severity == "High" else "orange" if severity == "Medium" else "green"
            st.metric("Risk Score", f"{risk_score:.1f}%")
        
        with col2:
            st.metric("Severity", severity)
        
        with col3:
            st.metric("Recommendation", "Consult Doctor" if severity in ["High", "Medium"] else "Healthy")
        
        st.divider()
        
        # Display risk gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=risk_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Diabetes Risk Score"},
            delta={'reference': 50},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "darkblue"},
                   'steps': [
                       {'range': [0, 30], 'color': "lightgray"},
                       {'range': [30, 70], 'color': "lightyellow"},
                       {'range': [70, 100], 'color': "lightcoral"}],
                   'threshold': {'line': {'color': "red", 'width': 4},
                               'thickness': 0.75,
                               'value': 90}},
            number={'suffix': "%"}
        ))
        st.plotly_chart(fig, use_container_width=True)
        
        # Treatment recommendations
        st.subheader("💊 Treatment Recommendations")
        recommendations = TreatmentRecommender.recommend_treatment("Diabetes", severity)
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
        
        # Save prediction
        add_prediction(
            patient_id=user['patient_id'],
            prediction_type="Diabetes",
            disease_predicted="Diabetes",
            risk_score=risk_score,
            severity_level=severity,
            model_used="Random Forest"
        )
        st.success("✅ Prediction calculated and saved to history!")

def show_heart_disease_prediction(predictor, user):
    """Heart disease prediction"""
    st.subheader("❤️ Heart Disease Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=150, value=50, key="heart_age")
        cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=400, value=200)
        blood_pressure = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=120, key="heart_bp")
    
    with col2:
        heart_rate = st.number_input("Resting Heart Rate (bpm)", min_value=30, max_value=200, value=70)
        chest_pain = st.selectbox("Chest Pain Type", [0, 1, 2, 3], 
                                 format_func=lambda x: ["None", "Typical", "Atypical", "Asymptomatic"][x])
    
    if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):
        risk_score, severity = predictor.predict_heart_disease(
            age, cholesterol, blood_pressure, heart_rate, chest_pain
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Risk Score", f"{risk_score:.1f}%")
        
        with col2:
            st.metric("Severity", severity)
        
        with col3:
            st.metric("Recommendation", "Consult Doctor" if severity in ["High", "Medium"] else "Healthy")
        
        st.divider()
        
        # Treatment recommendations
        st.subheader("💊 Treatment Recommendations")
        recommendations = TreatmentRecommender.recommend_treatment("Heart Disease", severity)
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
        
        # Save prediction
        add_prediction(
            patient_id=user['patient_id'],
            prediction_type="Heart Disease",
            disease_predicted="Heart Disease",
            risk_score=risk_score,
            severity_level=severity,
            model_used="Logistic Regression"
        )
        st.success("✅ Prediction calculated and saved to history!")

def show_kidney_disease_prediction(predictor, user):
    """Kidney disease prediction"""
    st.subheader("🔬 Kidney Disease Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=150, value=45, key="kidney_age")
        creatinine = st.number_input("Creatinine Level (mg/dL)", min_value=0.4, max_value=10.0, value=1.0)
        bun = st.number_input("Blood Urea Nitrogen (mg/dL)", min_value=5, max_value=150, value=20)
    
    with col2:
        gfr = st.number_input("Glomerular Filtration Rate (GFR)", min_value=10, max_value=150, value=90)
        blood_pressure = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=120, key="kidney_bp")
    
    if st.button("🔍 Predict Kidney Disease Risk", use_container_width=True):
        risk_score, severity = predictor.predict_kidney_disease(
            age, creatinine, bun, gfr, blood_pressure
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Risk Score", f"{risk_score:.1f}%")
        
        with col2:
            st.metric("Severity", severity)
        
        with col3:
            st.metric("Recommendation", "Consult Doctor" if severity in ["High", "Medium"] else "Healthy")
        
        st.divider()
        
        # Treatment recommendations
        st.subheader("💊 Treatment Recommendations")
        recommendations = TreatmentRecommender.recommend_treatment("Kidney Disease", severity)
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
        
        # Save prediction
        add_prediction(
            patient_id=user['patient_id'],
            prediction_type="Kidney Disease",
            disease_predicted="Kidney Disease",
            risk_score=risk_score,
            severity_level=severity,
            model_used="Random Forest"
        )
        st.success("✅ Prediction calculated and saved to history!")
