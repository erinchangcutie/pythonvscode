import streamlit as st

st.title ('Chef Erin cheap & yummy foods')

st.image ('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9kSUs_HJeJybPm5osfWnGW-AD97C7Qy4MsQ&s')

st.subheader ('Meal Category')

bill = 0

meal1, meal2, meal3 = st.columns(3)

with meal1:
    if st.checkbox('Fish & Chips: $3') :
        bill += 3
        st.write('Ok done!')
 
    if st.checkbox('Rice & Fish: $2') :
        bill += 2
        st.write('Ok done!')

with meal2:
    if st.checkbox('Pasta & Sauce: $2') :
        bill += 2
        st.write('Ok done!')
    
    if st.checkbox('Tomato Soup: $3'):
        bill += 3
        st.write('Ok done!')

with meal3:
    if st.checkbox('Salad: $2'):
        bill += 2
        st.write('Ok done!')

    if st.checkbox('Chicken & Rice: $3'):
        bill += 3
        st.write('Ok done!')

st.subheader('Drink Category')

drink1, drink2, drink3 = st.columns(3)

with drink1:
    if st.checkbox('Water: $1'):
        bill += 1
        st.write('Ok done!')

    if st.checkbox('Milk: $2'):
        bill += 2
        st.write('Ok done!')

with drink2:
    if st.checkbox('Hot Tea: $3'):
        bill += 3
        st.write('Ok done!')

    if st.checkbox('Hot Coffee: $3'):
        bill += 3
        st.write('Ok done!')

with drink3:
    if st.checkbox('Cold Orange Juice: $2'):
        bill += 2
        st.write('Ok done!')

    if st.checkbox('Cold Diet Coke: $1'):
        bill += 1
        st.write('Ok done!')

st.subheader('Dessert/Fruit Category')

dessert1,dessert2,dessert3 = st.columns(3)

with dessert1:
    if st.checkbox('Ice Cream: $3'):
        bill += 3
        st.write('Ok done!')
    
    if st.checkbox('Pudding: $2'):
        bill += 2
        st.write('Ok done!')

with dessert2:
    if st.checkbox('Watermelon :$1'):
        bill += 1
        st.write('Ok done!')
    
    if st.checkbox('Honeydew Melon :$1'):
        bill += 1
        st.write('Ok done!')

with dessert3:
    if st.checkbox('Jelly :$2'):
        bill += 2
        st.write('Ok done!')

    if st. checkbox('Popsicle :$3'):
        bill += 3
        st.write('Ok done!')

if st.button('Check my bill'):
    st.write('Your bill is',bill,'dollars.')