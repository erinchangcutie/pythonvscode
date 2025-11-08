import streamlit as st

st.title('Ow Ow toy store')

toy1,toy2,toy3=st.columns(3)

with toy1:

    st.image('https://m.media-amazon.com/images/I/71ayZU0UU8L._AC_UL640_FMwebp_QL65_.jpg')

with toy2:
    
    st.subheader('Magnetic Blocks: $10')

with toy3:

    st.number_input('How many blocks do you want to get?',0)

st.divider()

plush1,plush2,plush3=st.columns(3)

with plush1:

    st.image('https://m.media-amazon.com/images/I/81VeJf19jcL._AC_UL640_FMwebp_QL65_.jpg')

with plush2:

    st.subheader('Bunny Plush: $5')

with plush3:

    st.number_input('How many plushies do you want to get?',0)

st.divider()

labubu1,labubu2,labubu3=st.columns(3)

with labubu1:

    st.image('https://m.media-amazon.com/images/I/71C45OtMGnL._AC_UL640_FMwebp_QL65_.jpg')

with labubu2:

    st.subheader('La Bu Bu: $20')

with labubu3:

    st.number_input('How many La Bu Bu do you want?',0)

st.divider()