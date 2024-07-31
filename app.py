import time
import numpy as np
import pandas as pd
import streamlit as st # type: ignore
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Menu", ["Home",'ChatBot',"Settings"], 
        icons=['house', 'chat','gear'], menu_icon="cast", default_index=1)
    selected


# Delete icons
st.markdown("""
<style>
.eyeqlp53.st-emotion-cache-1pbsqtx.ex0cdmw0
{
    visibility:hidden;            
}
.st-emotion-cache-1huvf7z.ef3psqc6
{
    visibility:hidden;            
}                       
</style>           
""",unsafe_allow_html=True)

# Login & sign up
log = st.button("login")
sign = st.button("sign up")
def sign_up():
    st.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)
    with st.form("form 2"):
        col1, col2 = st.columns([1, 1])  
        f_name = col1.text_input("First Name")
        l_name = col2.text_input("Last Name")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        s_status = st.form_submit_button("Submit")
        
        if s_status:
            if f_name == "" or l_name == "":
                st.warning("Please enter your first and last name!")
            else:
                st.success("Sign up successful!")

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


# Website depcription
_LOREM_IPSUM = """
**website helps you find everything about electronics and programming**
"""
def web_des():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.1)
if st.button("website description"):
    st.write_stream(web_des)


# Input image
image = st.file_uploader("Please upload an Image" ,type=["png","jpg"]) # upload file 
if image is not None:
    st.image(image)


# input text
val = st.text_input("enter your question")
print(val)


