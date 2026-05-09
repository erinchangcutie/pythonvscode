import streamlit as st

menu = st.sidebar.radio('Choose an option',['Welcome','Upload Picture','Take a picture','Upload videos'])

if menu == 'Welcome':
    st.image('https://air.io/storage/boxAdis6iyIGQ240Kejd1VEdUGouU9deZdDPzu5Y.jpg')

    st.header(':rainbow[Welcome to Ow Ow music & video app!]')

    st.balloons()

elif menu == 'Upload Picture':
   st.subheader('Choose a Ow Ow picture to view')
   uploadpic = st.file_uploader('Choose a picture to view',type=['png','jpeg','jpg'])
   #stores the image in the variable
   
   if uploadpic:#if variable has something inside
        st.image(uploadpic)#show image

elif menu == 'Take a picture':

    st.subheader('Take a Ow Ow picture')  
    selfie = st.camera_input('Take an picture')

    if selfie:
        st.image(selfie)

elif menu == 'Upload videos' :
    st.subheader('Choose a Ow Ow video')
    uploadvid = st.text_input('Upload a Ow Ow youtube video')
    if uploadvid :
        st.video(uploadvid)