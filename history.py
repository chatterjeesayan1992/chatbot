# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Wed Dec 12 16:57:04 2018)---
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')

## ---(Thu Dec 13 10:01:50 2018)---
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
CLS
clear
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')

## ---(Fri Dec 14 23:00:08 2018)---
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
import numpy as np 
import pandas as pd 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import gensim
from gensim.models import Word2Vec
import string
from string import digits
import matplotlib.pyplot as plt
from pyjarowinkler import distance
import speech_recognition as sr
#nltk.download("averaged_perceptron_tagger")
#nltk.download('punkt')
#nltk.download('stopwords')

r=sr.Recognizer()
sample_rate = 48000
chunk_size = 2048

sr.Microphone.list_microphone_names()

mic=sr.Microphone(device_index=1,sample_rate=sample_rate,chunk_size=chunk_size)



df=pd.read_csv("C:/Projects/data_for_chatbot.csv")



## ---(Sun Dec 16 19:30:48 2018)---
import pandas as pd
df=pd.read_csv("C:/Projects/data_for_chatbot.csv")

## ---(Mon Dec 17 09:36:36 2018)---
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')

## ---(Mon Dec 17 11:53:07 2018)---
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')
matched_keywords
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')

## ---(Tue Dec 18 20:19:47 2018)---
runfile('C:/Users/sayanc098/.spyder-py3/temp.py', wdir='C:/Users/sayanc098/.spyder-py3')