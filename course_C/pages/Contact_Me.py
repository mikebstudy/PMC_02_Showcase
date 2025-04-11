import streamlit as st
import send_email as se

st.header("Contact Me")

with (st.form(key="email_form")):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message2 = f"Subject: From PMC.02.Showcase\n{message}\nFrom: {user_email}"
    print(message2)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        se.send_email(message2)
        st.info("Your email was sent successfully.")