import streamlit as st

st.title ('Erin Age Calculator')

name = st.text_input('Please enter your name.')

birth_year = st.number_input('Please enter your birth year.',0)

current_year = st.number_input('Please enter the current year.',0)

age = current_year - birth_year

if st.button ('Check my age'):
    st.write(name,'your age is',age,'.')