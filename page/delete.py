import streamlit as st
import sys

sys.path.insert(1, 'controller')
 
import client as client

def delete():
    st.title("Delete person")
   
    delete_id = st.number_input("Input ID",format="%d",step=1)
  
    if st.button("Delete") :            
        client.delete(delete_id)
        st.success("Delete person success")