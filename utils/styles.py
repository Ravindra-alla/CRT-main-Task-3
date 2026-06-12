import streamlit as st

def load_custom_css():
    """Load custom CSS styling"""
    css = """
    <style>
        /* Main Container */
        .main {
            background-color: #f0f8ff;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #1e3a5f;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
            color: white;
        }
        
        /* Header Styling */
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .header h1 {
            margin: 0;
            font-size: 32px;
            font-weight: bold;
        }
        
        /* Card Styling */
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin: 10px 0;
            border-left: 4px solid #667eea;
        }
        
        .card h3 {
            color: #1e3a5f;
            margin-top: 0;
        }
        
        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 10px 0;
        }
        
        .metric-card .value {
            font-size: 32px;
            font-weight: bold;
        }
        
        .metric-card .label {
            font-size: 14px;
            opacity: 0.9;
        }
        
        /* Button Styling */
        .stButton > button {
            background-color: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .stButton > button:hover {
            background-color: #764ba2;
        }
        
        /* Input Styling */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            padding: 10px;
        }
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }
        
        /* Table Styling */
        .dataframe {
            font-size: 12px;
        }
        
        .dataframe thead {
            background-color: #667eea;
            color: white;
        }
        
        .dataframe tbody tr:hover {
            background-color: #f0f0f0;
        }
        
        /* Alert Styling */
        .alert-success {
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #28a745;
        }
        
        .alert-danger {
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #f5c6cb;
        }
        
        .alert-warning {
            background-color: #fff3cd;
            color: #856404;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #ffc107;
        }
        
        .alert-info {
            background-color: #d1ecf1;
            color: #0c5460;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #17a2b8;
        }
        
        /* Stats Container */
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        
        /* Sidebar Links */
        .sidebar-item {
            color: white;
            padding: 12px 20px;
            margin: 5px 0;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .sidebar-item:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        .sidebar-item.active {
            background-color: #667eea;
            font-weight: bold;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 24px;
            }
            
            .metric-card .value {
                font-size: 24px;
            }
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def create_header(title, subtitle=""):
    """Create a styled header"""
    html = f"""
    <div class="header">
        <h1>{title}</h1>
        {f'<p>{subtitle}</p>' if subtitle else ''}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def create_card(title, content):
    """Create a styled card"""
    html = f"""
    <div class="card">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def create_metric_card(label, value, color="blue"):
    """Create a styled metric card"""
    colors = {
        "blue": "#667eea",
        "purple": "#764ba2",
        "green": "#28a745",
        "red": "#dc3545",
        "orange": "#fd7e14"
    }
    color_code = colors.get(color, "#667eea")
    
    html = f"""
    <div style="background: linear-gradient(135deg, {color_code} 0%, rgba(0,0,0,0.1) 100%); 
                color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 10px 0;">
        <div style="font-size: 32px; font-weight: bold;">{value}</div>
        <div style="font-size: 14px; opacity: 0.9;">{label}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def create_alert(message, alert_type="info"):
    """Create a styled alert"""
    class_name = f"alert-{alert_type}"
    html = f'<div class="{class_name}">{message}</div>'
    st.markdown(html, unsafe_allow_html=True)
