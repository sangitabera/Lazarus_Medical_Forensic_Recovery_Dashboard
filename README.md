# 🚑 Lazarus Dashboard
### Real-Time Patient Monitoring & Forensic Data Reconstruction System


# 📌 Overview

Lazarus Dashboard is an interactive healthcare analytics system built using Streamlit that simulates a real-world hospital environment where patient data has been partially corrupted.

The system reconstructs fragmented healthcare records, decodes encoded telemetry data, monitors patient vitals in real-time, detects anomalies, and generates downloadable reports through an interactive dashboard.


# 🎯 Project Objectives

- Reconstruct fragmented healthcare datasets
- Monitor patient vitals in real-time
- Detect abnormal conditions and trigger alerts
- Handle corrupted or inconsistent medical records
- Generate downloadable patient reports
- Build an interactive healthcare dashboard


# ✨ Features

## 📊 Interactive Dashboard
- Real-time monitoring dashboard using Streamlit
- Dynamic patient filtering
- Live visualization updates

## 📡 Vitals Monitoring
- Decode heart rate from hexadecimal values
- Display oxygen saturation (SpO2)
- Handle missing telemetry values using interpolation

## 🧠 Data Processing Pipeline
- Cleans inconsistent datasets
- Standardizes column names
- Handles corrupted and missing values

## 🔗 Forensic Data Reconstruction
- Rebuilds relationships between fragmented datasets
- Uses `ghost_id` as the primary linking key

## 🚨 Real-Time Alert System
- Detects abnormal heart rate values
- Displays blinking red critical alerts
- Highlights emergency patient conditions

## 💊 Medication Decoding
- Decodes scrambled medication data
- Displays processed medication information

## 📥 Downloadable Reports
- Export merged patient reports
- Combines demographics, telemetry, and medication data

## 🧬 Duplicate Patient Detection
- Detects potential duplicate patient records
- Uses heuristic matching logic

## ⚙️ Tech Stack
Category     Technology
Frontend     Streamlit
Backend          Python
Data Processing    Pandas, NumPy
Visualization     Plotly
Dataset Format    CSV

## 🔗 Dataset Architecture

### 👤 Patient Demographics
Contains:
internal_id,
ghost_id,
parity_group,
name,
age


### 📡 Telemetry Logs
Contains:
packet_id,
ghost_id,
room_id,
heart_rate_hex,
spO2

### 💊 Prescription Audit
Contains:
ghost_id,
med_scrambled,
decoded_med

### 🔄 Workflow
- Load raw datasets
- Normalize column names
- Decode hexadecimal heart rate values
- Handle missing SpO2 values
- Merge datasets using ghost_id
- Detect abnormal vitals
- Trigger critical alerts
- Generate interactive visualizations
- Export reports


### 🚨 Alert Logic
- Metric
- Condition
- Alert
- Heart Rate < 60 or > 100 (Critical)
- SpO2 < 90 (Critical)

## ▶️ Installation
Clone Repository
Bash
git clone https://github.com/your-username/lazarus-dashboard.git
cd lazarus-dashboard

Install Dependencies
Bash
pip install -r requirements.txt

Run Application
Bash
streamlit run app.py

## 📈 Use Cases
- Healthcare monitoring systems
- Medical telemetry analysis
- Data reconstruction systems
- Real-time dashboard applications
- Academic and portfolio projects

## 🧠 Concepts Used
- Data Cleaning
- Feature Engineering
- Data Merging
- Real-Time UI Rendering
- Alert Systems
- Duplicate Detection
- Modular Backend Design

## 🚀 Future Enhancements
- Machine Learning anomaly detection
- Real-time streaming integration
- Cloud deployment
- Multi-patient monitoring
- Advanced analytics dashboard


## 👩‍💻 Author
Sangita Bera
Aspiring Backend & Data Engineer

## ⭐ Support
If you found this project useful, consider giving it a star on GitHub ⭐
