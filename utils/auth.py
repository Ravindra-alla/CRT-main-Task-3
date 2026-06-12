import bcrypt
import streamlit as st
from utils.database import get_user, add_user

def hash_password(password):
    """Hash a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    """Verify a password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def login(username, password):
    """Authenticate user"""
    user = get_user(username)
    if user and verify_password(password, user[2]):  # user[2] is password hash
        return {
            'user_id': user[0],
            'username': user[1],
            'email': user[3],
            'role': user[4],
            'full_name': user[5]
        }
    return None

def register(username, password, email, role, full_name, phone):
    """Register new user"""
    hashed_pwd = hash_password(password)
    user_id = add_user(username, hashed_pwd, email, role, full_name, phone)
    return user_id

def is_logged_in():
    """Check if user is logged in"""
    return 'user' in st.session_state and st.session_state.user is not None

def get_current_user():
    """Get current logged in user"""
    return st.session_state.get('user', None)

def logout():
    """Logout user"""
    if 'user' in st.session_state:
        del st.session_state.user
    st.query_params.clear()
    st.rerun()
