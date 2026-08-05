import streamlit as st 

st.title("TITLE PAGE")
st.header("Register Form")


name = st.text_input("Enter username ", placeholder=" enter here")
roll_no=st.number_input("Enter Roll Number: ",1, 100)
id = st.text_input("Enter Id: ", type="password", placeholder="Enter Id")
address=st.text_area("Enter Address: ",placeholder="Enter Address")
gender=st.radio("Choose Gender: ", ['Male', 'Female', 'Other'])
hobbies=st.selectbox("Select Hobbies: ", ['dancing', 'Riding', 'Singing'])
select=st.selectbox("Choose Your favorite food : ",['Maggi', 'Pav Vada', 'Pavbhaji'])
login =st.button("Submit the form")

if login:
    st.write("Form is submitted successfully!..")
