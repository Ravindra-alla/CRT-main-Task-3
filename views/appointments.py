import streamlit as st
import pandas as pd
from utils.database import get_appointments, get_appointments_with_details, update_appointment_status
from utils.styles import create_header

def show(user):
    """View appointments"""
    create_header("Appointments", "Manage your appointments")
    
    if user['role'] == "Patient":
        show_patient_appointments(user)
    elif user['role'] == "Doctor":
        show_doctor_appointments(user)

def show_patient_appointments(user):
    """Patient appointments"""
    # Get appointments for patient
    appointments = get_appointments_with_details(patient_id=user['patient_id'])
    
    if not appointments.empty:
        # Create tabs for different statuses
        tab1, tab2, tab3 = st.tabs(["Upcoming", "Completed", "Cancelled"])
        
        with tab1:
            st.subheader("📅 Upcoming Appointments")
            upcoming = appointments[appointments['status'].isin(['Pending', 'Confirmed'])]
            if not upcoming.empty:
                for idx, appt in upcoming.iterrows():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"👨‍⚕️ **Doctor:** Dr. {appt['doctor_name']} ({appt['doctor_specialization']})")
                        st.write(f"📍 **Date:** {appt['appointment_date']} at {appt['appointment_time']}")
                        st.write(f"📝 **Notes:** {appt.get('notes', 'N/A')}")
                    with col2:
                        if st.button("🗑️ Cancel", key=f"cancel_{idx}"):
                            if update_appointment_status(appt['appointment_id'], 'Cancelled'):
                                st.success("Appointment cancelled successfully!")
                                st.rerun()
                    st.divider()
            else:
                st.info("No upcoming appointments")
        
        with tab2:
            st.subheader("✅ Completed Appointments")
            completed = appointments[appointments['status'] == 'Completed']
            if not completed.empty:
                st.dataframe(completed[['appointment_date', 'appointment_time', 'doctor_name', 'doctor_specialization', 'status']], use_container_width=True)
            else:
                st.info("No completed appointments")
        
        with tab3:
            st.subheader("❌ Cancelled Appointments")
            cancelled = appointments[appointments['status'] == 'Cancelled']
            if not cancelled.empty:
                st.dataframe(cancelled[['appointment_date', 'appointment_time', 'doctor_name', 'doctor_specialization', 'status']], use_container_width=True)
            else:
                st.info("No cancelled appointments")
    else:
        st.info("No appointments scheduled yet")
        if st.button("Book an Appointment"):
            st.session_state.page = "Book Appointment"
            st.rerun()

def show_doctor_appointments(user):
    """Doctor appointments"""
    st.subheader("📅 My Appointments")
    
    tab1, tab2 = st.tabs(["Today", "All"])
    
    # Get appointments for doctor
    appointments = get_appointments_with_details(doctor_id=user['doctor_id'])
    
    with tab1:
        st.write("**Today's Schedule**")
        from datetime import datetime
        today_str = datetime.now().strftime('%Y-%m-%d')
        if not appointments.empty:
            today_appts = appointments[appointments['appointment_date'] == today_str]
            if not today_appts.empty:
                for idx, appt in today_appts.iterrows():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"👤 **Patient:** {appt['patient_name']}")
                        st.write(f"⏰ **Time:** {appt['appointment_time']}")
                        st.write(f"📝 **Notes:** {appt.get('notes', 'N/A')}")
                        st.write(f"📊 **Status:** {appt['status']}")
                    with col2:
                        if appt['status'] in ['Pending', 'Confirmed']:
                            col_a, col_b = st.columns(2)
                            with col_a:
                                if st.button("✓ Complete", key=f"complete_{appt['appointment_id']}"):
                                    if update_appointment_status(appt['appointment_id'], 'Completed'):
                                        st.success("Appointment completed!")
                                        st.rerun()
                            with col_b:
                                if st.button("✕ Cancel", key=f"cancel_{appt['appointment_id']}"):
                                    if update_appointment_status(appt['appointment_id'], 'Cancelled'):
                                        st.success("Appointment cancelled!")
                                        st.rerun()
                    st.divider()
            else:
                st.info("No appointments scheduled for today.")
        else:
            st.info("No appointments scheduled for today.")
    
    with tab2:
        if not appointments.empty:
            st.dataframe(appointments[['appointment_date', 'appointment_time', 'patient_name', 'status', 'notes']], use_container_width=True)
        else:
            st.info("No appointments")
