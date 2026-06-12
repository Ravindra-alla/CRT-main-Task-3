import streamlit as st
from utils.styles import create_header

def show(user):
    """Settings page"""
    create_header("Settings", "Manage System Settings")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Account", "Notifications", "Privacy", "System"])
    
    with tab1:
        st.subheader("🔐 Account Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Current Account**")
            st.write(f"Username: {user['username']}")
            st.write(f"Email: {user['email']}")
            st.write(f"Role: {user['role']}")
        
        with col2:
            st.write("**Security**")
            if st.button("Change Password"):
                with st.form("change_password_form"):
                    old_password = st.text_input("Old Password", type="password")
                    new_password = st.text_input("New Password", type="password")
                    confirm_password = st.text_input("Confirm Password", type="password")
                    
                    if st.form_submit_button("Update Password"):
                        if new_password == confirm_password:
                            st.success("✅ Password changed successfully!")
                        else:
                            st.error("Passwords do not match")
        
        st.divider()
        
        st.subheader("📧 Email & Contact")
        
        email = st.text_input("Email Address", value=user['email'])
        phone = st.text_input("Phone Number")
        
        if st.button("Update Contact Information"):
            st.success("✅ Contact information updated!")
    
    with tab2:
        st.subheader("🔔 Notification Preferences")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Notification Channels**")
            email_notif = st.checkbox("Email Notifications", value=True)
            sms_notif = st.checkbox("SMS Notifications", value=True)
            push_notif = st.checkbox("Push Notifications", value=True)
            whatsapp_notif = st.checkbox("WhatsApp Notifications", value=False)
        
        with col2:
            st.write("**Notification Types**")
            appointment_reminders = st.checkbox("Appointment Reminders", value=True)
            medicine_reminders = st.checkbox("Medicine Reminders", value=True)
            lab_alerts = st.checkbox("Lab Report Alerts", value=True)
            emergency_alerts = st.checkbox("Emergency Alerts", value=True)
            report_updates = st.checkbox("Report Updates", value=True)
        
        st.divider()
        
        st.write("**Notification Timing**")
        col1, col2 = st.columns(2)
        
        with col1:
            appointment_before = st.selectbox("Appointment Reminder (hours before)", [24, 12, 6, 3, 1])
        
        with col2:
            medicine_time = st.time_input("Daily Medicine Reminder Time", value=None)
        
        if st.button("Save Notification Settings"):
            st.success("✅ Notification settings saved!")
    
    with tab3:
        st.subheader("🔒 Privacy & Data")
        
        st.write("**Data Sharing**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            share_with_doctors = st.checkbox("Share medical data with doctors", value=True)
            share_with_family = st.checkbox("Share emergency data with family", value=True)
        
        with col2:
            research_participation = st.checkbox("Allow medical research use (anonymized)", value=False)
            analytics = st.checkbox("Enable usage analytics", value=True)
        
        st.divider()
        
        st.write("**Data Export & Deletion**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Download My Data"):
                st.success("✅ Preparing your data for download...")
        
        with col2:
            if st.button("🗑️ Delete Account"):
                st.warning("⚠️ This action cannot be undone. Please confirm in the dialog below.")
                if st.checkbox("I understand this action is permanent"):
                    if st.button("Confirm Delete"):
                        st.error("❌ Account deletion initiated")
    
    with tab4:
        st.subheader("⚙️ System Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Display**")
            theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
            language = st.selectbox("Language", ["English", "Spanish", "French", "German"])
            date_format = st.selectbox("Date Format", ["MM/DD/YYYY", "DD/MM/YYYY", "YYYY-MM-DD"])
        
        with col2:
            st.write("**Preferences**")
            timezone = st.selectbox("Timezone", ["EST", "CST", "MST", "PST", "UTC"])
            items_per_page = st.selectbox("Items Per Page", [10, 25, 50, 100])
            auto_logout = st.selectbox("Auto Logout (minutes)", [15, 30, 60, 120])
        
        st.divider()
        
        st.write("**Advanced Settings**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            enable_2fa = st.checkbox("Enable Two-Factor Authentication", value=False)
            session_timeout = st.checkbox("Enable Session Timeout", value=True)
        
        with col2:
            api_access = st.checkbox("Allow API Access", value=False)
            debug_mode = st.checkbox("Debug Mode", value=False)
        
        if st.button("Save System Settings"):
            st.success("✅ System settings saved!")
        
        st.divider()
        
        st.subheader("📋 About")
        st.write("""
        **AI-Powered Healthcare Prediction & Resource Management System**
        
        Version: 1.0.0
        Last Updated: 2024-01-15
        
        **Features:**
        - AI Disease Prediction
        - Treatment Recommendations
        - Patient Outcome Predictions
        - Resource Management
        - Staff Scheduling
        
        For support, contact: support@healthcare.com
        """)
