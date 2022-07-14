import streamlit as st

st.title('Moje prvni appka')

st.write('Toto je moje prvni aplikace, kterou delam')

page = st.sidebar.radio('Select page',['Test','Thomson'])
if page == 'Test':
    st.write('Toto je moje prvni aplikace, kterou delam')

if page == 'Thompson':
    st.write('Thompson sampling')
