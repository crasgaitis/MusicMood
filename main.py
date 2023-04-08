from utils import make_music, get_key, get_ma_mi, analyze
import streamlit as st  

st.write('please work')

try:
    user_set = st.file_uploader("upload file", type={"csv"})
    analyze(user_set)    
    make_music(get_key(get_ma_mi(user_set)))
    
    audio_file = open('output.mid', 'rb')
    audio_bytes = audio_file.read()
    
    st.audio(audio_bytes, format='audio/ogg')
    
except:
    pass