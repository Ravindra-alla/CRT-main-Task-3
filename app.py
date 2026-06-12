import streamlit as st
import sys
import os
from datetime import datetime
from utils.auth import is_logged_in, get_current_user, login, register, logout, hash_password
from utils.database import init_database, get_user, add_user, get_or_create_patient, get_or_create_doctor
from utils.styles import load_custom_css, create_header

# Initialize database
init_database()

# Page configuration
st.set_page_config(
    page_title="Healthcare Prediction System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_custom_css()

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None

if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# Autologin from query parameters
if st.session_state.user is None and "username" in st.query_params:
    username = st.query_params["username"]
    user_record = get_user(username)
    if user_record:
        user = {
            'user_id': user_record[0],
            'username': user_record[1],
            'email': user_record[3],
            'role': user_record[4],
            'full_name': user_record[5],
            'phone': user_record[6]
        }
        if user['role'] == "Patient":
            user['patient_id'] = get_or_create_patient(user['user_id'])
        elif user['role'] == "Doctor":
            user['doctor_id'] = get_or_create_doctor(user['user_id'])
        st.session_state.user = user

def render_header():
    """Render main header"""
    st.markdown("""
    <div class="header">
        <h1>🏥 AI-Powered Healthcare Prediction & Resource Management</h1>
        <p>Intelligent healthcare platform for predictive analytics and resource optimization</p>
    </div>
    """, unsafe_allow_html=True)

def render_login_page():
    """Render login page"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="header" style="text-align: center;">
            <h1>🏥 Healthcare System</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # Login/Register Tabs
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            st.subheader("Login to Your Account")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login", use_container_width=True):
                user = login(username, password)
                if user:
                    if user['role'] == "Patient":
                        user['patient_id'] = get_or_create_patient(user['user_id'])
                    elif user['role'] == "Doctor":
                        user['doctor_id'] = get_or_create_doctor(user['user_id'])
                    st.session_state.user = user
                    st.query_params["username"] = user['username']
                    st.success(f"Welcome {user['full_name']}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        with tab2:
            st.subheader("Create New Account")
            reg_username = st.text_input("Username", key="reg_username")
            reg_email = st.text_input("Email", key="reg_email")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            reg_confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm_password")
            reg_full_name = st.text_input("Full Name", key="reg_full_name")
            reg_phone = st.text_input("Phone", key="reg_phone")
            reg_role = st.selectbox("Role", ["Patient", "Doctor", "Admin", "Staff"], key="reg_role")
            
            if st.button("Register", use_container_width=True):
                if not reg_username or not reg_email or not reg_password or not reg_full_name:
                    st.error("Please fill all required fields")
                elif reg_password != reg_confirm_password:
                    st.error("Passwords do not match")
                elif len(reg_password) < 6:
                    st.error("Password must be at least 6 characters")
                else:
                    try:
                        hashed_pwd = hash_password(reg_password)
                        user_id = add_user(reg_username, hashed_pwd, reg_email, reg_role, reg_full_name, reg_phone)
                        if user_id:
                            if reg_role == "Patient":
                                get_or_create_patient(user_id)
                            elif reg_role == "Doctor":
                                get_or_create_doctor(user_id)
                            st.success("Account created successfully! Please login.")
                        else:
                            st.error("Username or email already exists")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

def render_sidebar():
    """Render sidebar navigation"""
    with st.sidebar:
        st.markdown("### 🏥 Healthcare System")
        st.divider()
        
        if st.session_state.user:
            st.write(f"**Welcome, {st.session_state.user['full_name']}**")
            st.write(f"Role: {st.session_state.user['role']}")
            st.divider()
            
            # Navigation menu based on role
            role = st.session_state.user['role']
            
            pages = {
                "Patient": [
                    ("Dashboard", "📊"),
                    ("My Profile", "👤"),
                    ("Book Appointment", "📅"),
                    ("My Appointments", "📋"),
                    ("Health Records", "📄"),
                    ("Disease Prediction", "🔬"),
                    ("My Reports", "📊"),
                    ("Notifications", "🔔"),
                ],
                "Doctor": [
                    ("Dashboard", "📊"),
                    ("My Profile", "👤"),
                    ("Appointments", "📅"),
                    ("Patients", "👥"),
                    ("Treatment Plans", "💊"),
                    ("My Schedule", "⏰"),
                    ("Reports", "📊"),
                ],
                "Admin": [
                    ("Dashboard", "📊"),
                    ("Patients", "👥"),
                    ("Doctors", "👨‍⚕️"),
                    ("Bed Management", "🛏️"),
                    ("Staff Scheduling", "⏰"),
                    ("Resource Management", "🔧"),
                    ("Reports", "📊"),
                    ("Settings", "⚙️"),
                ],
                "Staff": [
                    ("Dashboard", "📊"),
                    ("Bed Management", "🛏️"),
                    ("Patients", "👥"),
                    ("Staff Schedule", "⏰"),
                ],
            }
            
            nav_pages = pages.get(role, pages["Patient"])
            
            for page_name, icon in nav_pages:
                if st.button(f"{icon} {page_name}", use_container_width=True, key=f"nav_{page_name}"):
                    st.session_state.page = page_name
                    st.rerun()
            
            st.divider()
            if st.button("🚪 Logout", use_container_width=True):
                logout()
        else:
            st.info("Please login to continue")

def render_main_content():
    """Render main content based on selected page"""
    page = st.session_state.page
    user_role = st.session_state.user['role'] if st.session_state.user else None
    
    # Import page modules dynamically
    if page == "Dashboard":
        from views.dashboard import show
        show(st.session_state.user)
    elif page == "My Profile" or page == "Profile":
        from views.profile import show
        show(st.session_state.user)
    elif page == "Book Appointment":
        from views.appointment_booking import show
        show(st.session_state.user)
    elif page == "My Appointments" or page == "Appointments":
        from views.appointments import show
        show(st.session_state.user)
    elif page == "Health Records":
        from views.health_records import show
        show(st.session_state.user)
    elif page == "Disease Prediction":
        from views.disease_prediction import show
        show(st.session_state.user)
    elif page == "My Reports" or page == "Reports":
        from views.reports import show
        show(st.session_state.user)
    elif page == "Notifications":
        from views.notifications import show
        show(st.session_state.user)
    elif page == "Patients":
        from views.patients_management import show
        show(st.session_state.user)
    elif page == "Doctors":
        from views.doctors_management import show
        show(st.session_state.user)
    elif page == "Bed Management":
        from views.bed_management import show
        show(st.session_state.user)
    elif page == "Staff Scheduling" or page == "Staff Schedule":
        from views.staff_scheduling import show
        show(st.session_state.user)
    elif page == "Resource Management":
        from views.resource_management import show
        show(st.session_state.user)
    elif page == "Treatment Plans":
        from views.treatment_plans import show
        show(st.session_state.user)
    elif page == "My Schedule":
        from views.doctor_schedule import show
        show(st.session_state.user)
    elif page == "Settings":
        from views.settings import show
        show(st.session_state.user)

# Main app logic
if not is_logged_in():
    render_login_page()
else:
    # Ensure role IDs are populated in session state
    user = st.session_state.user
    if user['role'] == "Patient" and 'patient_id' not in user:
        st.session_state.user['patient_id'] = get_or_create_patient(user['user_id'])
    elif user['role'] == "Doctor" and 'doctor_id' not in user:
        st.session_state.user['doctor_id'] = get_or_create_doctor(user['user_id'])
        
    render_sidebar()
    
    # Main content area
    if st.session_state.page:
        try:
            render_main_content()
        except ImportError as e:
            st.error(f"Page not found: {e}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
