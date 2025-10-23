import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.write("Hello")

st.title("SUML WEB")

st.code("x=abcd")

st.latex("a^2 + b^2 = c^")

st.checkbox("yes")
st.checkbox("no")

st.button("Click")
st.radio('Pick your gender' ,['Male','Female'])

st.selectbox('Pick your gender' ,['Male','Female'])

st.select_slider('Pick a mark',['Bad','Good','Excellent'])

st.slider('Pick a mark',0,50)


st.number_input('Pick a')
st.text_input('Pick b')
st.date_input('Pick c')
st.time_input("Pick a time")
st.text_input('Pick d')
st.file_uploader('Choose a file')
st.color_picker('Pick a color')

st.balloons()
st.progress(10)


rand = np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=20)
st.pyplot(fig)

st.line_chart()