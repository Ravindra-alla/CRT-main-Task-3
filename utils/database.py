import sqlite3
import pandas as pd
from datetime import datetime
import os
import numpy as np

# Register adapters for numpy types so sqlite3 handles them correctly in raw SQL queries
try:
    sqlite3.register_adapter(np.int64, int)
    sqlite3.register_adapter(np.int32, int)
    sqlite3.register_adapter(np.float64, float)
    sqlite3.register_adapter(np.float32, float)
except Exception:
    pass

DB_PATH = "healthcare_system.db"

def init_database():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL,
            full_name TEXT,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Patients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            age INTEGER,
            gender TEXT,
            weight REAL,
            height REAL,
            blood_group TEXT,
            medical_conditions TEXT,
            family_history TEXT,
            allergies TEXT,
            insurance_id TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    # Doctors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            specialization TEXT,
            experience INTEGER,
            qualification TEXT,
            available_slots TEXT,
            department TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    # Appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            appointment_date TEXT,
            appointment_time TEXT,
            status TEXT DEFAULT 'Pending',
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
        )
    ''')
    
    # Electronic Health Records table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ehr_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            record_type TEXT,
            description TEXT,
            prescription TEXT,
            diagnostic_reports TEXT,
            vaccination_status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    ''')
    
    # Predictions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            prediction_type TEXT,
            disease_predicted TEXT,
            risk_score REAL,
            severity_level TEXT,
            model_used TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    ''')
    
    # Bed Management table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS beds (
            bed_id INTEGER PRIMARY KEY AUTOINCREMENT,
            bed_number TEXT UNIQUE,
            ward TEXT,
            status TEXT DEFAULT 'Available',
            patient_id INTEGER,
            bed_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Staff Schedule table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS staff_schedule (
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER NOT NULL,
            shift_date TEXT,
            shift_time TEXT,
            shift_type TEXT,
            status TEXT DEFAULT 'Scheduled',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
        )
    ''')
    
    conn.commit()
    conn.close()

def add_user(username, password, email, role, full_name, phone):
    """Add a new user"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, password, email, role, full_name, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password, email, role, full_name, phone))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except sqlite3.IntegrityError:
        return None

def get_user(username):
    """Get user by username"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def add_patient(user_id, age, gender, weight, height, blood_group, medical_conditions, family_history, allergies):
    """Add patient record"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (user_id, age, gender, weight, height, blood_group, 
        medical_conditions, family_history, allergies)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, age, gender, weight, height, blood_group, medical_conditions, family_history, allergies))
    conn.commit()
    patient_id = cursor.lastrowid
    conn.close()
    return patient_id

def get_patient(patient_id):
    """Get patient details"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_patients():
    """Get all patients with their user details"""
    conn = sqlite3.connect(DB_PATH)
    query = '''
        SELECT p.*, u.full_name, u.email, u.phone 
        FROM patients p 
        JOIN users u ON p.user_id = u.user_id
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def add_appointment(patient_id, doctor_id, appointment_date, appointment_time, notes=""):
    """Add new appointment"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (int(patient_id), int(doctor_id), appointment_date, appointment_time, notes))
    conn.commit()
    appointment_id = cursor.lastrowid
    conn.close()
    return appointment_id

def get_appointments(patient_id=None):
    """Get appointments"""
    conn = sqlite3.connect(DB_PATH)
    if patient_id:
        df = pd.read_sql_query('SELECT * FROM appointments WHERE patient_id = ?', 
                              conn, params=(patient_id,))
    else:
        df = pd.read_sql_query('SELECT * FROM appointments', conn)
    conn.close()
    return df

def add_prediction(patient_id, prediction_type, disease_predicted, risk_score, severity_level, model_used):
    """Add prediction record"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO predictions (patient_id, prediction_type, disease_predicted, risk_score, 
        severity_level, model_used)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (patient_id, prediction_type, disease_predicted, risk_score, severity_level, model_used))
    conn.commit()
    prediction_id = cursor.lastrowid
    conn.close()
    return prediction_id

def get_predictions(patient_id=None):
    """Get predictions"""
    conn = sqlite3.connect(DB_PATH)
    if patient_id:
        df = pd.read_sql_query('SELECT * FROM predictions WHERE patient_id = ?', 
                              conn, params=(patient_id,))
    else:
        df = pd.read_sql_query('SELECT * FROM predictions', conn)
    conn.close()
    return df

def add_ehr_record(patient_id, record_type, description, prescription="", diagnostic_reports="", vaccination_status=""):
    """Add EHR record"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ehr_records (patient_id, record_type, description, prescription, 
        diagnostic_reports, vaccination_status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (patient_id, record_type, description, prescription, diagnostic_reports, vaccination_status))
    conn.commit()
    record_id = cursor.lastrowid
    conn.close()
    return record_id

def get_ehr_records(patient_id):
    """Get EHR records for patient"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query('SELECT * FROM ehr_records WHERE patient_id = ?', 
                           conn, params=(patient_id,))
    conn.close()
    return df

def add_bed(bed_number, ward, bed_type="Standard"):
    """Add bed to system"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO beds (bed_number, ward, bed_type, status)
            VALUES (?, ?, ?, ?)
        ''', (bed_number, ward, bed_type, "Available"))
        conn.commit()
        bed_id = cursor.lastrowid
        conn.close()
        return bed_id
    except sqlite3.IntegrityError:
        return None

def get_available_beds():
    """Get all available beds"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query('SELECT * FROM beds WHERE status = "Available"', conn)
    conn.close()
    return df

def update_bed_status(bed_id, status, patient_id=None):
    """Update bed status"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if patient_id:
        cursor.execute('UPDATE beds SET status = ?, patient_id = ? WHERE bed_id = ?', 
                      (status, patient_id, bed_id))
    else:
        cursor.execute('UPDATE beds SET status = ? WHERE bed_id = ?', (status, bed_id))
    conn.commit()
    conn.close()

def add_doctor(user_id, specialization, experience, qualification, department):
    """Add doctor record"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO doctors (user_id, specialization, experience, qualification, department)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, specialization, experience, qualification, department))
    conn.commit()
    doctor_id = cursor.lastrowid
    conn.close()
    return doctor_id

def get_all_doctors():
    """Get all doctors with their user details"""
    conn = sqlite3.connect(DB_PATH)
    query = '''
        SELECT d.*, u.full_name, u.email, u.phone 
        FROM doctors d 
        JOIN users u ON d.user_id = u.user_id
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_doctor(doctor_id):
    """Get doctor details"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doctors WHERE doctor_id = ?', (doctor_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_doctor_by_user_id(user_id):
    """Get doctor details by user_id"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doctors WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_patient_by_user_id(user_id):
    """Get patient details by user_id"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_or_create_patient(user_id):
    """Get patient_id for a user_id, create it if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT patient_id FROM patients WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result:
        patient_id = result[0]
    else:
        # Create a new patient record with defaults
        cursor.execute('''
            INSERT INTO patients (user_id, age, gender, weight, height, blood_group, 
            medical_conditions, family_history, allergies, insurance_id)
            VALUES (?, 30, 'Male', 70.0, 170.0, 'O+', '', '', '', '')
        ''', (user_id,))
        conn.commit()
        patient_id = cursor.lastrowid
    conn.close()
    return patient_id

def get_or_create_doctor(user_id):
    """Get doctor_id for a user_id, create it if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT doctor_id FROM doctors WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result:
        doctor_id = result[0]
    else:
        # Create a new doctor record with defaults
        cursor.execute('''
            INSERT INTO doctors (user_id, specialization, experience, qualification, available_slots, department)
            VALUES (?, 'General Practice', 5, 'MD', 'Monday, Tuesday, Wednesday, Thursday, Friday', 'General')
        ''', (user_id,))
        conn.commit()
        doctor_id = cursor.lastrowid
    conn.close()
    return doctor_id

def update_patient(patient_id, age, gender, weight, height, blood_group, medical_conditions, family_history, allergies, insurance_id):
    """Update patient details"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE patients 
        SET age = ?, gender = ?, weight = ?, height = ?, blood_group = ?, 
            medical_conditions = ?, family_history = ?, allergies = ?, insurance_id = ?
        WHERE patient_id = ?
    ''', (age, gender, weight, height, blood_group, medical_conditions, family_history, allergies, insurance_id, patient_id))
    conn.commit()
    conn.close()
    return True

def update_doctor(doctor_id, specialization, experience, qualification, department, available_slots):
    """Update doctor details"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE doctors 
        SET specialization = ?, experience = ?, qualification = ?, department = ?, available_slots = ?
        WHERE doctor_id = ?
    ''', (specialization, experience, qualification, department, available_slots, doctor_id))
    conn.commit()
    conn.close()
    return True

def update_appointment_status(appointment_id, status):
    """Update appointment status"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE appointments SET status = ? WHERE appointment_id = ?', (status, appointment_id))
    conn.commit()
    conn.close()
    return True

def get_appointments_with_details(patient_id=None, doctor_id=None):
    """Get appointments with patient and doctor names"""
    conn = sqlite3.connect(DB_PATH)
    query = '''
        SELECT 
            a.appointment_id, 
            a.patient_id, 
            a.doctor_id, 
            a.appointment_date, 
            a.appointment_time, 
            a.status, 
            a.notes, 
            a.created_at,
            up.full_name as patient_name,
            ud.full_name as doctor_name,
            d.specialization as doctor_specialization
        FROM appointments a
        LEFT JOIN patients p ON a.patient_id = p.patient_id
        LEFT JOIN users up ON p.user_id = up.user_id
        LEFT JOIN doctors d ON a.doctor_id = d.doctor_id
        LEFT JOIN users ud ON d.user_id = ud.user_id
    '''
    params = []
    conditions = []
    if patient_id:
        conditions.append("a.patient_id = ?")
        params.append(patient_id)
    if doctor_id:
        conditions.append("a.doctor_id = ?")
        params.append(doctor_id)
        
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
        
    query += " ORDER BY a.appointment_date DESC, a.appointment_time DESC"
    
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df
