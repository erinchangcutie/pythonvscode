import streamlit as st

st.title ('Minecraft budget')

name = st.text_input ('Please enter your name.')

emeralds = st.number_input ('Please enter the amount of emeralds you have.',0)

weapons = st.number_input ('Please enter how much emeralds you spent on weapons.',0)

armor = st.number_input ('Please enter how much emeralds you spent on armor.',0)

food = st.number_input ('Please enter how much emeralds you spent on food.',0)

blocks = st.number_input ('Please enter how much you spent on building blocks.',0)

total_spent = weapons + armor + food + blocks

emeralds_left = emeralds - total_spent

if st.button ('Check my emeralds') :
        
    if emeralds_left > 20 :
        st.write ('Nice shopping',name,'you still have',emeralds_left,'emeralds left. Save some for rare trades!')

    elif emeralds_left > 0 and emeralds_left < 20 :
        st.write ('Be careful',name,'! You only have',emeralds_left,'emeralds left. spend wisely.')

    elif emeralds_left < 0 :
        st.write ('Oh no',name,'! You are out of emeralds. Better find some villagers to trade with!')

    else :
        st.write ('Error')