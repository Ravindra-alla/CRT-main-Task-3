import streamlit as st
import pandas as pd
from utils.styles import create_header

def show(user):
    """Doctor schedule page"""
    create_header("My Schedule", "Manage Your Work Schedule")
    
    tab1, tab2, tab3 = st.tabs(["This Week", "Availability", "Statistics"])
    
    with tab1:
        st.subheader("📅 Weekly Schedule")
        
        schedule_data = pd.DataFrame({
            'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'Shift': ['Morning', 'Evening', 'Morning', 'Evening', 'Morning', 'Day Off', 'Day Off'],
            'Start Time': ['6:00 AM', '2:00 PM', '6:00 AM', '2:00 PM', '6:00 AM', '-', '-'],
            'End Time': ['2:00 PM', '10:00 PM', '2:00 PM', '10:00 PM', '2:00 PM', '-', '-'],
            'Patients': [12, 10, 14, 11, 9, 0, 0],
            'Status': ['Confirmed', 'Confirmed', 'Confirmed', 'Confirmed', 'Confirmed', 'Off', 'Off']
        })
        
        st.dataframe(schedule_data, use_container_width=True)
        
        # Request change
        st.subheader("🔄 Request Schedule Change")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            from_date = st.date_input("From Date")
        
        with col2:
            to_date = st.date_input("To Date")
        
        with col3:
            change_type = st.selectbox("Change Type", ["Swap Shift", "Request Day Off", "Change Shift"])
        
        reason = st.text_area("Reason for Change", height=80)
        
        if st.button("Submit Request"):
            st.success("✅ Schedule change request submitted!")
    
    with tab2:
        st.subheader("⏰ Set Availability")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Working Days**")
            monday = st.checkbox("Monday", value=True)
            tuesday = st.checkbox("Tuesday", value=True)
            wednesday = st.checkbox("Wednesday", value=True)
            thursday = st.checkbox("Thursday", value=True)
            friday = st.checkbox("Friday", value=True)
            saturday = st.checkbox("Saturday", value=False)
            sunday = st.checkbox("Sunday", value=False)
        
        with col2:
            st.write("**Working Hours**")
            start_time = st.time_input("Start Time", value=None)
            end_time = st.time_input("End Time", value=None)
            
            st.write("**Preferred Shifts**")
            morning = st.checkbox("Morning (6AM-2PM)", value=True)
            evening = st.checkbox("Evening (2PM-10PM)", value=True)
            night = st.checkbox("Night (10PM-6AM)", value=False)
        
        if st.button("Update Availability"):
            st.success("✅ Availability updated successfully!")
    
    with tab3:
        st.subheader("📊 Schedule Statistics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Hours This Month", "160")
        with col2:
            st.metric("Days Off", "4")
        with col3:
            st.metric("Total Patients", "156")
        
        st.divider()
        
        # Monthly hours
        st.subheader("Monthly Hours Breakdown")
        
        monthly_data = pd.DataFrame({
            'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            'Hours': [40, 42, 38, 40],
            'Patients': [35, 42, 38, 41]
        })
        
        st.dataframe(monthly_data, use_container_width=True)
        
        import plotly.express as px
        
        fig = px.bar(monthly_data, x='Week', y='Hours', title='Weekly Hours')
        st.plotly_chart(fig, use_container_width=True)
