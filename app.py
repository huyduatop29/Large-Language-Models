import time
import numpy as np
import pandas as pd
import streamlit as st # type: ignore

log = st.button("login")
sign = st.button("sign up")

def sign_up():
    st.markdown("<h1></h1>User Registration</h1>",unsafe_allow_html=True)
    with st.form("form 2"):
        col1,col2=st.columns(2)
        col1.text_input("First Name")
        col2.text_input("Last Name")
        st.text_input("Email Adress")
        st.text_input("Password")
        st.form_submit_button("submit")

def login():
    st.markdown("<h1></h1>User Registration</h1>",unsafe_allow_html=True)
    with st.form("form 2"):
        st.text_input("Email Adress")
        st.text_input("Password")
        st.form_submit_button("submit")

if log:
    login()
if sign:
    sign_up()




_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

if st.button("Stream data"):
    st.write_stream(stream_data)

image = st.file_uploader("Please upload an Image" ,type=["png","jpg"]) # upload file 
if image is not None:
    st.image(image)

val = st.text_area("enter your question")
print(val)