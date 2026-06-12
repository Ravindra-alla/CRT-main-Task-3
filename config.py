# Healthcare System Configuration

# Database settings
DATABASE_URL = "healthcare_system.db"
DATABASE_TIMEOUT = 5

# Application settings
APP_NAME = "AI-Powered Healthcare Prediction & Resource Management"
APP_VERSION = "1.0.0"
DEBUG_MODE = False

# Security settings
PASSWORD_MIN_LENGTH = 6
SESSION_TIMEOUT_MINUTES = 120
MAX_LOGIN_ATTEMPTS = 5

# Prediction models
USE_PRETRAINED_MODELS = False
MODEL_CONFIDENCE_THRESHOLD = 0.7

# Email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SEND_EMAIL_NOTIFICATIONS = False

# Notification settings
NOTIFICATION_ENABLED = True
NOTIFICATION_EMAIL_TEMPLATE = "template_email.html"
NOTIFICATION_SMS_ENABLED = False

# Feature flags
ENABLE_AI_CHATBOT = False
ENABLE_TELEMEDICINE = False
ENABLE_VIDEO_CONSULTATION = False
ENABLE_MOBILE_APP = False

# Data retention settings
DATA_RETENTION_DAYS = 2555  # ~7 years
BACKUP_FREQUENCY_HOURS = 24

# Performance settings
CACHE_TIMEOUT_SECONDS = 300
MAX_FILE_UPLOAD_SIZE_MB = 50

# ML Model settings
RANDOM_FOREST_N_ESTIMATORS = 100
LOGISTIC_REGRESSION_MAX_ITER = 1000
CROSS_VALIDATION_FOLDS = 5

# UI Settings
THEME = "light"  # light or dark
LANGUAGE = "en"  # en, es, fr, de
TIMEZONE = "UTC"

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/app.log"
