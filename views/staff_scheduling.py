import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import create_header

def show(user):
    """Staff scheduling page"""
    create_header("Staff Scheduling", "Optimize Hospital Staff Schedules")
    
    tab1, tab2, tab3 = st.tabs(["View Schedule", "Create Schedule", "Shift Management"])
    
    with tab1:
        st.subheader("📅 Current Staff Schedule")
        
        # Time period selection
        col1, col2 = st.columns(2)
        
        with col1:
            week_selector = st.date_input("Select Week")
        
        with col2:
            department_filter = st.selectbox("Department", ["All", "Doctors", "Nurses", "Staff"])
        
        # Schedule table
        schedule_data = pd.DataFrame({
            'Name': ['Dr. Smith', 'Dr. Johnson', 'Nurse A', 'Nurse B', 'Staff 1'],
            'Role': ['Doctor', 'Doctor', 'Nurse', 'Nurse', 'Staff'],
            'Monday': ['Morning', 'Evening', 'Night', 'Morning', 'Morning'],
            'Tuesday': ['Evening', 'Night', 'Morning', 'Evening', 'Morning'],
            'Wednesday': ['Night', 'Morning', 'Evening', 'Night', 'Off'],
            'Thursday': ['Morning', 'Evening', 'Off', 'Morning', 'Morning'],
            'Friday': ['Evening', 'Night', 'Morning', 'Evening', 'Evening'],
            'Saturday': ['Off', 'Morning', 'Evening', 'Off', 'Morning'],
            'Sunday': ['Morning', 'Off', 'Night', 'Morning', 'Off']
        })
        
        st.dataframe(schedule_data, use_container_width=True)
        
        # AI-powered insights
        st.subheader("🤖 AI Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("📊 **Predicted Peak Hours:** 10 AM - 2 PM, 6 PM - 8 PM")
        
        with col2:
            st.info("✅ **Recommended Staff:** +2 nurses during peak hours")
    
    with tab2:
        st.subheader("➕ Create New Schedule")
        
        col1, col2 = st.columns(2)
        
        with col1:
            staff_name = st.selectbox("Select Staff", ["Dr. Smith", "Dr. Johnson", "Nurse A", "Nurse B"])
            role = st.selectbox("Role", ["Doctor", "Nurse", "Staff", "Technician"])
            start_date = st.date_input("Start Date")
        
        with col2:
            end_date = st.date_input("End Date")
            shift_type = st.selectbox("Shift Type", ["Morning (6AM-2PM)", "Evening (2PM-10PM)", "Night (10PM-6AM)", "Day Off"])
        
        # Repeat pattern
        st.subheader("Repeat Pattern")
        
        repeat_type = st.radio("Repeat", ["No Repeat", "Weekly", "Monthly", "Custom"])
        
        if repeat_type == "Weekly":
            days = st.multiselect("Days", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        
        if st.button("Create Schedule", use_container_width=True):
            st.success("✅ Schedule created successfully!")
    
    with tab3:
        st.subheader("⏰ Shift Management")
        
        # Shift utilization
        shift_data = pd.DataFrame({
            'Shift': ['Morning', 'Evening', 'Night'],
            'Total Staff': [25, 22, 18],
            'Required': [20, 20, 15],
            'Utilization %': [125, 110, 120]
        })
        
        st.dataframe(shift_data, use_container_width=True)
        
        fig = px.bar(shift_data, x='Shift', y=['Total Staff', 'Required'], title='Shift Utilization')
        st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Staff workload analysis
        st.subheader("👥 Staff Workload Analysis")
        
        workload_data = pd.DataFrame({
            'Staff': ['Dr. Smith', 'Dr. Johnson', 'Nurse A', 'Nurse B', 'Staff 1'],
            'Hours This Week': [40, 38, 40, 36, 40],
            'Overtime': [0, 0, 0, 0, 0],
            'Days Off': [1, 1, 1, 2, 1]
        })
        
        st.dataframe(workload_data, use_container_width=True)
