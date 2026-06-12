import streamlit as st
import pandas as pd
from utils.database import get_all_doctors, add_doctor, add_user
from utils.auth import hash_password
from utils.styles import create_header

def show(user):
    """Doctor management page"""
    create_header("Doctors Management", "Manage doctor records")
    
    tab1, tab2 = st.tabs(["View Doctors", "Add Doctor"])
    
    with tab1:
        st.subheader("👨‍⚕️ Doctor List")
        
        # Search and filter
        col1, col2 = st.columns(2)
        
        with col1:
            search_query = st.text_input("🔍 Search Doctor", placeholder="Name or Specialty")
        
        with col2:
            specialty_filter = st.selectbox("Filter by Specialty", 
                ["All", "Cardiology", "Neurology", "Orthopedics", "General Practice"])
        
        # Get doctors
        doctors = get_all_doctors()
        
        if not doctors.empty:
            st.dataframe(doctors[['full_name', 'specialization', 'experience', 'qualification', 'department', 'email', 'phone']], use_container_width=True)
            
            st.divider()
            
            # Doctor details
            if len(doctors) > 0:
                selected_doctor_idx = st.selectbox("Select Doctor for Details", 
                                                  range(len(doctors)), 
                                                  format_func=lambda x: f"Dr. {doctors.iloc[x]['full_name']} ({doctors.iloc[x]['specialization']})")
                
                doctor = doctors.iloc[selected_doctor_idx]
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("**Professional Info**")
                    st.write(f"Doctor Name: Dr. {doctor['full_name']}")
                    st.write(f"Specialization: {doctor['specialization']}")
                    st.write(f"Experience: {doctor['experience']} years")
                
                with col2:
                    st.write("**Department**")
                    st.write(f"Department: {doctor['department']}")
                    st.write(f"Qualification: {doctor['qualification']}")
                
                with col3:
                    st.write("**Status**")
                    st.write(f"Status: Active")
                    st.write(f"Availability: Mon-Fri")
        else:
            st.info("No doctors found")
    
    with tab2:
        st.subheader("➕ Add New Doctor")
        
        col1, col2 = st.columns(2)
        
        with col1:
            username = st.text_input("Username", key="new_doc_username")
            password = st.text_input("Password", type="password", key="new_doc_password")
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
        
        with col2:
            specialization = st.selectbox("Specialization",
                ["Cardiology", "Neurology", "Orthopedics", "General Practice", "Pediatrics", "Surgery"])
            experience = st.number_input("Years of Experience", min_value=0, max_value=60)
            qualification = st.text_input("Qualifications")
            department = st.text_input("Department")
            license_number = st.text_input("Medical License Number")
        
        availability = st.multiselect(
            "Available Days",
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        )
        
        if st.button("Save Doctor", use_container_width=True):
            if not username or not password or not full_name or not email:
                st.error("Please fill all required fields (Username, Password, Full Name, Email)")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters")
            else:
                hashed_pwd = hash_password(password)
                user_id = add_user(username, hashed_pwd, email, "Doctor", full_name, phone)
                if user_id:
                    # Save doctor record
                    doctor_id = add_doctor(user_id, specialization, experience, qualification, department)
                    if doctor_id:
                        st.success("✅ Doctor added successfully!")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error("Failed to add doctor record")
                else:
                    st.error("Username or email already exists")
