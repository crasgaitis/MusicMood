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
        st.write(user_set)
        
          
        make_music(get_key(get_ma_mi(user_set)))
        
        # midi_path = (make_music(get_key(get_ma_mi(user_set))))
        # midi_audio = AudioSegment.from_file(midi_path, format="mid")
        # play(midi_audio)
        
        # st.audio(midi_audio.export(format="mp3"), format="mp3")
        
        
    
except:
    pass