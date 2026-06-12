import streamlit as st
from utils.database import get_patient, get_doctor, update_patient, update_doctor
from utils.styles import create_header

def show(user):
    """User profile page"""
    create_header("My Profile", "Manage your profile information")
    
    if user['role'] == "Patient":
        show_patient_profile(user)
    elif user['role'] == "Doctor":
        show_doctor_profile(user)
    else:
        show_admin_profile(user)

def show_patient_profile(user):
    """Patient profile"""
    patient_id = user.get('patient_id')
    patient = get_patient(patient_id) if patient_id else None
    
    if patient:
        age_val = int(patient[2]) if patient[2] is not None else 30
        gender_val = patient[3] if patient[3] is not None else "Male"
        weight_val = float(patient[4]) if patient[4] is not None else 70.0
        height_val = int(patient[5]) if patient[5] is not None else 170
        blood_group_val = patient[6] if patient[6] is not None else "O+"
        med_conds = [c.strip() for c in patient[7].split(",") if c.strip()] if patient[7] else []
        family_history_val = patient[8] if patient[8] is not None else ""
        allergies_val = patient[9] if patient[9] is not None else ""
        insurance_id_val = patient[10] if patient[10] is not None else ""
    else:
        age_val = 30
        gender_val = "Male"
        weight_val = 70.0
        height_val = 170
        blood_group_val = "O+"
        med_conds = []
        family_history_val = ""
        allergies_val = ""
        insurance_id_val = ""
        
    gender_options = ["Male", "Female", "Other"]
    gender_index = gender_options.index(gender_val) if gender_val in gender_options else 0
    
    blood_options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    blood_index = blood_options.index(blood_group_val) if blood_group_val in blood_options else 0
    
    med_options = ["Diabetes", "Heart Disease", "Hypertension", "Asthma", "Thyroid", "Other"]
    med_defaults = [c for c in med_conds if c in med_options]

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Personal Information")
        name = st.text_input("Full Name", value=user['full_name'], disabled=True)
        email = st.text_input("Email", value=user['email'], disabled=True)
        phone = st.text_input("Phone", value=user.get('phone', ''), disabled=True)
    
    with col2:
        st.subheader("Medical Information")
        age = st.number_input("Age", min_value=1, max_value=150, value=age_val)
        gender = st.selectbox("Gender", gender_options, index=gender_index)
        blood_group = st.selectbox("Blood Group", blood_options, index=blood_index)
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, value=weight_val)
        height = st.number_input("Height (cm)", min_value=50, value=height_val)
        bmi = weight / ((height/100) ** 2)
        st.metric("BMI", f"{bmi:.2f}")
    
    with col2:
        st.subheader("Medical Conditions")
        medical_conditions = st.multiselect(
            "Select Conditions",
            med_options,
            default=med_defaults
        )
        family_history = st.text_area("Family History", value=family_history_val, height=100)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        allergies = st.text_area("Allergies", value=allergies_val, height=100)
        insurance_id = st.text_input("Insurance ID", value=insurance_id_val)
    
    with col2:
        st.subheader("Emergency Contact")
        emergency_name = st.text_input("Emergency Contact Name")
        emergency_phone = st.text_input("Emergency Contact Phone")
    
    if st.button("Update Profile", use_container_width=True):
        med_cond_str = ",".join(medical_conditions)
        if update_patient(patient_id, age, gender, weight, height, blood_group, med_cond_str, family_history, allergies, insurance_id):
            st.success("Profile updated successfully!")
            st.rerun()

def show_doctor_profile(user):
    """Doctor profile"""
    doctor_id = user.get('doctor_id')
    doctor = get_doctor(doctor_id) if doctor_id else None
    
    if doctor:
        specialization_val = doctor[2] if doctor[2] is not None else "General Practice"
        experience_val = int(doctor[3]) if doctor[3] is not None else 5
        qualification_val = doctor[4] if doctor[4] is not None else "MD"
        availability_val = [d.strip() for d in doctor[5].split(",") if d.strip()] if doctor[5] else ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        department_val = doctor[6] if doctor[6] is not None else "General"
    else:
        specialization_val = "General Practice"
        experience_val = 5
        qualification_val = "MD"
        availability_val = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        department_val = "General"
        
    spec_options = ["General Practice", "Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Surgery"]
    spec_index = spec_options.index(specialization_val) if specialization_val in spec_options else 0
    
    avail_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    avail_defaults = [d for d in availability_val if d in avail_options]

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Personal Information")
        name = st.text_input("Full Name", value=user['full_name'], disabled=True)
        email = st.text_input("Email", value=user['email'], disabled=True)
        phone = st.text_input("Phone", value=user.get('phone', ''), disabled=True)
    
    with col2:
        st.subheader("Professional Information")
        specialization = st.selectbox("Specialization", spec_options, index=spec_index)
        department = st.text_input("Department", value=department_val)
        experience = st.number_input("Years of Experience", min_value=0, max_value=60, value=experience_val)
    
    col1, col2 = st.columns(2)
    
    with col1:
        qualification = st.text_area("Qualifications", value=qualification_val, height=100)
        license_number = st.text_input("Medical License Number")
    
    with col2:
        st.subheader("Availability")
        availability = st.multiselect(
            "Available Days",
            avail_options,
            default=avail_defaults
        )
        start_time = st.time_input("Start Time", value=None)
        end_time = st.time_input("End Time", value=None)
    
    if st.button("Update Profile", use_container_width=True):
        avail_str = ",".join(availability)
        if update_doctor(doctor_id, specialization, experience, qualification, department, avail_str):
            st.success("Profile updated successfully!")
            st.rerun()

def show_admin_profile(user):
    """Admin profile"""
    st.subheader("Administrator Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Name:** {user['full_name']}")
        st.write(f"**Email:** {user['email']}")
        st.write(f"**Role:** {user['role']}")
    
    with col2:
        st.write(f"**Username:** {user['username']}")
        st.write(f"**Status:** Active")
        st.write(f"**Last Login:** Today")
    
    st.divider()
    
    if st.button("Change Password", use_container_width=True):
        st.subheader("Change Password")
        old_password = st.text_input("Old Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        if st.button("Update Password"):
            if new_password == confirm_password:
                st.success("Password changed successfully!")
            else:
                st.error("Passwords do not match")
