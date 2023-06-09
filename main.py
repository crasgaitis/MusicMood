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
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
from config import API_KEY

os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

st.write('Mood Music')

filename = '4_class_model.pkl'
clf = pickle.load(open(filename, 'rb'))



try:
    user_set = st.file_uploader("upload file", type={"csv"})
    user_set = pd.read_csv(user_set)
    user_set.drop('label')
    
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
        # mf.writestr(midi_data)
        st.write(midi_data)
        midi_data.seek(0)
        
        st.download_button(
            label='Download MIDI',
            data=midi_data.getvalue(),
            file_name='music.mid',
            mime='audio/midi')

        for i, row in user_set.iterrows():
            text = row['text']
            prediction = clf.predict([text])[0]
            user_set.loc[i, 'label'] = prediction
        
        st.write('now')
        st.write(user_set)

        
        emotion_map = {
            'joy' : 0,
            'fear' : 1,
            'anger' : 2,
            'sadness' : 3,
        }

        user_set['label'] = user_set['label'].map(lambda x: emotion_map[x])
        user_set['label'] = pd.Categorical(user_set['label'], categories=emotion_map.values())
        
        emotion = user_set['label'].value_counts().idxmax()
        

        sns.countplot(x='label', data=user_set)
        plt.title('Distribution of mental health states')
        plt.ylabel('Count')
        
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
    
        string = f"Give a caption for an image that is a metaphorical symbol of {emotion}:"
        
        suggested_response = generate_response(string)
        suggested_response = suggested_response.split(":")[0]
        suggested_response = suggested_response.strip().replace("'", "")    
        
        st.write('response below')
        st.write(suggested_response)    
    
except:
    pass