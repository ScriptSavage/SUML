import streamlit as st

def convert_units(value, from_unit, to_unit):
    if from_unit == "Kg" and to_unit == "Pounds":
        return value * 2.20462
    elif from_unit == "Pounds" and to_unit == "Kg":
        return value / 2.20462
    elif from_unit == "Km" and to_unit == "Mile":
        return value * 0.621371
    elif from_unit == "Mile" and to_unit == "Km":
        return value / 0.621371
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    else:
        return value

from_unit = st.selectbox("From Unit :", ["Kg", "Pounds", "Km", "Mile", "Celsius", "Fahrenheit"])

unit_mapping = {
    "Kg": "Pounds",
    "Pounds": "Kg",
    "Km": "Mile",
    "Mile": "Km",
    "Celsius": "Fahrenheit",
    "Fahrenheit": "Celsius"
}

to_unit = unit_mapping[from_unit]

value = st.number_input(f"Input Value : {from_unit}", value=0.0)

if st.button("Convert"):
    if value:
        converted_value = convert_units(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
    else:
        st.write("Invalid value")