import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

points = 0
points_max = 5
showing = False

st.header("Quiz")

Q1 = st.radio('What is the capital of Poland?', ['Paris', 'Warsaw', 'Krakow'])
Q2 = st.radio('What day is it?', ['Monday', 'Monday', 'Thursday', 'Friday'])
Q3 = st.radio('Cats or Dogs?', ['Cats', 'Dogs'])
Q4 = st.radio('How many shades of gray are there?', ['What?', '50'])
Q5 = st.radio('Did you like the quiz?', ['Yes', 'No'])

if Q1 == 'Warsaw':
    points += 1
if Q2 == 'Thursday':
    points += 1
if Q3 == 'Cats':
    points += 1
if Q4 == '50':
    points += 1
if Q5 == 'Yes':
    points += 1

showing = st.button('Show points')

if showing:
    st.caption(f"Your score: {points}/{points_max}")

st.header("Konwerter")

import streamlit as st

def convert_units(value, from_unit, to_unit):
    if from_unit == "Kilogramy" and to_unit == "Funty":
        return value * 2.20462
    elif from_unit == "Funty" and to_unit == "Kilogramy":
        return value / 2.20462
    elif from_unit == "Kilometry" and to_unit == "Mile":
        return value * 0.621371
    elif from_unit == "Mile" and to_unit == "Kilometry":
        return value / 0.621371
    elif from_unit == "Celsjusz" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsjusz":
        return (value - 32) * 5/9
    else:
        return value

st.caption("Konwertuj Kilometry na mile, Celsjusz na fahrenheit, Kilogramy na funty i na odwrót")

from_unit = st.selectbox("Z jednostki:", ["Kilogramy", "Funty", "Kilometry", "Mile", "Celsjusz", "Fahrenheit"])

unit_mapping = {
    "Kilogramy": "Funty",
    "Funty": "Kilogramy",
    "Kilometry": "Mile",
    "Mile": "Kilometry",
    "Celsjusz": "Fahrenheit",
    "Fahrenheit": "Celsjusz"
}

to_unit = unit_mapping[from_unit]

value = st.number_input(f"Wprowadź wartość w {from_unit}", value=0.0)

if st.button("Przelicz"):
    if value:
        converted_value = convert_units(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
    else:
        st.write("Proszę wprowadzić wartość do konwersji.")