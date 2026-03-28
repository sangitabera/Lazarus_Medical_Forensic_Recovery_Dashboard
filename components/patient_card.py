import streamlit as st

def show_patient_cards(patients):
    st.subheader("🧑‍⚕️ Patient Identity Cards")

    for _, row in patients.iterrows():
        st.card = st.container()
        with st.card:
            st.write(f"Name: {row['decoded_name']}")
            st.write(f"Age: {row['age']}")
            st.write(f"Ward: {row['ward']}")