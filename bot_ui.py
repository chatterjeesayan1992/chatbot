import warnings
warnings.filterwarnings('ignore')
from flask import Flask,render_template,request,redirect,url_for,Response
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
from variables import *
from bot_logic import *
import random,json
import sys
import json
#import turtle

s="Hello! Press the type icon to write or press the mic button to speak"


app = Flask(__name__, static_folder='static')



@app.route('/')
def index():
	return render_template('page7.html',bot_response=s)

@app.route('/pass_val/?value=<user_input>',methods=['POST','GET'])
def last_page(user_input):
    return render_template('page7.html',my_query=user_input)

@app.route('/pass_val',methods=['POST','GET'])

def process():
    speaker_flag=False
    get_flag=False
    if request.method=="GET":
        qs=request.query_string
        qs=str(qs)
        if "speaker" in qs:
            speaker_flag=True
        if speaker_flag==True:
            text_given="1"
            reply=bot(text_given)
            return render_template('page7.html',my_query=reply[0],bot_response=reply[1],listen=reply[2],type=reply[3],speech_detecting=reply[4],speech_detected=reply[5])
        if "type" in qs:
            get_flag=True
        if get_flag==True:
            text_given="2"
            reply=bot(text_given)
            return render_template('page7.html',my_query=reply[0],bot_response=reply[1],listen=reply[2],type=reply[3],speech_detecting=reply[4],speech_detected=reply[5])

    elif request.method=="POST" :
        text_given=request.form["user_input"]
        reply=bot(text_given)
        return render_template('page7.html',my_query=reply[0],bot_response=reply[1],listen=reply[2],type=reply[3],speech_detecting=reply[4],speech_detected=reply[5])

    return render_template("page7.html",my_query=request.query_string)
    
  
    

if __name__=='__main__':
	app.run(debug=True,port=5000)












#with open(r"C:\Users\sayanc098\.spyder-py3\templates\page7.html") as inf:
#    txt = inf.read()
#    soup = bs4.BeautifulSoup(txt)
