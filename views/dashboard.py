import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils.database import get_all_patients, get_appointments, get_predictions, get_appointments_with_details
from utils.styles import create_metric_card, create_header

def show(user):
    """Dashboard page"""
    create_header("Dashboard", "Welcome to Healthcare Prediction System")
    
    if user['role'] == "Patient":
        show_patient_dashboard(user)
    elif user['role'] == "Doctor":
        show_doctor_dashboard(user)
    elif user['role'] == "Admin":
        show_admin_dashboard(user)
    elif user['role'] == "Staff":
        show_staff_dashboard(user)

def show_patient_dashboard(user):
    """Patient dashboard"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        create_metric_card("Health Score", "85%", "green")
    with col2:
        create_metric_card("Appointments", "3", "blue")
    with col3:
        create_metric_card("Risk Level", "Low", "orange")
    with col4:
        create_metric_card("Reports", "12", "purple")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Upcoming Appointments")
        appointments = get_appointments()
        if not appointments.empty:
            st.dataframe(appointments[['appointment_date', 'appointment_time', 'status']].head(), use_container_width=True)
        else:
            st.info("No appointments scheduled")
    
    with col2:
        st.subheader("🔬 Health Metrics")
        metrics_data = {
            "Blood Pressure": "120/80",
            "Heart Rate": "72 bpm",
            "Blood Sugar": "95 mg/dL",
            "Weight": "70 kg"
        }
        for metric, value in metrics_data.items():
            st.metric(metric, value)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Health Trends")
        fig = px.line(x=['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                      y=[85, 87, 86, 88],
                      markers=True,
                      title='Health Score Trend',
                      labels={'x': 'Week', 'y': 'Score'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("⚠️ Recent Predictions")
        predictions = get_predictions()
        if not predictions.empty:
            st.dataframe(predictions[['prediction_type', 'risk_score', 'severity_level']].head(5), use_container_width=True)
        else:
            st.info("No predictions yet")

def show_doctor_dashboard(user):
    """Doctor dashboard"""
    from datetime import datetime
    
    doctor_id = user.get('doctor_id')
    appointments = get_appointments_with_details(doctor_id=doctor_id) if doctor_id else pd.DataFrame()
    
    today_str = datetime.now().strftime('%Y-%m-%d')
    if not appointments.empty:
        today_appts = appointments[appointments['appointment_date'] == today_str]
        total_appts = len(appointments)
        today_count = len(today_appts)
        completed_count = len(appointments[appointments['status'] == 'Completed'])
    else:
        today_appts = pd.DataFrame()
        total_appts = 0
        today_count = 0
        completed_count = 0
        
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        create_metric_card("Patients Today", str(today_count), "blue")
    with col2:
        create_metric_card("Appointments", str(total_appts), "green")
    with col3:
        create_metric_card("Pending Reports", "5", "orange")
    with col4:
        create_metric_card("Consultations", str(completed_count), "purple")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👥 Today's Patients")
        if not today_appts.empty:
            patients_df = today_appts[['patient_name', 'appointment_time', 'status']].rename(
                columns={'patient_name': 'Patient', 'appointment_time': 'Time', 'status': 'Status'}
            )
            st.dataframe(patients_df, use_container_width=True)
        else:
            st.info("No appointments scheduled for today.")
    
    with col2:
        st.subheader("📋 Pending Reports")
        st.write("- ECG Report - Jane Smith")
        st.write("- Lab Test - John Doe")
        st.write("- MRI Report - Bob Wilson")
    
    st.divider()
    st.subheader("📊 Appointment Status")
    if not appointments.empty:
        status_counts = appointments['status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        fig = px.pie(status_counts, values='Count', names='Status', title='Appointment Status')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No appointments found to display status chart.")

def show_admin_dashboard(user):
    """Admin dashboard"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        create_metric_card("Total Patients", "245", "blue")
    with col2:
        create_metric_card("Total Doctors", "42", "green")
    with col3:
        create_metric_card("Bed Occupancy", "78%", "orange")
    with col4:
        create_metric_card("Revenue", "$125K", "purple")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏥 Hospital Statistics")
        stats = pd.DataFrame({
            'Metric': ['Patients', 'Doctors', 'Staff', 'Beds'],
            'Count': [245, 42, 120, 200]
        })
        st.dataframe(stats, use_container_width=True)
    
    with col2:
        st.subheader("📊 Resource Utilization")
        resources = pd.DataFrame({
            'Resource': ['Beds', 'Doctors', 'Equipment'],
            'Utilization %': [78, 85, 92]
        })
        fig = px.bar(resources, x='Resource', y='Utilization %', title='Resource Utilization')
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Patient Growth")
        fig = px.line(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                      y=[100, 120, 145, 180, 210, 245],
                      markers=True,
                      title='Monthly Patient Growth')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Revenue Trend")
        fig = px.line(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                      y=[85, 92, 105, 115, 120, 125],
                      markers=True,
                      title='Monthly Revenue (in $1000s)')
        st.plotly_chart(fig, use_container_width=True)

def show_staff_dashboard(user):
    """Staff dashboard"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        create_metric_card("Available Beds", "45", "green")
    with col2:
        create_metric_card("Occupied Beds", "155", "orange")
    with col3:
        create_metric_card("Emergency Beds", "10", "red")
    with col4:
        create_metric_card("Total Beds", "200", "blue")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛏️ Bed Status")
        bed_status = pd.DataFrame({
            'Ward': ['ICU', 'General', 'Emergency', 'Pediatric'],
            'Available': [8, 30, 5, 12],
            'Occupied': [12, 60, 10, 30]
        })
        st.dataframe(bed_status, use_container_width=True)
    
    with col2:
        st.subheader("⏰ Shift Information")
        st.write("Current Shift: Morning (6:00 AM - 2:00 PM)")
        st.write("Staff on Duty: 25 nurses, 8 doctors")
        st.write("Next Shift: Evening (2:00 PM - 10:00 PM)")
