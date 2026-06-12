import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import create_header

def show(user):
    """Resource management page"""
    create_header("Resource Management", "Optimize Hospital Resource Allocation")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Equipment", "Supplies", "Optimization"])
    
    with tab1:
        st.subheader("📊 Resource Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Beds Available", "45", delta="+5")
        with col2:
            st.metric("Ventilators", "15/20")
        with col3:
            st.metric("Oxygen Units", "30/35")
        with col4:
            st.metric("Medical Equipment", "142/150")
        
        st.divider()
        
        # Resource utilization
        st.subheader("📈 Resource Utilization")
        
        resources = pd.DataFrame({
            'Resource': ['Beds', 'Ventilators', 'Oxygen Units', 'ICU Equipment', 'Monitors'],
            'Total': [200, 20, 35, 50, 80],
            'In Use': [155, 15, 30, 42, 68],
            'Available': [45, 5, 5, 8, 12]
        })
        
        resources['Utilization %'] = (resources['In Use'] / resources['Total'] * 100).round(1)
        
        st.dataframe(resources, use_container_width=True)
        
        fig = px.bar(resources, x='Resource', y='Utilization %', title='Resource Utilization %')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("🔧 Medical Equipment Management")
        
        equipment_data = pd.DataFrame({
            'Equipment': ['Ventilators', 'ECG Monitors', 'Defibrillators', 'Oxygen Concentrators', 'Infusion Pumps'],
            'Total': [20, 40, 15, 35, 50],
            'Functional': [18, 38, 14, 32, 48],
            'Maintenance': [2, 2, 1, 3, 2],
            'Last Service': ['2024-01-05', '2024-01-08', '2024-01-10', '2024-01-03', '2024-01-07']
        })
        
        st.dataframe(equipment_data, use_container_width=True)
        
        st.subheader("🔧 Schedule Maintenance")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            equipment = st.selectbox("Select Equipment", equipment_data['Equipment'])
        
        with col2:
            maintenance_date = st.date_input("Maintenance Date")
        
        with col3:
            maintenance_type = st.selectbox("Type", ["Routine", "Repair", "Calibration"])
        
        if st.button("Schedule Maintenance"):
            st.success("✅ Maintenance scheduled successfully!")
    
    with tab3:
        st.subheader("📦 Medical Supplies")
        
        supplies_data = pd.DataFrame({
            'Supply': ['Syringes', 'Needles', 'IV Bags', 'Bandages', 'Gloves', 'Masks'],
            'Unit': ['box', 'box', 'box', 'box', 'box', 'box'],
            'Stock': [500, 450, 300, 600, 5000, 8000],
            'Min. Level': [200, 200, 100, 200, 2000, 3000],
            'Status': ['✅ OK', '✅ OK', '⚠️ Low', '✅ OK', '✅ OK', '✅ OK']
        })
        
        st.dataframe(supplies_data, use_container_width=True)
        
        st.subheader("📥 Order Supplies")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            supply = st.selectbox("Supply", supplies_data['Supply'])
        
        with col2:
            quantity = st.number_input("Quantity", min_value=1, value=100)
        
        with col3:
            supplier = st.text_input("Supplier")
        
        if st.button("Place Order"):
            st.success("✅ Order placed successfully!")
    
    with tab4:
        st.subheader("🤖 AI Resource Optimization")
        
        st.info("""
        **Optimization Recommendations:**
        
        1. **Peak Hours Detection:** 10 AM - 2 PM shows 85% utilization
        2. **Resource Allocation:** Increase nursing staff by 15% during peak hours
        3. **Equipment Efficiency:** Optimize equipment scheduling to improve availability
        4. **Cost Optimization:** Consolidate supply orders to reduce costs by 12%
        5. **Predictive Alerts:** System predicts high demand next Tuesday - prepare resources
        """)
        
        # Demand forecast
        st.subheader("📊 Demand Forecast")
        
        forecast_data = pd.DataFrame({
            'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'Predicted Patients': [45, 58, 52, 48, 42, 35, 30],
            'Beds Needed': [32, 42, 38, 35, 30, 25, 22]
        })
        
        fig = px.line(forecast_data, x='Day', y=['Predicted Patients', 'Beds Needed'], 
                     markers=True, title='7-Day Demand Forecast')
        st.plotly_chart(fig, use_container_width=True)
