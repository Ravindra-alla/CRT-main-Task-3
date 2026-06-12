import streamlit as st
import pandas as pd
from utils.database import get_ehr_records, add_ehr_record
from utils.styles import create_header

def show(user):
    """Health records page"""
    create_header("Health Records", "Electronic Health Record (EHR)")
    
    tab1, tab2 = st.tabs(["View Records", "Add Record"])
    
    with tab1:
        st.subheader("📄 Medical History")
        
        # Get EHR records
        records = get_ehr_records(patient_id=user['patient_id'])
        
        if not records.empty:
            # Create tabs for different record types
            record_types = records['record_type'].unique()
            
            for record_type in record_types:
                with st.expander(f"{record_type} Records"):
                    filtered_records = records[records['record_type'] == record_type]
                    for idx, record in filtered_records.iterrows():
                        st.write(f"**Date:** {record['created_at']}")
                        st.write(f"**Description:** {record['description']}")
                        if record['prescription']:
                            st.write(f"**Prescription:** {record['prescription']}")
                        st.divider()
        else:
            st.info("No health records found")
    
    with tab2:
        st.subheader("➕ Add New Record")
        
        col1, col2 = st.columns(2)
        
        with col1:
            record_type = st.selectbox(
                "Record Type",
                ["Prescription", "Lab Report", "Diagnostic Report", 
                 "Vaccination", "Surgery Report", "Other"]
            )
            description = st.text_area("Description", height=100)
        
        with col2:
            if record_type == "Prescription":
                prescription = st.text_area("Prescription Details", height=100)
            elif record_type == "Vaccination":
                vaccination = st.text_input("Vaccine Name")
                prescription = f"Vaccination: {vaccination}"
            else:
                prescription = ""
            
            diagnostic_reports = st.text_input("Attachment/File Name (if any)")
        
        if st.button("Add Record", use_container_width=True):
            record_id = add_ehr_record(
                patient_id=user['patient_id'],
                record_type=record_type,
                description=description,
                prescription=prescription,
                diagnostic_reports=diagnostic_reports
            )
            if record_id:
                st.success("✅ Record added successfully!")
            else:
                st.error("Failed to add record")
    
    st.divider()
    st.subheader("📊 Health Summary")
    
    summary_data = {
        'Metric': ['Total Records', 'Last Update', 'Vaccinations', 'Prescriptions'],
        'Value': ['45', 'Today', '12', '8']
    }
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
