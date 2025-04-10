import streamlit as st
#from ..send_email import send_email
import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mikebstudy@gmail.com"
    password = "sygy exnt fwll mjxr"

    context = ssl.create_default_context()

    receiver = "mikebstudy@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

st.header("Contact Me")

with (st.form(key="email_form")):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message2 = f"Subject: From PMC.02.Showcase\n{message}\nFrom: {user_email}"
    print(message2)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message2)
        st.info("Your email was sent successfully.")