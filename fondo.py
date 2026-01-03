import streamlit as st

st.title('How to get chocolate fondue with ICE CREAM!')

st.image('https://www.aeon.com.hk/html/assets/images/HD-Fondue_1225_web-770-4.jpg')

st.write('Start to go on a adventure!')

fondo = st.radio('1. Do you want Fundue Ice Cream?',['Choose an option','Yes','No'])

if fondo == 'Yes' :
    store = st.radio('Did you find a popular ice cream shop that is big and has seats?',['Choose an option','Yes','No'])

    if store == 'Yes' :
        flavour = st.radio ('Please choose a ice cream flavour.', ['Choose an option','Strawberry🍓: $20','Chocolate🍫: $20','Vanilla🍦: $20','Mango🥭: $20'])
       
        if flavour == 'Choose an option' :
            st.info('Please choose an option.')

        cone = st.slider ('How many cones would you like?')

        total_cost = 20 * cone
        if st.button ('Check the price') :
            st.write ('This will be',total_cost,'dollars.')


    elif store == 'Choose an option' :
        st.info('Please choose an option.')

    elif store == 'No' :
        st.error('Sorry do it again next time.')

elif fondo == 'Choose an option':
    st.info('Please choose an option.')



else :
    st.error('Sorry do it again next time.')
    