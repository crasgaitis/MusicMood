from utils import make_music, get_key, get_ma_mi, analyze
import streamlit as st 

st.write('please work')

try:
    user_set = st.file_uploader("upload file", type={"csv"})
    
    submit = st.button('Go')
    
    if submit:    
        analyze(user_set)    
        make_music(get_key(get_ma_mi(user_set)))
        
        st.audio()
    
    
except:
    pass