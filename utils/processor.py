import pandas as pd
from utils.decoder import decode_name, decode_bpm, decode_med

def process_data(patients, telemetry, meds):

    # ✅ Decode names
    patients['decoded_name'] = patients['name'].apply(decode_name)

    # ✅ Ward using parity_group
    patients['ward'] = patients['parity_group'].apply(
        lambda x: "Ward A" if x % 2 == 0 else "Ward B"
    )

    # ✅ Decode BPM from heart_rate_hex
    telemetry['bpm'] = telemetry['heart_rate_hex'].apply(decode_bpm)

    # ✅ Interpolate oxygen (spO2)
    telemetry.columns = telemetry.columns.str.lower()
    telemetry['spo2'] = telemetry['spo2'].interpolate()

    # ✅ Decode meds
    meds['decoded_med'] = meds['scrambled_med'].apply(decode_med)

    return patients, telemetry, meds