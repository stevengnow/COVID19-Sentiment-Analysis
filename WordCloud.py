#!/usr/bin/env python
# coding: utf-8

# # ECE143 Project - WordCloud Metric

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


# #### Find Most Common Words - Wordcloud 

# In[8]:


def str_to_dt(date_str):
    return datetime.datetime.strptime(date_str[:10], '%Y-%m-%d').date()

df = Data.assign(date=Data.date.apply(str_to_dt), axis=1)
start_date = datetime.date(2020, 5, 1)
end_date = datetime.date(2020, 11, 19) #change this
delta = datetime.timedelta(days=30)
while start_date < end_date:   
    since = start_date
    until = start_date + delta
    df_date = df.loc[(df['date'] < until) & (df['date'] >= since)]
    clean = []
    for tweet in tqdm(df_date['tweet']):  
        result = re.sub(r"http\S+", "", str(tweet))
        clean.append(result.lower())
    # Collect Tweet Data
    join = ' '.join(clean)
    c = dict(Counter(join.split()))
    sort_c = dict(sorted(c.items(), key=lambda x: x[1], reverse = True))
    # print("The most common words and their frequency: ", sort_c)

    # WordCloud Generation
    text = ' '.join(row for row in clean)
    text = text[:100000]  #spacy limit
    sp = spacy.load('en_core_web_sm')
    doc = sp(text)
    newText =''
    for word in doc:
        if word.pos_ in ['ADJ','NOUN']:  # can switch to ['ADJ','NOUN'] if we want to include big nouns
            newText = ' '.join((newText, word.text.lower()))
    wordcloud = WordCloud(background_color = 'white').generate(newText.replace('covid','').replace("new", " ").replace('coronavirus','').replace('case',''))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    start_date += delta


# In[ ]:




