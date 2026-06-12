# Deployment Guide: Streamlit App on Render

This guide explains how to deploy the AI-Powered Healthcare Prediction & Resource Management System on **Render**.

We have added a blueprint configuration file ([render.yaml](file:///c:/Users/ALLA%20NAGA%20RAVINDRA/Desktop/crt-main%20task%20-3/render.yaml)) at the root of the project to automate the setup process.

---

## Option 1: Automatic Blueprint Deployment (Recommended)

1. Push your repository to your GitHub account.
2. Sign in to your [Render Dashboard](https://dashboard.render.com/).
3. Click **New** (top right) and select **Blueprint**.
4. Connect your GitHub repository.
5. Render will automatically detect the `render.yaml` file and parse the setup configuration.
6. Click **Approve** to deploy.

---

## Option 2: Manual Deployment

If you prefer to configure the deployment manually:

1. Click **New** (top right) and select **Web Service**.
2. Connect your GitHub repository.
3. Configure the following parameters in the Web Service setup screen:
   - **Language**: `Python`
   - **Build Command**: `pip install -r requirements.txt && python seed_test_data.py`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Expand the **Advanced** section to add the Python version environment variable:
   - **Key**: `PYTHON_VERSION`
   - **Value**: `3.10.12` (or your preferred Python version, e.g. `3.11.x`)
5. Click **Create Web Service**.

---

## Handling Persistent SQLite Storage (Critical)

By default, Render web services have an **ephemeral filesystem**, meaning any changes to the database file (registrations, bookings, predictions) will be **wiped** whenever the service restarts (e.g., during a redeployment or scaling event).

To persist your data permanently on Render:

### Step 1: Add a Persistent Disk on Render
1. Go to your Web Service dashboard in Render.
2. Click **Disks** in the sidebar.
3. Click **Add Disk** and set:
   - **Name**: `healthcare-db-disk`
   - **Mount Path**: `/data`
   - **Size**: `1 GiB` (more than enough for SQLite)
4. Click **Create Disk**.

### Step 2: Configure Environment Variable
Once the disk is mounted at `/data`, tell the application to store the SQLite database on this disk:
1. Go to **Environment** in the sidebar of your Web Service.
2. Add a new environment variable:
   - **Key**: `DB_PATH`
   - **Value**: `/data/healthcare_system.db`
3. Click **Save Changes**.

On the next deploy, the database will be created, seeded, and persisted permanently at `/data/healthcare_system.db` even across app restarts and updates!
