from utils import make_music, get_key, get_ma_mi, analyze
import streamlit as st 
from pydub import AudioSegment
from pydub.playback import play
import pickle

st.write('Mood Music')

# with open("4_class_model.pkl", 'rb') as file:
#     clf = pickle.load(file)

try:
    user_set = st.file_uploader("upload file", type={"csv"})
    
    submit = st.button('Go')
    
    if submit:    
        analyze(user_set)  
        st.write(user_set)
        
        midi_file = make_music(get_key(get_ma_mi(user_set)))
        
        midi_file.open("output.mid", "wb")
        midi_file.write()
        midi_file.close()
        
        # midi_path = (make_music(get_key(get_ma_mi(user_set))))
        # midi_audio = AudioSegment.from_file(midi_path, format="mid")
        # play(midi_audio)
        
        # st.audio(midi_audio.export(format="mp3"), format="mp3")
        
        
        
        # generate prompt
        
        def generate_response(prompt):
            response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=30,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = response.choices[0].text.strip()
    
        string = f"Give a caption for an image that is a metaphorical symbol of {emotion}:"
        
        suggested_response = generate_response(string)
        suggested_response = suggested_response.split(":")[0]
        suggested_response = suggested_response.strip().replace("'", "")        
    
except:
    pass