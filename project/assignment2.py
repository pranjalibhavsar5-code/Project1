# interactive_app.py
import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Inter" \
    "active Streamlit App",
    page_icon="✨",
    layout="centered"
)

# App title
st.title("✨ Interactive Web Page with Streamlit")

# Section: User input
st.header("User Information")
name = st.text_input("Enter your name:", placeholder="Type here...")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Section: Selection
st.header("Preferences")
color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue", "Yellow"])
hobby = st.multiselect("Select your hobbies:", ["Reading", "Traveling", "Gaming", "Cooking", "Sports"])

# Section: Slider
st.header("Data Visualization")
num_points = st.slider("Number of random data points:", min_value=10, max_value=200, value=50)

# Generate random data
try:
    data = pd.DataFrame({
        'x': np.arange(num_points),
        'y': np.random.randn(num_points).cumsum()
    })
    st.line_chart(data.set_index('x'))
except Exception as e:
    st.error(f"Error generating chart: {e}")

# Display summary
if st.button("Show Summary"):
    if not name.strip():
        st.warning("Please enter your name.")
    else:
        st.success(f"Hello {name}! 🎉")
        st.write(f"**Age:** {age}")
        st.write(f"**Favorite Color:** {color}")
        st.write(f"**Hobbies:** {', '.join(hobby) if hobby else 'None selected'}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
