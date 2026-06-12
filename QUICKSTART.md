# Quick Start Guide - AI-Powered Healthcare System

## 🚀 Quick Start

### Windows Users

1. **Download and Extract the Project**
   - Extract the healthcare-system folder to your preferred location

2. **Run Setup (First Time Only)**
   ```
   Double-click: setup.bat
   ```
   This will:
   - Create a virtual environment
   - Install all dependencies
   - Configure the system

3. **Start the Application**
   ```
   Double-click: run.bat
   ```

### Linux/Mac Users

1. **Download and Extract the Project**
   ```bash
   tar -xzf healthcare-system.tar.gz
   cd healthcare-system
   ```

2. **Run Setup (First Time Only)**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Start the Application**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

## 🧪 Test Accounts

Use the registration page to create test accounts with different roles:

**Option 1: Create New Accounts**
- Navigate to the "Register" tab
- Fill in the required information
- Select your role (Patient, Doctor, Admin, Staff)
- Click Register

**Option 2: Sample Test Data**
- Patient: username=`patient1`, role=`Patient`
- Doctor: username=`doctor1`, role=`Doctor`
- Admin: username=`admin1`, role=`Admin`
- Staff: username=`staff1`, role=`Staff`

## 📋 Main Features to Explore

### For Patients
1. **Dashboard** - View health metrics and appointments
2. **Book Appointment** - Schedule with doctors
3. **Disease Prediction** - Get AI-powered health risk assessment
4. **Health Records** - Access your medical history
5. **My Reports** - View lab and diagnostic reports

### For Doctors
1. **Dashboard** - View today's patients
2. **Appointments** - Manage patient appointments
3. **Treatment Plans** - Create treatment recommendations
4. **My Schedule** - Manage work schedule

### For Admin
1. **Dashboard** - Hospital statistics
2. **Patient Management** - Add and manage patients
3. **Doctor Management** - Add and manage doctors
4. **Bed Management** - Track bed availability
5. **Staff Scheduling** - Optimize staff schedules
6. **Resource Management** - Manage hospital resources
7. **Reports** - Generate system reports

## 🔐 First Run Setup

1. **Application starts** → You'll see the login/registration page
2. **Create your account** → Fill in all required fields
3. **Select your role** → Choose from Patient, Doctor, Admin, or Staff
4. **Login** → Use your credentials to access the system
5. **Explore** → Navigate using the left sidebar menu

## 🎯 Common Tasks

### Book an Appointment (Patient)
1. Click "Book Appointment" in the sidebar
2. Select a doctor
3. Choose date and time slot
4. Add appointment reason
5. Confirm booking

### View Health Predictions (Patient)
1. Go to "Disease Prediction"
2. Select prediction type (Diabetes, Heart Disease, etc.)
3. Enter health metrics
4. Click "Predict"
5. View risk score and recommendations

### Manage Beds (Admin/Staff)
1. Navigate to "Bed Management"
2. View bed status by ward
3. Allocate beds to patients
4. Add new beds as needed

### Create Staff Schedule (Admin)
1. Go to "Staff Scheduling"
2. Select staff member
3. Choose shift type and dates
4. Set repeat pattern
5. Create schedule

## 🛠️ Troubleshooting

### Python Not Found
- Install Python 3.8+ from https://www.python.org/
- Make sure "Add Python to PATH" is checked during installation

### Port Already in Use
- The app uses port 8501
- If busy, use: `streamlit run app.py --server.port=8502`

### Database Issues
- Delete `healthcare_system.db` to reset
- Run app again to recreate database

### Missing Dependencies
- Delete `venv` folder
- Run `setup.bat` (Windows) or `setup.sh` (Linux/Mac) again

## 📊 Understanding the Dashboard

**Left Sidebar**
- Navigation menu based on your role
- Shows your name and role
- Logout button at bottom

**Main Area**
- Displays selected page content
- Contains forms, tables, and charts
- Interactive elements for user actions

## 💡 Tips

- Use the search features to find patients/doctors quickly
- Check notifications regularly for important alerts
- The AI predictions update in real-time
- Dashboard metrics refresh automatically

## 📞 Need Help?

1. Check the README.md for detailed documentation
2. Review module docstrings in the code
3. Check application logs for error details
4. Verify all dependencies are installed

## 🔄 Regular Maintenance

- Backup your database regularly
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Clear cache if experiencing issues
- Monitor application logs

---

**Enjoy using the Healthcare System! 🏥**
