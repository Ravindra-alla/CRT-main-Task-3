# AI-Powered Healthcare Prediction & Resource Management System

A comprehensive Streamlit-based healthcare platform featuring AI-powered disease prediction, patient management, resource optimization, and staff scheduling.


Live Demo link:-https://crt-main-task-3-1.onrender.com


## 🏥 Features

### 1. **Authentication & User Management**
- User registration/login with password encryption
- Role-based access control (Patient, Doctor, Admin, Staff)
- Profile management

### 2. **Patient Management**
- Patient registration and medical history
- Allergies and insurance information
- Personal health data management

### 3. **Doctor Management**
- Doctor profiles with specializations
- Availability scheduling
- Experience and qualifications tracking

### 4. **Appointment Scheduling**
- Online appointment booking
- Slot availability checking
- Appointment confirmation and rescheduling

### 5. **Electronic Health Records (EHR)**
- Centralized medical record storage
- Prescription history
- Vaccination records
- Diagnostic reports

### 6. **AI Disease Prediction**
- **Diabetes Risk Prediction** (Random Forest)
- **Heart Disease Risk Assessment** (Logistic Regression)
- **Kidney Disease Prediction** (Random Forest)
- **Cancer Risk Assessment**
- Risk scoring and severity classification

### 7. **Treatment Recommendation Engine**
- AI-based treatment suggestions
- Specialist recommendations
- Diagnostic test suggestions

### 8. **Patient Outcome Prediction**
- Recovery probability prediction
- ICU requirement assessment
- Hospitalization duration estimation
- Readmission risk prediction

### 9. **Bed Management System**
- Real-time bed availability tracking
- Ward allocation
- ICU bed management
- Emergency bed reservation

### 10. **Staff Scheduling Optimization**
- Doctor shift management
- Nurse allocation
- Peak load prediction
- Automatic schedule suggestions

### 11. **Resource Management**
- Equipment tracking and maintenance
- Supply inventory management
- Demand forecasting
- Cost optimization

### 12. **Analytics & Dashboards**
- Patient health dashboard
- Doctor dashboard
- Admin dashboard
- Staff dashboard
- Real-time metrics and KPIs

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** SQLite
- **ML Libraries:** scikit-learn, XGBoost
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Authentication:** bcrypt

## 📋 Requirements

```
streamlit==1.32.0
pandas==2.1.4
numpy==1.24.3
scikit-learn==1.3.2
xgboost==2.0.3
matplotlib==3.8.2
seaborn==0.13.0
plotly==5.18.0
bcrypt==4.1.2
python-dotenv==1.0.0
joblib==1.3.2
```

## 🚀 Installation & Setup

### 1. Clone or Download the Project
```bash
cd path/to/healthcare-system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## 👥 User Roles & Features

### **Patient**
- Dashboard with health metrics
- Book and manage appointments
- View health records
- Disease prediction assessment
- Medicine reminders
- Lab reports access

### **Doctor**
- Dashboard with patient list
- View appointments
- Manage treatment plans
- Access patient records
- Schedule management
- Performance reports

### **Admin**
- Patient management
- Doctor management
- Bed management
- Resource management
- Staff scheduling
- System analytics and reports

### **Staff**
- Dashboard
- Bed management
- Patient information
- Staff schedule

## 🔐 Default Test Credentials

The system initializes with the database on first run. You can create accounts through the registration page.

**Sample Credentials:**
- Username: `admin`
- Email: `admin@healthcare.com`
- Role: `Admin`

## 📊 ML Models Used

### Disease Prediction Models:
1. **Random Forest** - Diabetes & Kidney Disease prediction
2. **Logistic Regression** - Heart Disease & Cancer Risk
3. **Classification Models** - Patient outcome prediction

### Prediction Features:
- Age, BMI, Blood Glucose
- Cholesterol levels
- Blood pressure
- Heart rate
- Family history
- Smoking history

## 🏗️ Project Structure

```
healthcare-system/
├── app.py                      # Main application entry point
├── requirements.txt             # Project dependencies
├── healthcare_system.db        # SQLite database
├── utils/
│   ├── auth.py                # Authentication utilities
│   ├── database.py            # Database operations
│   ├── styles.py              # CSS and styling
│   └── __init__.py
├── models/
│   ├── predictors.py          # ML models
│   └── __init__.py
├── pages/
│   ├── dashboard.py           # Dashboard pages
│   ├── profile.py             # User profile
│   ├── appointment_booking.py # Appointment booking
│   ├── appointments.py        # View appointments
│   ├── health_records.py      # EHR module
│   ├── disease_prediction.py  # AI predictions
│   ├── reports.py             # Reports generation
│   ├── notifications.py       # Notifications
│   ├── patients_management.py # Patient management
│   ├── doctors_management.py  # Doctor management
│   ├── bed_management.py      # Bed tracking
│   ├── staff_scheduling.py    # Staff schedules
│   ├── resource_management.py # Resource tracking
│   ├── treatment_plans.py     # Treatment recommendations
│   ├── doctor_schedule.py     # Doctor schedule
│   ├── settings.py            # User settings
│   └── __init__.py
├── data/                       # Data storage
└── styles/                     # Additional CSS files
```

## 🎯 Key Features Implemented

✅ Complete Authentication System
✅ Multi-role Dashboard
✅ Patient Management Module
✅ Doctor Management Module
✅ Appointment Scheduling
✅ Electronic Health Records
✅ AI Disease Prediction
✅ Treatment Recommendations
✅ Patient Outcome Predictions
✅ Bed Management System
✅ Staff Scheduling
✅ Resource Management
✅ Analytics & Reports
✅ Notification System
✅ Settings & Profile Management

## 📈 Dashboard Features

### Patient Dashboard
- Health score and metrics
- Upcoming appointments
- Recent predictions
- Health trends visualization

### Doctor Dashboard
- Today's patients list
- Pending reports
- Appointment status
- Patient statistics

### Admin Dashboard
- Hospital statistics
- Resource utilization
- Patient growth trends
- Revenue tracking

### Staff Dashboard
- Bed status overview
- Shift information
- Ward utilization
- Patient tracking

## 🔍 AI Prediction Example

**Diabetes Prediction:**
```
Input: Age=45, BMI=28, Blood Glucose=140, BP=130, Family History=1
Output: Risk Score=78%, Severity=High
Recommendations: Intensive therapy, Daily monitoring, Dietary changes
```

## 💾 Database Schema

The application uses SQLite with the following main tables:
- `users` - User accounts and authentication
- `patients` - Patient information
- `doctors` - Doctor profiles
- `appointments` - Appointment records
- `ehr_records` - Electronic health records
- `predictions` - AI prediction results
- `beds` - Bed management
- `staff_schedule` - Staff schedules

## 🎨 UI/UX Features

- **Responsive Design** - Works on desktop and tablets
- **Custom CSS Styling** - Professional healthcare theme
- **Interactive Charts** - Plotly visualizations
- **Dark Mode Support** - Theme selection
- **Intuitive Navigation** - Left sidebar menu
- **Real-time Updates** - Dynamic data refresh

## 🔒 Security Features

- Password hashing with bcrypt
- Session management
- Role-based access control
- Data encryption
- SQL injection prevention
- CSRF protection

## 📱 Mobile Responsiveness

The application is designed to work on:
- Desktop browsers
- Tablets
- Mobile devices (optimized)

## 🚀 Future Enhancements

- [ ] Mobile app integration
- [ ] SMS/Email notifications
- [ ] Advanced reporting
- [ ] AI chatbot integration
- [ ] Video consultation
- [ ] Telemedicine features
- [ ] Integration with external APIs
- [ ] Machine learning model improvement

## 📞 Support & Contact

For issues or questions:
- Email: support@healthcare.com
- Documentation: See individual module docstrings
- Issues: Check the application logs

## 📄 License

This project is provided as-is for educational and healthcare purposes.

## 🙏 Acknowledgments

- Built with Streamlit for rapid development
- Uses scikit-learn for ML models
- Plotly for interactive visualizations
- Inspired by modern healthcare systems

---

**Happy Healthcare Innovation! 🏥**
