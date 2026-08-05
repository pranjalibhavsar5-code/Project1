import streamlit as st 

st.title("REGISTER PAGE")
name = st.text_input("Enter username ", placeholder=" enter here")
Password = st.text_input("Enter paassword", type="password", placeholder="Set password")
# roll_number = st.number_input("Enter Roll no", 1, 100)
# hsc_per=st.number_input("HSC parcentages", 0.0, 100.0)
col1, col2 =st.columns(2)
with col1:
    login = st.button("login")
with col2:
  register =st.button("register")
  if register:
       st.switch_page("PRANJALIHTML/student_register.py")