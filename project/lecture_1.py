import streamlit as st 

st.title("hello, Streamlit!")
name = st.text_input("Enter student name", placeholder=" enter here")
address = st.text_input("Enter ID", type="password")
roll_number = st.number_input("Enter Roll no", 1, 100)
hsc_per=st.number_input("HSC parcentages", 0.0, 100.0)
submit_button=st.button("submit")

if submit_button:
    st.write("data submited successfully!")
    if not name :
      st.error("Please enter name")
    else:
        st.write(f"Your name is {name}")