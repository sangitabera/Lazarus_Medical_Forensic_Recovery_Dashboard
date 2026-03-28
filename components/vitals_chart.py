import time
import streamlit as st
import plotly.express as px

def show_vitals_chart(telemetry):
    st.subheader("📊 Vitals Monitor (Live)")

    chart_placeholder = st.empty()

    for i in range(1, len(telemetry) + 1):
        current_data = telemetry.iloc[:i]

        fig = px.line(
            current_data,
            x="packet_id",
            y="bpm",
            title="Decoded BPM Over Time"
        )

        chart_placeholder.plotly_chart(
            fig,
            use_container_width=True
        )

        time.sleep(1)