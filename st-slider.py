import streamlit as st
from datetime import time, datetime

st.header('st.slider')

#Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#Example 2

st.subheader('Range slider')

values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 25.0)
        )
st.write('Values: ', values)

#Example 3

st.subheader('Range time slider')

appointment = st.slider(
        "Schedule your apppointment:",
        value=(time(11,30), time(12, 45))
        )
st.write("You're scheduled for: ", appointment)

#Example 4

st.subheader('Datetime slider')

start_time = st.slider(
        "When do you start?",
        value = datetime(2020, 1, 1, 9, 30),
        format = "MM/DD/YY - hh:mm"
        )
st.write("Start time: ", start_time)

#Example 5

st.subheader('Select slider')

color = st.select_slider(
        'Select a color of the rainbow',options = ['red','orange','yellow','green','blue','indigo','violet']
        )
st.write('My favorite color is', color)
