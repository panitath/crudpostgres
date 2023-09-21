import streamlit as st
import sys

sys.path.insert(1, 'controller')
 
import client as client

def insert():
    st.title("Add new person")
    with st.form(key ="insert"):
        input_fullname = st.text_input(label="Fullname")
        input_email = st.text_input(label="email")
        input_age = st.text_input(label="age")
        button_submit = st.form_submit_button(label="Submit")
        if button_submit :
            client.insert(input_fullname,input_email,input_age)
            st.success("Insert person success")
            st.experimental_rerun()