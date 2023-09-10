import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
#reminder keys are like ids
    user_email = st.text_input("Your email address :")
    message = st.text_area("Your message :")
    button_submit = st.form_submit_button("Submit")
    print(button_submit)
#false if unpressed, true when pressed
#reminder to put print msgs to verify error, data
# and how to give good instructions in loops
    if button_submit:
        message = message + user_email
        print("i was pressed")