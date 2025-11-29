import streamlit as st

st.title('OWSHK School')

name=st.text_input('Please enter your name.')

n,g =st.columns(2)

with g :
    eng=st.number_input('Please enter your english score.',0)

    math=st.number_input('Please enter your math score.',0)

    pe=st.number_input('Please enter your PE score.',0)

    reading=st.number_input('Please enter your reading score.',0)
   
    chinsese=st.number_input('Please enter your chinsese score.',0)

st.divider()

with n :
    his=st.number_input('Please enter your history score.',0)

    art=st.number_input('Please enter your art score.',0)

    music=st.number_input('Please enter your music score.',0)

    ict=st.number_input('Please enter your ICT score.',0)

    geo=st.number_input('Please enter your geography score.',0)

total=eng+math+his+art+music+ict+geo+pe+reading+chinsese

av=total/10

if st.button ('Check my grade.') :

    if av > 90 :
        st.write('You got a A')

    elif av < 90 and av > 70 :
        st.write('You got a B')

    elif av < 70 and av > 50 :
        st.write('You got a C')

    elif av < 50 and av > 30 :
        st.write ('You got a D')

    elif av < 30 and av > 10 :
        st.write ('You got a F')
    
    else :
        st.write('You need to redo this year.')