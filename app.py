import streamlit as st
import pandas as pd

# 1. The Title & Subtitle
st.set_page_config(page_title="CSV Janitor", page_icon="🧹")
st.title("🧹 The CSV Janitor")
st.write("Upload your messy Real Estate data, and I will clean it instantly.")

# 2. File Uploader (The Drag & Drop)
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file)

    st.header("1. The Messy Data 🤢")
    st.write(df.head())  # Show first few rows

    # 3. The Sidebar Controls (User chooses how to clean)
    st.sidebar.header("Cleaning Options")

    # Option A: Drop Duplicates
    if st.sidebar.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()
        st.sidebar.success("Duplicates Removed!")

    # Option B: Fill Missing Values (The logic you learned)
    # We check numeric columns only
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if st.sidebar.checkbox("Fill Missing Numbers (with Average)"):
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
        st.sidebar.success("Missing Values Filled!")

    # 4. Show Clean Data
    st.header("2. The Clean Data ✨")
    st.write(df)

    # 5. Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Clean CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv",
    )