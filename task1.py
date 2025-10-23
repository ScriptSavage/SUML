import streamlit as st

st.title("Suml Quiz")

st.text('Task 1')
st.latex('x^3 = 27')
task1 = st.multiselect('Jaka jest wartość x?', ['1', '2', '3'])
task1_correct_answer = ['3']

st.text('Task 2')
task2 = st.multiselect('Kiedy był chrzest Polski?', ['1234', '1910', '966'])
task2_correct_answer = ['966']

st.text('Task 3')
task3 = st.radio('Kto jest prezydentem Polski?', ['Adam Małysz', 'Karol Nawrocki', 'Robert Kubica'])
task3_correct_answer = 'Karol Nawrocki'

if st.button("Sprawdź wynik"):
    score = 0

    if task1 == task1_correct_answer:
        score += 1
    if task2 == task2_correct_answer:
        score += 1
    if task3 == task3_correct_answer:
        score += 1

    if score == 3:
        st.balloons()
    st.success(f"Wynik: {score}/3")
