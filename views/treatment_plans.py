import streamlit as st
import pandas as pd
from models.predictors import TreatmentRecommender, PatientOutcomePredictor
from utils.styles import create_header

def show(user):
    """Treatment plans page"""
    create_header("Treatment Recommendations", "View and Manage Treatment Plans")
    
    tab1, tab2 = st.tabs(["My Patients", "Treatment Plans"])
    
    with tab1:
        st.subheader("👥 Patient List")
        
        patients = pd.DataFrame({
            'Patient ID': [1, 2, 3, 4],
            'Name': ['John Doe', 'Jane Smith', 'Bob Wilson', 'Alice Johnson'],
            'Disease': ['Diabetes', 'Heart Disease', 'Hypertension', 'Kidney Disease'],
            'Risk Level': ['High', 'Medium', 'Low', 'High'],
            'Last Treatment': ['2024-01-10', '2024-01-08', '2024-01-05', '2024-01-12']
        })
        
        st.dataframe(patients, use_container_width=True)
        
        # Select patient
        selected_patient = st.selectbox("Select Patient", patients['Name'])
    
    with tab2:
        st.subheader("💊 Treatment Plans")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Current Treatment Plan")
            
            disease = st.selectbox("Disease", ["Diabetes", "Heart Disease", "Kidney Disease", "Hypertension"])
            severity = st.selectbox("Severity", ["High", "Medium", "Low"])
        
        with col2:
            st.subheader("Patient Information")
            age = st.number_input("Age", min_value=1, max_value=150, value=50)
            comorbidities = st.number_input("Number of Comorbidities", min_value=0, max_value=10, value=1)
            treatment_duration = st.selectbox("Treatment Duration", ["1 week", "2 weeks", "1 month", "3 months", "6 months"])
        
        st.divider()
        
        if st.button("Generate Treatment Plan"):
            st.subheader("📋 Recommended Treatment Plan")
            
            # Get recommendations
            recommendations = TreatmentRecommender.recommend_treatment(disease, severity)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Treatment Recommendations:**")
                for i, rec in enumerate(recommendations, 1):
                    st.write(f"{i}. {rec}")
            
            with col2:
                st.write("**Outcome Predictions:**")
                recovery_prob = PatientOutcomePredictor.predict_recovery(age, severity, comorbidities)
                icu_needed = PatientOutcomePredictor.predict_icu_requirement(severity, 120, 96)
                duration = PatientOutcomePredictor.predict_hospitalization_duration(age, disease, severity)
                
                st.metric("Recovery Probability", f"{recovery_prob:.1f}%")
                st.metric("ICU Required", "Yes" if icu_needed else "No")
                st.metric("Expected Duration", f"{duration} days")
            
            st.divider()
            
            # Medication schedule
            st.subheader("💊 Medication Schedule")
            
            medications = pd.DataFrame({
                'Medication': ['Metformin', 'Enalapril', 'Aspirin', 'Lisinopril'],
                'Dosage': ['500 mg', '10 mg', '100 mg', '5 mg'],
                'Frequency': ['Twice daily', 'Once daily', 'Once daily', 'Once daily'],
                'Duration': ['Ongoing', 'Ongoing', '3 months', 'Ongoing'],
                'Side Effects': ['Nausea', 'Dizziness', 'Bleeding risk', 'Cough']
            })
            
            st.dataframe(medications, use_container_width=True)
            
            st.divider()
            
            # Follow-up schedule
            st.subheader("📅 Follow-up Schedule")
            
            followup_data = pd.DataFrame({
                'Date': ['2024-02-15', '2024-03-15', '2024-04-15', '2024-05-15'],
                'Type': ['Lab Test', 'Check-up', 'Lab Test', 'Check-up'],
                'Doctor': ['Dr. Smith', 'Dr. Johnson', 'Dr. Smith', 'Dr. Johnson'],
                'Notes': ['Fasting blood test', 'General checkup', 'Lipid profile', 'Review treatment']
            })
            
            st.dataframe(followup_data, use_container_width=True)
            
            # Save plan
            if st.button("Save Treatment Plan"):
                st.success("✅ Treatment plan saved successfully!")
                st.balloons()
