import sqlite3
import sys
import os

# Add current directory to python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils.database import get_or_create_patient, get_or_create_doctor, add_user, update_doctor, DB_PATH
from utils.auth import hash_password

def seed():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Sync all existing patients
    cursor.execute("SELECT user_id, full_name FROM users WHERE role='Patient'")
    patient_users = cursor.fetchall()
    print("Syncing patient IDs:")
    for user_id, name in patient_users:
        p_id = get_or_create_patient(user_id)
        print(f"  - Patient: {name} (User ID: {user_id}, Patient ID: {p_id})")
        
    # 2. Add some seed doctors if not already present
    doctors_data = [
        {
            "username": "dr_smith",
            "password": "doctor123",
            "email": "john.smith@hospital.com",
            "full_name": "John Smith",
            "phone": "555-0101",
            "specialization": "Cardiology",
            "experience": 15,
            "qualification": "MD, FACC",
            "department": "Cardiology"
        },
        {
            "username": "dr_jones",
            "password": "doctor123",
            "email": "sarah.jones@hospital.com",
            "full_name": "Sarah Jones",
            "phone": "555-0102",
            "specialization": "Neurology",
            "experience": 12,
            "qualification": "MD, PhD",
            "department": "Neurology"
        },
        {
            "username": "dr_davis",
            "password": "doctor123",
            "email": "robert.davis@hospital.com",
            "full_name": "Robert Davis",
            "phone": "555-0103",
            "specialization": "General Practice",
            "experience": 8,
            "qualification": "MD",
            "department": "General Medicine"
        }
    ]
    
    print("\nSyncing doctors:")
    for doc in doctors_data:
        cursor.execute("SELECT user_id FROM users WHERE username=?", (doc["username"],))
        exists = cursor.fetchone()
        if exists:
            user_id = exists[0]
            print(f"  - Doctor user {doc['username']} already exists (User ID: {user_id})")
        else:
            hashed_pwd = hash_password(doc["password"])
            user_id = add_user(
                doc["username"], 
                hashed_pwd, 
                doc["email"], 
                "Doctor", 
                doc["full_name"], 
                doc["phone"]
            )
            print(f"  - Created doctor user {doc['username']} (User ID: {user_id})")
            
        doc_id = get_or_create_doctor(user_id)
        update_doctor(doc_id, doc["specialization"], doc["experience"], doc["qualification"], doc["department"], "Monday,Tuesday,Wednesday,Thursday,Friday")
        print(f"    Doctor ID: {doc_id}, Specialization: {doc['specialization']}")
        
    conn.commit()
    conn.close()
    print("\nDatabase seeding completed successfully!")

if __name__ == "__main__":
    seed()
