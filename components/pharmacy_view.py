import streamlit as st

def show_pharmacy(meds):
    st.subheader("💊 Pharmacy Portal")

    st.write("Scrambled vs Decrypted Meds")

    st.dataframe(meds[['scrambled_med', 'decoded_med']])