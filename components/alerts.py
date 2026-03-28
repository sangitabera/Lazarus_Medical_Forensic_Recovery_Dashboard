import streamlit as st
import time

def show_alerts(telemetry):
    st.subheader("🚨 Critical Triage Alerts")

    alert_placeholder = st.empty()

    latest_bpm = telemetry['bpm'].iloc[-1]

    if latest_bpm < 60 or latest_bpm > 100:
        for _ in range(6):  

            # RED alert ON
            alert_placeholder.markdown(
    f"""
    <style>
    @keyframes blink {{
        0% {{ background-color: red; }}
        50% {{ background-color: darkred; }}
        100% {{ background-color: red; }}
    }}
    .alert-box {{
        animation: blink 1s infinite;
        color: white;
        padding: 20px;
        font-size: 24px;
        text-align: center;
        border-radius: 10px;
        font-weight: bold;
    }}
    </style>

    <div class="alert-box">
        🚨 CRITICAL ALERT! BPM = {latest_bpm}
    </div>
    """,
    unsafe_allow_html=True
)
            time.sleep(0.5)

            alert_placeholder.markdown(
                """
                <div style="
                    background-color: #330000;
                    color: white;
                    padding: 20px;
                    font-size: 24px;
                    text-align: center;
                    border-radius: 10px;
                ">
                ⚠️ Monitoring...
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.5)

    else:
        alert_placeholder.success(f"✅ BPM Normal: {latest_bpm}")