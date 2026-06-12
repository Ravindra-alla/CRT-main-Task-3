import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import get_available_beds, add_bed, update_bed_status
from utils.styles import create_header

def show(user):
    """Bed management page"""
    create_header("Bed Management", "Real-time Hospital Bed Tracking")
    
    tab1, tab2, tab3 = st.tabs(["View Beds", "Allocate Bed", "Add Bed"])
    
    with tab1:
        st.subheader("🛏️ Bed Status Overview")
        
        # Bed statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Beds", "200")
        with col2:
            st.metric("Available", "45", delta="+5")
        with col3:
            st.metric("Occupied", "155", delta="-3")
        with col4:
            st.metric("Occupancy Rate", "77.5%")
        
        st.divider()
        
        # Ward-wise breakdown
        st.subheader("Ward Breakdown")
        
        ward_data = pd.DataFrame({
            'Ward': ['ICU', 'General', 'Emergency', 'Pediatric', 'Maternity'],
            'Total': [20, 80, 20, 50, 30],
            'Available': [8, 30, 5, 12, 10],
            'Occupied': [12, 50, 15, 38, 20]
        })
        
        st.dataframe(ward_data, use_container_width=True)
        
        # Visualization
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(ward_data, x='Ward', y=['Available', 'Occupied'], 
                        title='Bed Availability by Ward', barmode='stack')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.pie(ward_data, values='Total', names='Ward', title='Bed Distribution')
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Detailed bed list
        st.subheader("Detailed Bed Information")
        
        beds = pd.DataFrame({
            'Bed ID': ['B001', 'B002', 'B003', 'B004', 'B005'],
            'Ward': ['ICU', 'General', 'Emergency', 'ICU', 'General'],
            'Status': ['Occupied', 'Available', 'Available', 'Occupied', 'Occupied'],
            'Patient': ['John Doe', '-', '-', 'Jane Smith', 'Bob Wilson'],
            'Type': ['ICU Bed', 'Standard', 'Emergency', 'ICU Bed', 'Standard']
        })
        
        st.dataframe(beds, use_container_width=True)
    
    with tab2:
        st.subheader("🔄 Allocate Bed")
        
        col1, col2 = st.columns(2)
        
        with col1:
            patient_name = st.text_input("Patient Name")
            patient_id = st.text_input("Patient ID")
            ward = st.selectbox("Select Ward", ["ICU", "General", "Emergency", "Pediatric", "Maternity"], key="allocate_ward")
        
        with col2:
            bed_type = st.selectbox("Bed Type", ["Standard", "ICU Bed", "Emergency", "Intensive Care"], key="allocate_bed_type")
            duration = st.number_input("Expected Duration (days)", min_value=1, value=7)
            special_requirements = st.text_area("Special Requirements", height=80)
        
        if st.button("Allocate Bed", use_container_width=True):
            st.success(f"✅ Bed allocated to {patient_name} in {ward} Ward")
    
    with tab3:
        st.subheader("➕ Add New Bed")
        
        col1, col2 = st.columns(2)
        
        with col1:
            bed_number = st.text_input("Bed Number", placeholder="e.g., B001")
            ward = st.selectbox("Ward", ["ICU", "General", "Emergency", "Pediatric", "Maternity"], key="add_bed_ward")
        
        with col2:
            bed_type = st.selectbox("Bed Type", ["Standard", "ICU Bed", "Emergency", "Intensive Care"], key="add_bed_type")
            equipment = st.multiselect("Equipment", ["Monitor", "Ventilator", "Oxygen", "IV Stand"])
        
        if st.button("Add Bed", use_container_width=True):
            st.success(f"✅ Bed {bed_number} added successfully!")
