import streamlit as st

def show_duplicates(duplicates_df):
    st.subheader("🧬 Duplicate Patient Detection")

    if duplicates_df.empty:
        st.success("✅ No duplicate patients detected")
    else:
        st.error("Duplicate Patients Found!")

        st.dataframe(duplicates_df)

        st.write(f"🔍 Total Suspected Duplicates: {len(duplicates_df)}")