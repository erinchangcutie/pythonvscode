import streamlit as st

animals=50

st.write('You have 50 animals.')

sold=st.number_input('How many animals did you sell at the market?',0)

eat=st.number_input('How many animals did you eat?',0)

escape=st.number_input('How many animals escaped?',0)

give=st.number_input('How many animals did you give?',0)

total=sold+eat+escape+give

animals_left=animals-total

if st.button ('Check ny animals') :

    if animals_left > 0 :
        st.write('Great job! You still have lots of animals.')

    else :
        st.write('Oh No! You have no more animals.')