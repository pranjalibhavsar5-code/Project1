import streamlit as st 

st.title("REGISTER PAGE")
name = st.text_input("Enter username ", placeholder=" enter here")
Password = st.text_input("Enter paassword", type="password", placeholder="Set password")

login =st.button("Login")
register=st.button("Register")
