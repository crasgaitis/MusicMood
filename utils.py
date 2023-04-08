from music21 import *
import random
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import pygame

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

# make_music(get_key('major'))