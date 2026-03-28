import streamlit as st

def download_report(patients, telemetry, meds):
    st.subheader("📥 Download Report")

    report = telemetry.merge(patients, on="ghost_id") \
                      .merge(meds, on="ghost_id")

    csv = report.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download Full Report",
        data=csv,
        file_name="lazarus_report.csv",
        mime="text/csv"
    )