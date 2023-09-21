import streamlit as st
import sys

sys.path.insert(1, 'controller')
 
import client as client

def update():
    st.title("Update person")
   
    update_id = st.number_input("Input ID",format="%d",step=1)
    input_fullname = st.text_input(label="Fullname")
    input_email = st.text_input(label="Email")
    input_age = st.text_input(label="Age")

    if st.button("Update") :            
        client.update(update_id,input_fullname,input_email,input_age)
        st.success("Update person success")