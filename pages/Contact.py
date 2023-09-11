import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
#reminder keys are like ids
    user_email = st.text_input("Your email address :")
    raw_message = st.text_area("Your message :")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}

"""
# we add #intentional breakline between subject and from
    button_submit = st.form_submit_button("Submit")
    print(button_submit)
#false if unpressed, true when pressed
#reminder to put print msgs to verify error, data
# and how to give good instructions in loops
    if button_submit:
        send_email(message)
        st.info("Your email has been sent !")