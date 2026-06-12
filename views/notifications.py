import streamlit as st
from utils.styles import create_header

def show(user):
    """Notifications page"""
    create_header("Notifications", "Stay updated with your health information")
    
    st.subheader("🔔 Your Notifications")
    
    notifications = [
        {
            'type': 'Appointment',
            'title': 'Appointment Reminder',
            'message': 'Your appointment with Dr. Smith is tomorrow at 10:00 AM',
            'time': '1 hour ago',
            'read': False
        },
        {
            'type': 'Prescription',
            'title': 'Prescription Ready',
            'message': 'Your prescription is ready for pickup at the pharmacy',
            'time': '3 hours ago',
            'read': False
        },
        {
            'type': 'Report',
            'title': 'Lab Report Available',
            'message': 'Your lab report is now available in your health records',
            'time': '1 day ago',
            'read': True
        },
        {
            'type': 'Alert',
            'title': 'Medicine Reminder',
            'message': 'Remember to take your diabetes medication',
            'time': '2 days ago',
            'read': True
        },
        {
            'type': 'Alert',
            'title': 'Follow-up Appointment',
            'message': 'Schedule your follow-up appointment',
            'time': '3 days ago',
            'read': True
        }
    ]
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Recent Notifications**")
    with col2:
        if st.button("Clear All"):
            st.success("All notifications cleared!")
    
    st.divider()
    
    # Unread count
    unread_count = sum(1 for n in notifications if not n['read'])
    st.metric("Unread Notifications", unread_count)
    
    st.divider()
    
    for idx, notification in enumerate(notifications):
        col1, col2, col3 = st.columns([0.5, 3, 1])
        
        with col1:
            if not notification['read']:
                st.markdown("🔵")
            else:
                st.markdown("⚪")
        
        with col2:
            bg_color = "light" if notification['read'] else "white"
            st.write(f"**{notification['title']}**")
            st.write(f"{notification['message']}")
            st.caption(notification['time'])
        
        with col3:
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("✓", key=f"mark_read_{idx}"):
                    st.success("Marked as read")
            with col_b:
                if st.button("✕", key=f"delete_{idx}"):
                    st.info("Deleted")
        
        st.divider()
    
    st.divider()
    st.subheader("⚙️ Notification Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Email Notifications", value=True)
        st.checkbox("SMS Notifications", value=True)
        st.checkbox("Push Notifications", value=True)
    
    with col2:
        st.checkbox("Appointment Reminders", value=True)
        st.checkbox("Medicine Reminders", value=True)
        st.checkbox("Lab Report Alerts", value=True)
    
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")
