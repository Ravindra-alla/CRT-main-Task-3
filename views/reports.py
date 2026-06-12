import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import create_header

def show(user):
    """Reports page"""
    create_header("Reports", "View and Download Reports")
    
    if user['role'] == "Patient":
        show_patient_reports(user)
    elif user['role'] == "Doctor":
        show_doctor_reports(user)
    elif user['role'] == "Admin":
        show_admin_reports(user)

def show_patient_reports(user):
    """Patient reports"""
    st.subheader("📊 My Medical Reports")
    
    tab1, tab2, tab3 = st.tabs(["Lab Reports", "Test Reports", "Diagnostic Reports"])
    
    reports = pd.DataFrame({
        'Date': ['2024-01-15', '2024-01-10', '2024-01-05'],
        'Type': ['Blood Test', 'Glucose Test', 'ECG'],
        'Status': ['Completed', 'Completed', 'Pending'],
        'Result': ['Normal', 'High', 'N/A']
    })
    
    with tab1:
        st.dataframe(reports[reports['Type'].str.contains('Blood')], use_container_width=True)
    
    with tab2:
        st.dataframe(reports[reports['Type'].str.contains('Glucose')], use_container_width=True)
    
    with tab3:
        st.dataframe(reports[reports['Type'].str.contains('ECG')], use_container_width=True)
    
    st.divider()
    
    if st.button("📥 Download All Reports"):
        st.success("Reports downloaded successfully!")

def show_doctor_reports(user):
    """Doctor reports"""
    st.subheader("📊 Patient Reports")
    
    reports = pd.DataFrame({
        'Patient': ['John Doe', 'Jane Smith', 'Bob Wilson'],
        'Report Type': ['Lab Report', 'ECG', 'Blood Test'],
        'Date': ['2024-01-15', '2024-01-14', '2024-01-13'],
        'Status': ['Completed', 'Pending', 'Completed']
    })
    
    st.dataframe(reports, use_container_width=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Patient Statistics")
        stats = pd.DataFrame({
            'Metric': ['Total Patients', 'This Month', 'Reports Generated'],
            'Count': [45, 12, 156]
        })
        st.dataframe(stats, use_container_width=True)
    
    with col2:
        st.subheader("📊 Report Types Distribution")
        report_types = pd.DataFrame({
            'Type': ['Lab', 'ECG', 'Imaging', 'Other'],
            'Count': [45, 23, 18, 15]
        })
        fig = px.pie(report_types, values='Count', names='Type')
        st.plotly_chart(fig, use_container_width=True)

def show_admin_reports(user):
    """Admin reports"""
    st.subheader("📊 Hospital Reports")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Patients", "Resources", "Revenue", "Performance"])
    
    with tab1:
        st.write("**Patient Statistics**")
        patient_stats = pd.DataFrame({
            'Metric': ['Total Patients', 'New This Month', 'Active', 'Discharged'],
            'Count': [245, 32, 156, 89]
        })
        st.dataframe(patient_stats, use_container_width=True)
        
        fig = px.bar(patient_stats, x='Metric', y='Count')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.write("**Resource Utilization**")
        resources = pd.DataFrame({
            'Resource': ['Beds', 'Doctors', 'Equipment', 'Staff'],
            'Total': [200, 42, 150, 120],
            'In Use': [156, 35, 138, 110],
            'Available': [44, 7, 12, 10]
        })
        st.dataframe(resources, use_container_width=True)
    
    with tab3:
        st.write("**Revenue Report**")
        revenue = pd.DataFrame({
            'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
            'Revenue': [85000, 92000, 105000, 115000, 120000, 125000]
        })
        st.dataframe(revenue, use_container_width=True)
        
        fig = px.line(revenue, x='Month', y='Revenue', markers=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.write("**Performance Metrics**")
        performance = pd.DataFrame({
            'Department': ['Cardiology', 'Neurology', 'Orthopedics', 'General'],
            'Satisfaction': [4.8, 4.6, 4.7, 4.5],
            'Patient Count': [45, 38, 52, 110]
        })
        st.dataframe(performance, use_container_width=True)
