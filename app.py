import streamlit as st

# Title
st.title("Student Marks Form")

# Form UI
with st.form("marks_form"):
    regno = st.text_input("Registration Number")
    name = st.text_input("Name")
    standard = st.text_input("Class")
    math = st.number_input("Math Marks", min_value=0, max_value=100)
    science = st.number_input("Science Marks", min_value=0, max_value=100)
    computer = st.number_input("Computer Marks", min_value=0, max_value=100)
    
    submitted = st.form_submit_button("Submit")

# Action on Submit
if submitted:
    st.success("Form submitted successfully!")
    st.write("### Student Data:")
    st.write(f"**Reg No:** {regno}")
    st.write(f"**Name:** {name}")
    st.write(f"**Class:** {standard}")
    st.write(f"**Math:** {math}")
    st.write(f"**Science:** {science}")
    st.write(f"**Computer:** {computer}")
    print(regno, name, standard, math, science, computer)  # Optional for debugging
