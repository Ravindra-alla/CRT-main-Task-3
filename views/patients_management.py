import streamlit as st
import pandas as pd
from utils.database import get_all_patients, add_patient, add_user
from utils.auth import hash_password
from utils.styles import create_header

def show(user):
    """Patient management page"""
    create_header("Patients Management", "Manage patient records and information")
    
    tab1, tab2 = st.tabs(["View Patients", "Add Patient"])
    
    with tab1:
        st.subheader("👥 Patient List")
        
        # Search and filter
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_query = st.text_input("🔍 Search Patient", placeholder="Name or ID")
        
        with col2:
            status_filter = st.selectbox("Filter by Status", ["All", "Active", "Inactive", "Discharged"])
        
        with col3:
            sort_by = st.selectbox("Sort by", ["Name", "Date", "Last Visit"])
        
        # Get patients
        patients = get_all_patients()
        
        if not patients.empty:
            st.dataframe(patients[['patient_id', 'full_name', 'age', 'gender', 'blood_group', 'email', 'phone']], use_container_width=True)
            
            st.divider()
            
            # Patient details
            selected_patient_idx = st.selectbox("Select Patient for Details", 
                                          range(len(patients)),
                                          format_func=lambda x: f"{patients.iloc[x]['full_name']} (ID: PAT-{patients.iloc[x]['patient_id']:05d})")
            
            if selected_patient_idx is not None:
                patient = patients.iloc[selected_patient_idx]
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("**Personal Info**")
                    st.write(f"Name: {patient['full_name']}")
                    st.write(f"Age: {patient['age']}")
                    st.write(f"Gender: {patient['gender']}")
                
                with col2:
                    st.write("**Contact**")
                    st.write(f"Email: {patient['email']}")
                    st.write(f"Phone: {patient['phone']}")
                
                with col3:
                    st.write("**Medical**")
                    st.write(f"Blood Group: {patient['blood_group']}")
                    st.write(f"Weight: {patient['weight']} kg")
                    st.write(f"Height: {patient['height']} cm")
                    st.write(f"Conditions: {patient['medical_conditions']}")
        else:
            st.info("No patients found")
    
    with tab2:
        st.subheader("➕ Add New Patient")
        
        col1, col2 = st.columns(2)
        
        with col1:
            username = st.text_input("Username", key="new_pat_username")
            password = st.text_input("Password", type="password", key="new_pat_password")
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
        
        with col2:
            age = st.number_input("Age", min_value=1, max_value=150, value=30)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
            weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
            height = st.number_input("Height (cm)", min_value=50, value=170)
        
        medical_conditions = st.multiselect(
            "Medical Conditions",
            ["Diabetes", "Heart Disease", "Hypertension", "Asthma", "Other"]
        )
        
        allergies = st.text_area("Allergies", height=80)
        
        if st.button("Save Patient", use_container_width=True):
            if not username or not password or not full_name or not email:
                st.error("Please fill all required fields (Username, Password, Full Name, Email)")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters")
            else:
                hashed_pwd = hash_password(password)
                user_id = add_user(username, hashed_pwd, email, "Patient", full_name, phone)
                if user_id:
                    # Save patient record
                    med_conds_str = ",".join(medical_conditions)
                    patient_id = add_patient(user_id, age, gender, weight, height, blood_group, med_conds_str, "", allergies)
                    if patient_id:
                        st.success("✅ Patient added successfully!")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error("Failed to add patient record")
                else:
                    st.error("Username or email already exists")
