import streamlit as st 

st.header("HOSTEL REGISTRATION FORM")

st.subheader("👤 STUDENT DETAILS")
student_name = st.text_input("Student Name" , placeholder = "Enter your full name")
gender = st.selectbox("Gender" , ["Male","Female","Other"])
age = st.number_input("Age",1,100 , placeholder = "Enter your current age")
email_id = st.text_input("Email ID" , placeholder = "Enter your Email ID")
mob_number = st.text_input("Mobile Number" , placeholder = "Enter your Number" ,)

building=st.selectbox("Choose building",[ 'Old Building', 'New building'])
    

st.subheader("💳 Payment Details")

payment = st.selectbox("Payment Mode , if You Choose Online payment then QR is giver" , ["Offline","Online"])

if(payment == "Online"):
    st.image("Scanner.png" , width = 250)
    st.write("Scan the QR code to make the payment!")
    
col1 , col2 , col3 = st.columns(3)

with col1:
    Submit = st.button("Submit")
    
with col2:
    st.button("🔄 Clear Form")

with col3:
    st.button("❌ Application Cancelled!")
    
if Submit:
    st.success("✅ Your Hostel room is Confirmed!")
    
    st.subheader("📋 Student Details")

    st.write(f"Student Name :- {student_name}")
    st.write(f"Gender :- {gender}")
    st.write(f"Age :- {age}")
    st.write(f"Email ID :- {email_id}")
    st.write(f"Mobile Number :- {mob_number}")
    st.write(f"Building :- {building}")
    