from music21 import *
import random
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import pygame

def make_music(key_input):

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
  
  pygame.init()
  pygame.midi.init()

  # Set up a midi output device
  output_device = pygame.midi.Output(0)

  # Play the melody notes
  for element in melody.flat.notes:
      pitch = element.pitch.midi
      duration_in_ms = int(element.duration.quarterLength * 1000)
      volume = 100
      output_device.note_on(pitch, volume)
      pygame.time.wait(duration_in_ms)
      output_device.note_off(pitch)

  # Close the midi output device
  output_device.close()

  # Quit Pygame midi module
  pygame.midi.quit()
  pygame.quit()


def get_key(type):
  if type == "major":
    key = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
  else:
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  return random.choice(key)

def get_ma_mi(set):

  score_avg = np.mean(set['mh_state'])

  if score_avg > -0.3:
    return 'major'
  else:
    return 'minor'

def analyze(set):

  analyzer = SentimentIntensityAnalyzer()

  sentiment_scores = []
  for message in set['text']:
      score = analyzer.polarity_scores(str(message))
      sentiment_scores.append(score['compound'])

  set['mh_state'] = sentiment_scores
  
# test

# analyze(user_set)

make_music(get_key('major'))