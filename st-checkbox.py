import streamlit as st
st.header('st.checkbox')
st.write('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffe = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more Ice cream")
if coffe:
    st.write("Okay, here's some coffe")
if cola:
    st.write("Here's your Cola!")
