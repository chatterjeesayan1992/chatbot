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
from variables import *




def bot(text_given): 
    listening=False 
    typing=False
    occasional_bot_response_flag=False
    occasional_bot_response="None"
    if text_given.isnumeric():
        if int(text_given)==1:
            flag=1
            listening=True
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            try:
                text_given=r.recognize_google(audio)
                occasional_bot_response_flag= True
                occasional_bot_response="You said" + "'"+ text_given + "'"
                bot_response_1=bot_process(text_given)
                return (text_given,bot_response_1,listening,typing,occasional_bot_response_flag,occasional_bot_response)
            except:
                bot_response_1="Could not recognize"
                s=""
                return (s,bot_response_1,listening,typing,occasional_bot_response_flag,occasional_bot_response)
        if int(text_given)==2:
            flag=0
            bot_response_1="Write your question and press enter"
            typing=True
            s=""
            ret=(s,bot_response_1,listening,typing,occasional_bot_response_flag,occasional_bot_response)

    elif text_given.isnumeric()==False:
        typing=True
        bot_response_1=bot_process(text_given)
        ret=(text_given,bot_response_1,listening,typing,occasional_bot_response_flag,occasional_bot_response)
    return ret
        


def bot_process(text_given):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text_given = text_given.translate(translator)
    wordsList = tokenizer.tokenize(text_given.split())
    wordsList = [w.lower() for w in wordsList if w not in stop_words]
    text_given_small=' '.join(wordsList)
    try:
        for words in wordsList:
            if words in aggregate_words:
                question_type="aggregate"
            elif words in ranking_words.keys():
                question_type="ranking"
                rank_code=ranking_words[words]
            elif words in gap_words:
                question_type="difference"
            elif words in trend_words:
                question_type="trend"

        time_quarter_information= False
        time_year_information=False
        for words in wordsList:
            if '_' in words:
                if "year" in words.split('_'):
                    time_year_information=True
                if "quarter" in words.split('_'):
                    time_quarter_information= True
                    is_quarter=df["is current quarter?"]=="Y"
                    current_quarter=df[is_quarter]["quarter"].iloc[0]
                    quarter_no=int(list(current_quarter)[1])
        q_flag=0
        for words in wordsList:
            if words.lower() in Q:
                time_quarter_information=True
                q_flag=1
                quarter_info=words.upper()
                #print(quarter_info)
                quarter_no=int(list(quarter_info)[1])

        if time_year_information==False:
            bot_response_1="Please provide time information"


        if time_year_information==True:
            for words in wordsList: 
                if words in year:
                    code=year[words]
                    if code==1:
                        is_year=df["financial year"]=="FY2019"
                        df_year=df[is_year]
                    elif code==0:
                        is_year=df["financial year"]=="FY2018"
                        df_year=df[is_year]

            if time_quarter_information==True:
                for words in wordsList: 
                    if words in quarter.keys():
                        code=quarter[words]
                        if code==1:
                            is_quarter=df_year["is current quarter?"]=="Y"
                            df_quarter=df_year[is_quarter]
                        elif code==0:
                            qu="Q"+str(quarter_no-1)
                            is_quarter=df_year["quarter"]==qu
                            df_quarter=df_year[is_quarter]
                        elif code==2:
                            qu="Q"+str(quarter_no+1)
                            is_quarter=df_year["is current quarter?"]=="Y"
                            df_quarter=df_year[is_quarter]
                    elif words in Q:
                        if q_flag==1:
                            #print("abc")
                            is_quarter=df_year["quarter"]==quarter_info
                            df_quarter=df_year[is_quarter]
                

        if question_type=="aggregate":
            tagged = nltk.pos_tag(wordsList)
            #print(tagged)
            for words in wordsList:
                if '_' in words and words not in year and words not in quarter:
                    matched_keywords=words
            #print(matched_keywords)
            matched_keywords=matched_keywords.split('_')
            if code==2:
                matched_keywords=matched_keywords.append('forecasted')
            for i,keywords in enumerate(final_name_list):
                if set(matched_keywords)==set(final_name_list[i].split()):
                    #print("got it")
                    required_column=final_name_list[i]
            if time_year_information==True and time_quarter_information==False:
                bot_response_1="Rs "+str(df_year[required_column].sum()) 
            if time_year_information==True and time_quarter_information==True:
                bot_response_1="Rs "+ str(df_quarter[required_column].sum())

        
        if question_type=="ranking":
            tagged = nltk.pos_tag(wordsList)
            matched_keywords=[]
            for w in wordsList:
                if ' '.join(w.split('_')) in final_name_list:
                    matched_keywords.append(' '.join(w.split('_')))
            #print(matched_keywords)
            for w in matched_keywords:
                if is_string_dtype(df[w]):
                    intent_word=w
                if is_numeric_dtype(df[w]):
                    matched_word=w       
            #print(intent_word)
            matched_word=matched_word.split(' ')
            #print(matched_word)
            for i,keywords in enumerate(final_name_list):
                if set(matched_word)==set(final_name_list[i].split()):
                    #print("got it")
                    required_column=final_name_list[i]
            if time_year_information==True and time_quarter_information==False:
                if rank_code==1:
                    index=df_year[required_column].argmax()
                    bot_response_1=df_year[intent_word][index]
                elif rank_code==0:
                    index=df_year[required_column].argmin()
                    bot_response_1=df_year[intent_word][index]

            if time_quarter_information==True and time_year_information==True:
                if rank_code==1:
                    #print(df_quarter[required_column])
                    index=df_quarter[required_column].argmax()
                    bot_response_1=df_quarter[intent_word][index]
                elif rank_code==0:
                    index=df_quarter[required_column].argmin()
                    bot_response_1=df_quarter[intent_word][index]

        if question_type=="difference":
            tagged = nltk.pos_tag(wordsList)
            #print(tagged)
            matched_keywords=[]
            for words in wordsList:
                if '_' in words and words not in year and words not in quarter:
                    matched_keywords.append(words)
            #print(matched_keywords)
            entity1=matched_keywords[0]
            entity2=matched_keywords[1]
            entity1=entity1.split('_')
            entity2=entity2.split('_')
            for i,keywords in enumerate(final_name_list):
                if set(entity1)==set(final_name_list[i].split()):
                    #print("got it")
                    required_column1=final_name_list[i]
            for i,keywords in enumerate(final_name_list):
                if set(entity2)==set(final_name_list[i].split()):
                    #print("got it")
                    required_column2=final_name_list[i]
            entity1=' '.join(entity1)
            entity2=' '.join(entity2)
            if time_year_information==True and time_quarter_information==False:
                bot_response_1="{} - {} = {} Rs".format(entity1,entity2,df_year[entity1].sum()-df_year[entity2].sum())
            elif time_year_information==True and time_quarter_information==True:
                bot_response_1="{} - {} = {} Rs".format(entity1,entity2,df_quarter[entity1].sum()-df_quarter[entity2].sum())        
    except :
        bot_response_1="Sorry!Couldn't understand.."
    return bot_response_1






































    