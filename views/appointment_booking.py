import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.database import get_all_doctors, add_appointment
from utils.styles import create_header

def show(user):
    """Appointment booking page"""
    create_header("Book Appointment", "Schedule an appointment with a doctor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Select Doctor")
        
        # Get all doctors
        doctors = get_all_doctors()
        
        if not doctors.empty:
            selected_doctor_idx = st.selectbox("Choose Doctor", range(len(doctors)), 
                                             format_func=lambda x: f"Dr. {doctors.iloc[x]['full_name']} ({doctors.iloc[x]['specialization']})")
            
            selected_doctor = doctors.iloc[selected_doctor_idx]
            
            st.write(f"**Doctor Name:** Dr. {selected_doctor['full_name']}")
            st.write(f"**Specialization:** {selected_doctor['specialization']}")
            st.write(f"**Experience:** {selected_doctor['experience']} years")
            st.write(f"**Department:** {selected_doctor['department']}")
        else:
            st.warning("No doctors available")
            return
    
    with col2:
        st.subheader("📅 Select Date & Time")
        
        # Date selection
        min_date = datetime.now() + timedelta(days=1)
        max_date = datetime.now() + timedelta(days=30)
        appointment_date = st.date_input("Choose Date", value=min_date, min_value=min_date, max_value=max_date)
        
        # Time selection
        time_slots = [f"{h:02d}:00" for h in range(9, 18)]
        appointment_time = st.selectbox("Choose Time Slot", time_slots)
        
        # Reason for appointment
        reason = st.text_area("Reason for Appointment", height=80)
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col2:
        if st.button("✅ Confirm Appointment", use_container_width=True):
            if not doctors.empty:
                # Use current patient's patient_id
                patient_id = user.get('patient_id', 1)
                appointment_id = add_appointment(
                    patient_id=patient_id,
                    doctor_id=selected_doctor['doctor_id'],
                    appointment_date=str(appointment_date),
                    appointment_time=appointment_time,
                    notes=reason
                )
                if appointment_id:
                    st.success("✅ Appointment booked successfully!")
                    st.balloons()
                    st.info(f"""
                    **Appointment Details:**
                    - Doctor: Dr. {selected_doctor['full_name']} ({selected_doctor['specialization']})
                    - Date: {appointment_date}
                    - Time: {appointment_time}
                    - Confirmation ID: APT-{appointment_id:05d}
                    """)
    
    st.divider()
    st.subheader("💡 Tips for Your Appointment")
    st.write("""
    - Arrive 10 minutes early
    - Bring all relevant medical documents
    - Make a list of symptoms or concerns
    - Bring insurance card and ID
    """)
