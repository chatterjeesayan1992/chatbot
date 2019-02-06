import warnings
warnings.filterwarnings('ignore')
from flask import Flask,render_template,request
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
import re
from pandas.api.types import is_string_dtype, is_numeric_dtype
from nltk.tokenize import MWETokenizer
#from temp2 import *
#from variables import *

stop_words = set(stopwords.words('english'))
tokenizer=MWETokenizer()

r=sr.Recognizer()
sample_rate = 48000
chunk_size = 2048
sr.Microphone.list_microphone_names()
mic=sr.Microphone(device_index=1,sample_rate=sample_rate,chunk_size=chunk_size)
df=pd.read_csv("C:/Projects/preprocessed_data.csv")

list_of_column_names=list(df.columns.values)
morphed_names=[]
for names in list_of_column_names:
    names=re.sub('[()]','',names)
    morphed_names.append(names)

morphed_names=[w.split(' ') for w in morphed_names]

morphed_names2=[]
for sent in morphed_names:
    list2=[]
    for w in sent:
        if w!='COGS':
            w=w.lower()
        list2.append(w)
    morphed_names2.append(list2)

final_name_list=[]
for sent in morphed_names2:
    sent=' '.join(sent)
    final_name_list.append(sent)

for strngs in morphed_names2:
    if len(strngs) > 1:
        tokenizer.add_mwe(strngs)

df.columns=final_name_list

aggregate_words=["total", "sum","overall", "aggregate"]
ranking_words={"biggest":1,"highest":1,"peak":1,"top":1,"smallest":0,"least":0,"lowest":0,"bottom":0}
gap_words=["gap","difference"]
trend_words=["trend","year_on_year","quarter_on_quarter"]
year={"current_financial_year":1,"FY2019":1,"present_year":1,"previous_year":0,"last_year":0,"past_year":0,"past_financial_year":0,"last_financial_year":0,"this_year":1,"current_fiscal_year":1,"current_year":1,"next_year":2,"next_financical_year":2,"next_fiscal_year":2,"coming_year":2,"coming_financial_year":2,"coming_fiscal_year":2}
quarter={"current_quarter":1,"present_quarter":1,"this_quarter":1,"last_quarter":0,"previous_quarter":0,"past_quarter":0,"next_quarter":2,"coming_quarter":2,"next_financial_quarter":2,"next_fiscal_quarter":2}
Q={"q1","q2","q3","q4"}

for expressions in trend_words:
    if '_' in expressions:
        tokenizer.add_mwe(tuple(expressions.split('_')))

for expressions in year:
    if '_' in expressions:
        tokenizer.add_mwe(tuple(expressions.split('_')))

for expressions in quarter:
    if '_' in expressions:
        tokenizer.add_mwe(tuple(expressions.split('_')))



