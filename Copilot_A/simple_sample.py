# app.py
import streamlit as st

# Title and description
st.title("My First Streamlit App")
st.write("Welcome to my web application!")

# User input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Displaying data
st.write("Here is a random number:")
st.write(42)

# Add a button
if st.button("Click me!"):
    st.write("You clicked the button!")
