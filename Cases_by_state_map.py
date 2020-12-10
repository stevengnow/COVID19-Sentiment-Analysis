#!/usr/bin/env python
# coding: utf-8

# In[1]:


#------------------Importing modules-------------

import pandas as pd
import plotly.express as px
from plotly.offline import plot

#----------------Rendering to browser when function is called---
#pio.renderers.default = 'browser'
pd.set_option('display.max_rows',1000)

#----------------Covid Data-------------------------------------
dx = pd.read_csv('https://query.data.world/s/tofgsyk2mqbcwudhhsdfcydxgrreru')


#---------------Removing extra dates----------------------------
dx = dx.set_index('date')
temp = dx.head(10).index.tolist()
dx = dx.drop(temp)
temp = dx.tail(4).index.tolist()
dx = dx.drop(temp)
dx.reset_index(inplace=True)

#---------------Deleting states----------------------------------
dx = dx.set_index('state')
dx = dx.drop(['Northern Mariana Islands','Guam','American Samoa','Puerto Rico','Virgin Islands'])


#--------------Calculating Data for 100k of ten month period------
state = dx.groupby(['state'])
state = state.sum()
state= state.drop(state.iloc[:,:10], axis = 1)
state = state.div(10)


#--------------Cleaning Data------------------------------------------
#state.dtypes = state.astype({'new_cases_per_100_000':'string'}).dtypes
state['new_cases_per_100_000'] = state.new_cases_per_100_000.astype(str)
state['new_cases_per_100_000'] = state['new_cases_per_100_000'].apply(lambda x: int(x.split('.')[0].replace('.','')))
state.reset_index(inplace=True)
state['state'] = state.state.astype(str)

#-------------Data set for US Map--------------------------------------
url = "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
df_abbrev = pd.read_csv(url)

#-----------------Merging Data----------------------------------------
state = state.rename(columns={"state":'State'})
result = pd.merge(state,df_abbrev, on = 'State')


#--------------------Rendering---------------------------------------
fig = px.choropleth(result, locationmode='USA-states',locations =result['Abbreviation'],color ='new_cases_per_100_000',
                   color_continuous_scale='Blues', range_color= (0,result['new_cases_per_100_000'].max()), scope='usa',
                   title ='New Covid Cases Per 100k')

#fig.show()


# In[2]:


get_ipython().system('pip install chart_studio==1.1.0')


# In[3]:


import chart_studio.plotly as py
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://query.data.world/s/tofgsyk2mqbcwudhhsdfcydxgrreru')
df_HI = df[df.state == 'Hawaii']
df_al = df[df.state == 'Alabama']
fig = make_subplots(rows=2, cols=1, start_cell="bottom-left")

fig.add_trace(go.Scatter(x= df_HI['date'], y= df_HI['new_cases_per_100_000'], name ='Hawaii', opacity = 0.6),row =1,col =1)
fig.add_trace(go.Scatter(x= df_al['date'], y= df_al['new_cases_per_100_000'], name ='Alabama', opacity = 0.6),row=2,col =1)

fig.update_layout(height=500, width=700,
                  title_text="Covid Cases", title_x = .5, title_font_color='black',title_font_family="Times New Roman" )
#fig.show()


# In[4]:


import chart_studio.plotly as py
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd
fig = go.Figure()

df = pd.read_csv('https://query.data.world/s/tofgsyk2mqbcwudhhsdfcydxgrreru')
df_HI = df[df.state == 'Hawaii']
df_al = df[df.state == 'Alabama']

fig.add_trace(go.Scatter(
    x=df_HI['date'],
    y=df_HI['new_cases_per_100_000'],
    name="Hawaii"       # this sets its legend entry
))


fig.add_trace(go.Scatter(
    x=df_HI['date'],
    y=df_al['new_cases_per_100_000'],
    opacity = 0.6,
    name="Alabama"
))
#If we want to remove grid lines
#fig.update_xaxes(showgrid= False)

fig.update_layout(
    title="New_Cases",
    yaxis_title="New Cases per 100k",
    legend_title="States",
    title_x = .5,
    
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

fig.show()


# In[5]:


###--------------------two weeks interval----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

df = pd.read_csv('https://query.data.world/s/tofgsyk2mqbcwudhhsdfcydxgrreru')

#changing the type of date to datetime64 to perform correct operations

df.date = pd.to_datetime(df.date, utc = True)

#--------------Selecting rows between two dates------

start_date = pd.to_datetime('7/14/2020', utc= True)
end_date = pd.to_datetime('7/31/2020 12:49', utc= True)
df = df.loc[(df['date'] > start_date) & (df['date'] < end_date)]

df['date'] = df['date'].dt.strftime('%m-%d-%Y')

df_HI = df[df.state == 'Hawaii']
df_Al = df[df.state == 'Alabama']


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_HI['date'],
    y=df_HI['new_cases_per_100_000'],
    name="Hawaii"       # this sets its legend entry
))


fig.add_trace(go.Scatter(
    x=df_HI['date'],
    y=df_Al['new_cases_per_100_000'],
    opacity = 0.6,
    name="Alabama"
))
#If we want to remove grid lines
#fig.update_xaxes(showgrid= False)

fig.update_layout(
    title="Two Weeks",
    yaxis_title="New Cases per 100k",
    legend_title="States",
    title_x = .5,
    
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

fig.show()


# In[32]:


d_new = pd.read_csv('All_states_15_day_intervals.csv')
dx = pd.read_csv('state_dic_df.csv')

date = d_new['date'][6:]
TX = d_new['TX'][6:]
FL = d_new['FL'][6:]
FL1 = dx['FL']
TX1 = dx['TX']
NY = d_new['NY'][6:]
CA = d_new['CA'][6:]
NY1 = dx['NY']
CA1 = dx['CA']
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=date,
    y=TX,
    opacity = 0.6,
    name="Texas",
    marker = dict(
    color='orange'
    )
))

fig.add_trace(go.Scatter(
    x=date,
    y=FL,
    opacity = 0.6,
    name="Florida",
    marker = dict(
    color='green'
    )
    
))
fig.add_trace(go.Scatter(
    x=date,
    y=CA,
    opacity = 0.6,
    name="California",
    marker = dict(
    color='black'
    )
    
))
fig.add_trace(go.Scatter(
    x=date,
    y=NY,
    opacity = 0.6,
    name="New York",
    marker = dict(
    color='blue'
    )
))
fig.update_layout(
    width = 1000,
    title="Two Weeks Cases Per 100k",
    yaxis_title="Cases",
    legend_title="States",
    title_x = .5
    
    
)
fig.show()
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=date,
    y=FL1,
    opacity = 0.6,
    name="Florida sentiment",
    fill = 'toself',
    marker = dict(
    color='green'
    )
))


fig.add_trace(go.Scatter(
    x=date,
    y=TX1,
    fill = 'toself',
    opacity = 0.6,
    name="Teaxs Sentiment",
    marker = dict(
    color='orange'
    )
))



fig.add_trace(go.Scatter(
    x=date,
    y=NY1,
    fill = 'toself',
    opacity = 0.6,
    name="New York Sentiment",
    marker = dict(
    color='blue'
    )
))

fig.add_trace(go.Scatter(
    x=date,
    y=CA1,
    opacity = 0.6,
    name="CA sentiment",
    fill = 'toself',
    marker = dict(
    color='black'
    )
))


fig.update_layout(
    width = 1000,
    title="Two Weeks Cases Per 100",
    yaxis_title="Total Sentiment",
    legend_title="States",
    title_x = .5,
    
    
)
fig.show()


# In[ ]:




