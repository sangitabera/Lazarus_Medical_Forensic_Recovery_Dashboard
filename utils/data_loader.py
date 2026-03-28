import pandas as pd

def load_data():
    patients = pd.read_csv("data/patient_demographics.csv")
    telemetry = pd.read_csv("data/telemetry_logs.csv")
    meds = pd.read_csv("data/prescription_audit.csv")

    return patients, telemetry, meds


