from utils import make_music, get_key, get_ma_mi, analyze
import streamlit as st 
from pydub import AudioSegment
from pydub.playback import play

st.write('please work')

try:
    user_set = st.file_uploader("upload file", type={"csv"})
    
    submit = st.button('Go')
    
    if submit:    
        analyze(user_set)    
        play(make_music(get_key(get_ma_mi(user_set))))
        
        
    
    
except:
    pass