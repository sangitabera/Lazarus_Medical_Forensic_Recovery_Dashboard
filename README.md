# 🚑 Lazarus Dashboard
Real-Time Patient Monitoring & Alert System (Streamlit + Python)


# 📌 Overview
Lazarus Dashboard is a real-time healthcare monitoring system designed to track patient vitals, detect anomalies, and generate actionable insights through an interactive dashboard.
This project simulates a hospital telemetry system, integrating patient demographics, real-time vitals, and medication data into a unified analytics pipeline.


# 🎯 Key Features

📡 Real-Time Telemetry Monitoring

Tracks heart rate & SpO2 continuously

Handles missing values using interpolation

# 🧠 Data Processing Pipeline

Cleans, transforms, and merges multiple datasets

Converts hex-encoded heart rate into readable format


# 🧾 Patient Demographics Integration

Links patients using ghost_id

Displays name, age, parity group, etc.


# 💊 Medication Decoding System

Processes scrambled medication data

Generates human-readable medication info


# 🚨 Real-Time Alert System

Detects abnormal vitals

Displays blinking red alerts in UI

# 📊 Interactive Dashboard (Streamlit)

Live data visualization

Filtering by patient / room


# 📥 Downloadable Reports

Merge patient + telemetry + meds

Export clean structured reports


# 🧩 Duplicate Patient Detection

Identifies anomalies in patient records


# 🏗️ Project Structure

lazarus_dashboard/
│
├── app.py                     # Main Streamlit app
│
├── components/
│   ├── pharmacy_view.py       # Medication display UI
│   └── download_report.py     # Report generation & export
│
├── utils/
│   └── processor.py           # Data processing pipeline
│
├── data/                      # (Optional) Input datasets
│
├── requirements.txt
└── README.md


# ⚙️ Tech Stack
Frontend/UI: Streamlit

Backend Logic: Python

Data Processing: Pandas, NumPy

Visualization: Streamlit Charts / Matplotlib

Data Handling: CSV / DataFrames

# 🔗 Data Architecture
Plain text

Patients Table
 ├── internal_id
 ├── ghost_id  🔑 (Primary linking key)
 ├── name, age, parity_group

Telemetry Logs
 ├── packet_id
 ├── ghost_id  🔑
 ├── room_id
 ├── heart_rate_hex
 ├── spO2

Medications
 ├── ghost_id  🔑
 ├── med_scrambled
 ├── decoded_med
 
👉 All datasets are linked using ghost_id


# 🔄 Data Processing Pipeline

Load raw datasets

Clean column names

Handle missing values (interpolation)

Convert:

heart_rate_hex → integer

Decode medications

Merge datasets using ghost_id

Detect anomalies

Render dashboard + alerts

# 🚨 Alert System Logic

Metric

Condition

Alert

Heart Rate

< 60 or > 100

🔴 Critical

SpO2

< 90
🔴 Critical

👉 Alerts are displayed using blinking red UI elements


# ▶️ Getting Started

1️⃣ Clone the Repository

git clone https://github.com/your-username/lazarus-dashboard.git

cd lazarus-dashboard

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the App

streamlit run app.py


# 📥 Report Generation
Merges:

Patient Data

Telemetry Data

Medication Data

Export Options:

CSV

Excel


# 🧠 Advanced Concepts Used

Data Normalization

Feature Engineering

Real-time UI simulation

Data merging strategies

Error handling (KeyErrors, missing columns)

Modular backend architecture


# 🛠️ Future Improvements

🔌 Live IoT integration (real sensors)

☁️ Cloud deployment (AWS / GCP)

🧠 ML-based anomaly detection

🔔 Push notifications (SMS / Email)

📊 Advanced analytics dashboard


# 💡 Learnings

Handling inconsistent schemas across datasets

Debugging real-world data pipeline errors

Designing scalable backend structure

Building interactive dashboards


# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repo and submit a pull request.


# 📜 License

This project is open-source and available under the MIT License.

# 👩‍💻 Author

Sangita Bera

🚀 Aspiring Backend Engineer |AI & ML Enthusiast


⭐ If you like this project
Give it a ⭐ on GitHub — it helps a lot!
