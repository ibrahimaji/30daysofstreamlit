import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('Line chart')

chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
        )

st.line_chart(chart_data)

st.subheader('Altair Chart')

df=pd.DataFrame(
        np.random.randn(200,3),
        columns=['a','b','c']
        )
c=alt.Chart(df).mark_circle().encode(
        x='a',y='b',size='c',color='c',tooltip=['a','b','c']
        )
st.altair_chart(c, use_container_width=True)
