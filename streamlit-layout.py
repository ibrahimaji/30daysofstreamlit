import streamlit as st
st.set_page_config(layout="wide")
st.title("How to layout your Streamlit app")
with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_alphabet = st.sidebar.selectbox('Choose an alphabet',['','A','B','C'])
user_food = st.sidebar.selectbox('What is your favorite food?',['','Tom Yam','Ayam Goreng','Sop Ayam'])
st.header('Output')
col1,col2,col3 = st.columns(3)
with col1:
    if user_name!='':
        st.write(f'Hello {user_name}')
    else:
        st.write('Please enter your **name**!')
with col2:
    if user_alphabet != '':
        st.write(f'{user_alphabet} is your favorite **alphabet**!')
    else:
        st.write('Please choose an **alphabet**!')
with col3:
    if user_food != '':
        st.write(f' **{user_food}** is your favorite **food**!')
    else:
        st.write('Please choose your favorite **food**')
