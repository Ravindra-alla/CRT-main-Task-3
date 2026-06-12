# 🏥 Installation & Setup Guide
## AI-Powered Healthcare Prediction & Resource Management System

---

## 📦 Prerequisites

Before starting, ensure you have:
- **Python 3.8+** installed ([Download here](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **~500MB** disk space for dependencies
- **Windows, Linux, or Mac** OS

---

## 🚀 Installation Steps

### **Step 1: Extract the Project**

#### Windows:
1. Right-click the `healthcare-system.zip` file
2. Select "Extract All"
3. Choose a location (e.g., `C:\Users\YourName\Desktop`)
4. Open the extracted folder

#### Linux/Mac:
```bash
tar -xzf healthcare-system.tar.gz
cd healthcare-system
```

---

### **Step 2: Run Setup (First Time Only)**

#### Windows:
1. **Double-click** `setup.bat` in the project folder
2. A command prompt will appear
3. Wait for all steps to complete
4. The script will show "Setup Successful!"

#### Linux/Mac:
```bash
chmod +x setup.sh
./setup.sh
```

**What the setup does:**
- ✅ Creates a virtual environment
- ✅ Installs all dependencies
- ✅ Configures the database
- ✅ Sets up the application

---

### **Step 3: Start the Application**

#### Windows:
**Double-click** `run.bat`

#### Linux/Mac:
```bash
chmod +x run.sh
./run.sh
```

**Expected output:**
```
You can now view your Streamlit app in your browser.
URL: http://localhost:8501
```

The browser will automatically open, or you can manually visit: **http://localhost:8501**

---

## 📝 Manual Setup (If Automated Scripts Don't Work)

### Windows:
```batch
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Linux/Mac:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

## 🧪 First Time Setup - Creating Test Accounts

1. **Launch the application** (following steps above)
2. **Register** tab is visible on the login page
3. **Create accounts** for testing:

### Test Account 1: Patient
- **Username:** `patient1`
- **Email:** `patient1@test.com`
- **Password:** `password123`
- **Full Name:** John Patient
- **Phone:** 555-1234
- **Role:** Patient

### Test Account 2: Doctor
- **Username:** `doctor1`
- **Email:** `doctor1@test.com`
- **Password:** `password123`
- **Full Name:** Dr. Smith
- **Phone:** 555-5678
- **Role:** Doctor

### Test Account 3: Admin
- **Username:** `admin1`
- **Email:** `admin1@test.com`
- **Password:** `password123`
- **Full Name:** Admin User
- **Phone:** 555-9999
- **Role:** Admin

---

## 🎯 Quick Navigation Guide

### **Sidebar Navigation** (Left side of screen)
- Different menu items based on your role
- Click any menu item to navigate
- Shows your name and role at the top
- Logout button at the bottom

### **Patient Menu:**
- 📊 Dashboard
- 👤 My Profile
- 📅 Book Appointment
- 📋 My Appointments
- 📄 Health Records
- 🔬 Disease Prediction
- 📊 My Reports
- 🔔 Notifications

### **Doctor Menu:**
- 📊 Dashboard
- 👤 My Profile
- 📅 Appointments
- 👥 Patients
- 💊 Treatment Plans
- ⏰ My Schedule
- 📊 Reports

### **Admin Menu:**
- 📊 Dashboard
- 👥 Patients
- 👨‍⚕️ Doctors
- 🛏️ Bed Management
- ⏰ Staff Scheduling
- 🔧 Resource Management
- 📊 Reports
- ⚙️ Settings

---

## ✨ Key Features to Try

### 1. **Disease Prediction** (Patient)
```
1. Click "Disease Prediction"
2. Select "Diabetes Prediction"
3. Enter sample values:
   - Age: 45
   - BMI: 28
   - Blood Glucose: 140
   - Blood Pressure: 130
   - Family History: Yes
4. Click "Predict Diabetes Risk"
5. View risk score and recommendations
```

### 2. **Book Appointment** (Patient)
```
1. Click "Book Appointment"
2. Select a doctor from the list
3. Choose a date and time slot
4. Add reason for visit
5. Click "Confirm Appointment"
```

### 3. **Manage Bed** (Admin)
```
1. Click "Bed Management"
2. View bed status by ward
3. Click "Allocate Bed" tab
4. Fill in patient and bed details
5. Click "Allocate Bed"
```

### 4. **View Dashboard** (Any Role)
```
1. Click "Dashboard" from sidebar
2. See role-specific metrics
3. View charts and statistics
4. Check recent activities
```

---

## 🔧 Troubleshooting

### **Issue: Command not found (Python)**
**Solution:**
1. Install Python from https://www.python.org/
2. During installation, **CHECK** "Add Python to PATH"
3. Restart your computer
4. Try again

### **Issue: Port 8501 already in use**
**Solution:**
```bash
# Use a different port
streamlit run app.py --server.port=8502
```

### **Issue: ModuleNotFoundError**
**Solution:**
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### **Issue: Database error**
**Solution:**
```bash
# Delete the database and reset
# Close the application first
# Delete: healthcare_system.db
# Restart the application
```

### **Issue: Application won't start**
**Solution:**
1. Delete `venv` folder
2. Delete `healthcare_system.db` file
3. Run `setup.bat` (Windows) or `setup.sh` (Linux/Mac) again
4. Run `run.bat` or `run.sh`

---

## 📊 Project Structure

```
healthcare-system/
├── app.py                    # Main application
├── requirements.txt          # Python dependencies
├── setup.bat / setup.sh      # Setup scripts
├── run.bat / run.sh          # Run scripts
├── config.py                 # Configuration
├── README.md                 # Full documentation
├── QUICKSTART.md             # Quick start guide
├── healthcare_system.db      # SQLite database (created on first run)
├── utils/                    # Utility modules
│   ├── auth.py              # Authentication
│   ├── database.py          # Database operations
│   └── styles.py            # UI styling
├── models/                   # ML Models
│   └── predictors.py        # Prediction models
└── pages/                    # Feature pages
    ├── dashboard.py
    ├── profile.py
    ├── appointments.py
    ├── disease_prediction.py
    ├── ... (15+ more pages)
```

---

## 🔐 Security & Privacy

- All passwords are encrypted with bcrypt
- Role-based access control
- Secure session management
- Data stored locally in SQLite
- No external data transmission (default setup)

---

## 📱 Browser Compatibility

✅ **Chrome** (Recommended)
✅ **Firefox**
✅ **Safari**
✅ **Edge**
✅ **Opera**

**Note:** For best experience, use Chrome on a desktop/laptop.

---

## ⚙️ System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 2GB | 4GB+ |
| Storage | 500MB | 1GB+ |
| CPU | 1GHz | 2GHz+ |
| Internet | Not required* | Broadband |
| OS | Windows 7+ / macOS 10.12+ / Ubuntu 16.04+ | Latest versions |

*Local operation only; some features may need internet.

---

## 📈 Performance Tips

1. **Close unnecessary applications** to free up RAM
2. **Use Chrome browser** for better performance
3. **Keep Python updated** for security and speed
4. **Regularly clear browser cache** if experiencing slowness
5. **Check disk space** - ensure 500MB free space

---

## 🔄 Regular Maintenance

### Weekly:
- Backup `healthcare_system.db` file
- Check application logs

### Monthly:
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Review and cleanup old data

### Quarterly:
- Update Python version
- Review security settings
- Optimize database

---

## 🆘 Getting Help

1. **Check logs:** Look for error messages in the console
2. **Review README.md:** Comprehensive documentation
3. **Check QUICKSTART.md:** For common tasks
4. **Google the error:** Most issues have solutions online
5. **Try fresh install:** Delete `venv` and `healthcare_system.db` and start over

---

## 📞 Support Resources

- **Official Documentation:** See README.md
- **Code Comments:** Check docstrings in Python files
- **Configuration:** Edit config.py for settings
- **Database:** SQLite (can view with DB Browser)

---

## ✅ Verification Checklist

After installation, verify:

- [ ] Python is installed (check: `python --version`)
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip list` shows all packages)
- [ ] Application starts without errors
- [ ] Browser opens to http://localhost:8501
- [ ] Can register a new account
- [ ] Can login with new account
- [ ] Dashboard displays correctly
- [ ] Navigation menu works

---

## 🎉 You're Ready!

Congratulations! Your AI-Powered Healthcare System is now running. 

**Start exploring:**
1. Create test accounts for different roles
2. Try the disease prediction feature
3. Explore the dashboards
4. Test appointment booking
5. Review the management modules

---

## 📚 Next Steps

1. **Read README.md** for detailed feature documentation
2. **Customize configuration** in config.py
3. **Explore the code** to understand the system
4. **Add sample data** for testing
5. **Deploy** to a web server (optional)

---

## 🚀 Happy Healthcare Innovation!

Thank you for using the AI-Powered Healthcare Prediction & Resource Management System!

**Version:** 1.0.0  
**Last Updated:** 2024-01-15  
**Status:** ✅ Production Ready

---

For more information, visit the project README or configuration files.
