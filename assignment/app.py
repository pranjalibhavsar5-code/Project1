import streamlit as st
from new import add_student

st.title("REGISTER PAGE")
name = st.text_input("Enter username ", placeholder=" enter here")
roll = st.number_input("Enter roll", placeholder="Enter roll number")
# roll_number = st.number_input("Enter Roll no", 1, 100)
# hsc_per=st.number_input("HSC parcentages", 0.0, 100.0)
if st.button("submit"):
   add_student(name, roll)
   st.success("Student added")

# col1, col2 =st.columns(2)
# with col1:
#     login = st.button("login")
# with col2:
#   register =st.button("register")
#   if register:
      
#       st.switch_page("pages/register.py")