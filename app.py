import streamlit as st

from utils.data_loader import load_data
from utils.processor import process_data
from components.patient_card import show_patient_cards
from components.vitals_chart import show_vitals_chart
from components.pharmacy_view import show_pharmacy
from components.alerts import show_alerts
from components.download_report import download_report

from utils.duplicate_detector import detect_duplicates
from components.duplicates_view import show_duplicates

st.set_page_config(page_title="Project Lazarus", layout="wide")

st.title("🧬 Project Lazarus Dashboard")

# Load data
patients, telemetry, meds = load_data()

# Process data
patients, telemetry, meds = process_data(patients, telemetry, meds)

# duplicate 
duplicates_df = detect_duplicates(patients)

# Sidebar filter
selected_patient = st.sidebar.selectbox(
    "Select Patient", patients['ghost_id']
)

# Filter data
telemetry_filtered = telemetry[telemetry['ghost_id'] == selected_patient]
meds_filtered = meds[meds['ghost_id'] == selected_patient]
patient_filtered = patients[patients['ghost_id'] == selected_patient]

# UI Sections
show_patient_cards(patient_filtered)
show_vitals_chart(telemetry_filtered)
show_pharmacy(meds_filtered)
show_alerts(telemetry_filtered)
download_report(patient_filtered, telemetry_filtered, meds_filtered)
show_duplicates(duplicates_df)