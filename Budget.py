import streamlit as st

st.title ('Erin Budget Planer')

name = st.text_input ('Please enter your name.')

monthly_income = st.number_input ('Please enter your monthly income.',0)

rent = st.number_input ('Please enter your monthly cost for rent.',0)

groceries = st.number_input ('Please enter your monthly cost for groceries.',0)

transportation = st.number_input ('PLease enter your mothly cost for transportation.',0)

other_expenses = st.number_input ('Please enter your monthly cost for other expenses.',0)

total_cost = rent + groceries + transportation + other_expenses

total_balance = monthly_income - total_cost

if st.button ('Check my balance') :
    
    if total_balance > 500 :
        st.write ('Yay! Great job',name,'! You have $',total_balance,'left! Consider saving or investing some of it!')

    elif total_balance >0 and total_balance < 500 :
        st.write ('Great job',name,'! you have $',total_balance,'left! This is a good amount for savings or lisure!')


    elif total_balance == 0 :
        st.write('Opps',name,'you spent all your money! You have $',total_balance,'!')

    elif total_balance < 0 :
        st.write ('Opps',name,'You are over budget by $',total_balance,'. Consider cutting back on expenses.')

    else :
        st.write('Error')