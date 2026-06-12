import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils.database import get_or_create_patient, get_or_create_doctor, get_all_doctors, add_appointment, get_appointments_with_details, add_user
from utils.auth import hash_password

def run_tests():
    print("Starting database integration tests...\n")
    
    # Clean up previous test state
    conn = sqlite3.connect('healthcare_system.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments")
    cursor.execute("DELETE FROM users WHERE username='test_patient_verify'")
    cursor.execute("DELETE FROM patients WHERE user_id NOT IN (SELECT user_id FROM users)")
    conn.commit()
    conn.close()
    
    username = "test_patient_verify"
    email = "verify@test.com"
    full_name = "Verification Patient"
    pwd = hash_password("testpwd123")
    
    # Check if user already exists
    conn = sqlite3.connect('healthcare_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username=?", (username,))
    res = cursor.fetchone()
    if res:
        user_id = res[0]
        print(f"Test user already exists with ID: {user_id}")
    else:
        user_id = add_user(username, pwd, email, "Patient", full_name, "111-222-3333")
        print(f"Created new test user with ID: {user_id}")
        
    # Get or create patient record
    patient_id = get_or_create_patient(user_id)
    print(f"Verified patient record exists. Patient ID: {patient_id}")
    assert patient_id is not None, "Patient ID should not be None"
    
    # 2. Test fetching doctors list with full name
    doctors = get_all_doctors()
    print(f"Verified doctors list contains {len(doctors)} doctors.")
    assert len(doctors) > 0, "There should be at least one doctor in the database."
    for idx, doc in doctors.iterrows():
        print(f"  - Doctor: Dr. {doc['full_name']} ({doc['specialization']}), Exper.: {doc['experience']} years")
        assert 'full_name' in doc, "full_name should be joined from users table"
        
    # Get a doctor to book with
    selected_doctor = doctors.iloc[0]
    doctor_id = selected_doctor['doctor_id']
    
    # 3. Test booking an appointment
    appt_id = add_appointment(
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_date="2026-06-20",
        appointment_time="10:00",
        notes="Automated verification test appointment"
    )
    print(f"Verified appointment booking. Appointment ID: {appt_id}")
    assert appt_id is not None, "Appointment ID should not be None"
    
    # 4. Test retrieving appointment details with joins
    appts = get_appointments_with_details(patient_id=patient_id)
    print(f"Verified retrieval of appointment details (found {len(appts)} appointments):")
    assert len(appts) > 0, "Should have retrieved at least one appointment details"
    
    for idx, appt in appts.iterrows():
        print(f"  - Appt ID: {appt['appointment_id']}")
        print(f"    Patient: {appt['patient_name']}")
        print(f"    Doctor: Dr. {appt['doctor_name']} ({appt['doctor_specialization']})")
        print(f"    Date/Time: {appt['appointment_date']} at {appt['appointment_time']}")
        print(f"    Status: {appt['status']}")
        print(f"    Notes: {appt['notes']}")
        
        # Assertions
        assert appt['patient_name'] == full_name, "Patient name should match the creator"
        assert appt['doctor_name'] == selected_doctor['full_name'], "Doctor name should match"
        
    conn.close()
    print("\nAll database integration tests passed successfully!")

if __name__ == "__main__":
    run_tests()
