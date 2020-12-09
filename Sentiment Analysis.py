#!/usr/bin/env python
# coding: utf-8

# # ECE143 Final Project - COVID19 Tweet Data Analysis

# #### Imports 

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame
from os import path
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
import string
import time
import torch
import flair
import spacy
from tqdm import tqdm
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
import datetime


# #### Recognize GPU 

# In[2]:


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)


# #### Load in Data 

# In[3]:


filename = 'US_tweets.feather'
Data = pd.read_feather('US_tweets.feather')


# #### Sentiment Analysis

# In[4]:


# Load in Classifier (Pre-trained model)
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')


# In[5]:


# Sentiment Analysis
def Sentiment_Analysis(column):
    start_time = time.time()
    sentiment, neg_sen, pos_sen, neg_values, pos_values = [],[],[],[],[]
    negative,positive = 0,0
    for i in tqdm(range(len(column))): 
        s = flair.data.Sentence(column[i])
        flair_sentiment.predict(s)
        sentiment.append(str(s.labels))
    for i in range(len(sentiment)):
        if 'NEGATIVE' in sentiment[i]:
            negative += 1
            neg_sen.append(sentiment[i])
        else:
            positive += 1
            pos_sen.append(sentiment[i])
    for analysis in neg_sen:
        substring = analysis[analysis.find('(')+1:analysis.find(')')]
        neg_values.append(substring)
    for analysis in pos_sen:
        substring = analysis[analysis.find('(')+1:analysis.find(')')]
        pos_values.append(substring)
    pos_values = list(round(float(value),1) for value in pos_values)
    neg_values = list(round(float(value),1) for value in neg_values)
    pos_dict = dict(Counter(pos_values))
    neg_dict = dict(Counter(neg_values))
    return pos_values, neg_values, pos_dict, neg_dict
    print ("Total time:", time.time() - start_time)
    print('Number of positive tweets:' , positive)
    print('Number of negative tweets:' , negative) 


# In[6]:


def sentiment_states(Data):
    def str_to_dt(date_str):
        return datetime.datetime.strptime(date_str[:10], '%Y-%m-%d').date()

    df = Data.assign(date=Data.date.apply(str_to_dt), axis=1)
    start_date = datetime.date(2020, 5, 1)
    end_date = datetime.date(2020, 11, 19) #change this
    delta = datetime.timedelta(days=15)

    keys = ['AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    state_dic = {k: [] for k in keys}
    avg_values = {k: [] for k in keys}
    num_tweets = {k: [] for k in keys}

    date_index = []
    while start_date < end_date:
        
        date_index.append(start_date.strftime("%Y-%m-%d")) 
        since = start_date
        until = start_date + delta
        df_date = df.loc[(df['date'] < until) & (df['date'] >= since)]

        for state in keys:
            Data = df_date[df_date['state'] == state].tweet
            pos_values, neg_values, pos_dict, neg_dict = Sentiment_Analysis(Data.reset_index(drop = True))
            state_dic[state].append(int(sum(pos_values) - int(sum(neg_values))))
            if (len(pos_values) + len(neg_values)) != 0:
                avg_values[state].append((int(sum(pos_values) - int(sum(neg_values))))/(len(pos_values) + len(neg_values)))
            else:
                avg_values[state].append(0)
            num_tweets[state].append(len(Data))

        start_date += delta

    state_dic['index'] = date_index
    avg_values['index'] = date_index
    num_tweets['index'] = date_index

    state_dic_df = pd.DataFrame(state_dic)
    avg_values_df = pd.DataFrame(avg_values)
    num_tweets_df = pd.DataFrame(num_tweets)

    state_dic_df.to_csv('state_dic_df' + '.csv')
    avg_values_df.to_csv('avg_values_df' + '.csv')
    num_tweets_df.to_csv('num_tweets_df' + '.csv')


# In[ ]:


#Sentiment Analysis of the Column of interest
pos_values, neg_values, pos_dict, neg_dict = Sentiment_Analysis(Data['tweet'].reset_index(drop = True))
negate = []
negative, positive = [],[]
# Plot Quantative results of the responses
negate = [-x for x in list(neg_dict.keys())]
negative = [x/len(Data)*100 for x in list(neg_dict.values())]
positive = [x/len(Data)*100 for x in list(pos_dict.values())]
x = negate + list(pos_dict.keys())
y = negative+positive
plt.bar(x, y, width = 0.07)
plt.title('Sentiment Analysis')
plt.xlabel('Very negative (-1) to Very positive (+1) Tweets')
plt.ylabel('Percent of Tweets')
plt.show()

df = DataFrame(zip(x,y), columns = ['Very negative (-1) to Very positive (+1) Tweets', 'Percent'])
fig = px.bar(df, x = 'Very negative (-1) to Very positive (+1) Tweets', y = 'Percent')
fig.show()
df = DataFrame(zip(x,list(neg_dict.values())+list(pos_dict.values())), columns = ['Very negative (-1) to Very positive (+1) Tweets', 'Number of Tweets'])
fig = px.bar(df, x = 'Very negative (-1) to Very positive (+1) Tweets', y = 'Number of Tweets')
fig.show()


# In[ ]:


sentiment_states(Data)

