from utils import get_key, get_ma_mi, analyze
import streamlit as st 
from pydub import AudioSegment
from pydub.playback import play
import openai
import pickle
from music21 import *
import random
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import pygame
import io
import pandas as pd

st.write('Mood Music')

# with open("4_class_model.pkl", 'rb') as file:
#     clf = pickle.load(file)


try:
    user_set = st.file_uploader("upload file", type={"csv"})
    user_set = pd.read_csv(user_set)
    
    submit = st.button('Go')
    
    if submit:    
        analyze(user_set) 
        st.write('submitted') 
        st.write(user_set)
        
        key_input = (get_key(get_ma_mi(user_set)))
        st.write(key_input)
        # thing
        
        key_str = key_input
        key_obj = key.Key(key_str)
        time_signature = meter.TimeSignature('4/4')

        # melody: random notes
        melody = stream.Stream()
        melody.append(key_obj)
        melody.append(time_signature)

        for i in range(8):
            note_name = random.choice(scale.MajorScale(key_str).getPitches() + scale.MelodicMinorScale(key_str).getPitches())
            note_obj = note.Note(note_name)
            note_obj.duration = duration.Duration(random.choice([0.25, 0.5, 1, 2]))
            melody.append(note_obj)

        # create MIDI file
        
        mf = midi.translate.streamToMidiFile(melody)
        
        midi_data = io.BytesIO()
        mf.write(midi_data)
        midi_data.seek(0)

        # Create download button for MIDI file
        st.download_button(
            label='Download MIDI',
            data=midi_data.getvalue(),
            file_name='music.mid',
            mime='audio/midi')
        
        # thing
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