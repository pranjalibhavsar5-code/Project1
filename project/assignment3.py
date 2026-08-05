import streamlit as st
import pandas as pd
import os

# Excel file name
EXCEL_FILE = "data.xlsx"

# Function to load existing data or create a new DataFrame
def load_data():
    if os.path.exists(EXCEL_FILE):
        try:
            return pd.read_excel(EXCEL_FILE)
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")
            return pd.DataFrame(columns=["Name", "Age", "Course"])
    else:
        return pd.DataFrame(columns=["Name", "Age", "Course"])

# Function to save data to Excel
def save_data(df):
    try:
        df.to_excel(EXCEL_FILE, index=False)
    except Exception as e:
        st.error(f"Error saving Excel file: {e}")

# Streamlit app title
st.title("📋 Student Registration Form")

# Load existing data
data = load_data()

# Form for registration
with st.form("registration_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    course = st.selectbox("Course", ["Python", "Data Science", "Web Development", "AI/ML"])
    
    submitted = st.form_submit_button("Register")

    if submitted:
        if not name.strip():
            st.warning("Please enter a valid name.")
        else:
            # Append new data
            new_entry = pd.DataFrame({"Name": [name], "Age": [age], "Course": [course]})
            data = pd.concat([data, new_entry], ignore_index=True)
            save_data(data)
            st.success(f"✅ {name} has been registered successfully!")

# Display registered students
st.subheader("📄 Registered Students")
st.dataframe(data)
