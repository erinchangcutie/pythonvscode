import streamlit as st

st.title('Ow Ow summer camp')

name=st.text_input('Please enter your name.')

a,b=st.columns(2)

with a:
    py=st.number_input('Please enter your Python score.',0)

    web_d=st.number_input('Please enter your web design score.',0)

with b:
    r=st.number_input('Please enter your robotics score.',0)

    minecraft=st.number_input('Please enter your Minecraft coding score.',0)

total=py+web_d+r+minecraft

average=total/4

if st.button('Check my grade'):
  
    if average>90:
      st.write('Great job',name,'you got platinum!')        

    elif average<90 and average>80:
      st.write('Great job',name,'you got Gold!')

    elif average<80 and average>70:
       st.write('Great job',name,'you got silver!')

    elif average<70 and average>60:
       st.write('Great job',name,'you got bronze!')

    elif average<60 and average>50:
        st.write(name,'you participated!')
    
    else:
      st.write(name,'you need to redo summer camp every single year until you pass wish you luck.')