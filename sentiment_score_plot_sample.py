#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import datetime
import plotly
import plotly.graph_objs as go
from plotly.offline import plot, iplot, init_notebook_mode


# In[6]:


start_date = datetime.date(2020, 5, 1)
start_date.strftime("%Y-%m-%d")


# In[7]:


state_dic_df = pd.read_csv('state_dic_df.csv').set_index(['index']).iloc[:, 1:]
avg_values_df = pd.read_csv('avg_values_df.csv').set_index(['index']).iloc[:, 1:]
num_tweets_df = pd.read_csv('num_tweets_df.csv').set_index(['index']).iloc[:, 1:]
new_cases_df = pd.read_csv('num_tweets_df.csv').set_index(['index']).iloc[:, 1:]


# In[8]:


state_dic_df


# In[9]:


# loop thru dates
states = state_dic_df.columns
dates = state_dic_df.index

df = avg_values_df


# In[10]:


avg_values_df.agg('mean').argmin()


# In[11]:


fig = go.Figure()

for state in states:
    fig.add_trace(go.Scatter(
        x=new_cases_df[state],
        y=state_dic_df[state].apply(abs),
        mode="markers",
        name=state,
        marker=go.scatter.Marker(
            #size=sz,
            #color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))
    
fig.update_layout(
    title="Correlating Sentiment & COVID cases",
    xaxis_title="log New COVID Cases per 100k (in 15 days)",
    yaxis_title='state total sentiment scores across time',
    #legend_title="States",
    title_x = .5,
    
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
)
fig.update_xaxes(type="log")

iplot(fig)


# In[12]:


fig = go.Figure()

for date in dates[:1]:
    fig.add_trace(go.Scatter(
        x=new_cases_df.loc[date,:],
        y=state_dic_df.loc[date,:],
        mode="markers",
        name=date,
        marker=go.scatter.Marker(
            #size=sz,
            #color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))
    
fig.update_layout(
    title="Correlating Sentiment & COVID cases",
    xaxis_title="log New COVID Cases per 100k (in 15 days)",
    yaxis_title='state total sentiment scores across time',
    #legend_title="States",
    title_x = .5,
    
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
)

iplot(fig)


# In[13]:


fig = go.Figure()

for state in states:
    fig.add_trace(go.Scatter(
        x=new_cases_df[state],
        y=state_dic_df[state].apply(abs),
        mode="markers",
        name=state,
        marker=go.scatter.Marker(
            #size=sz,
            #color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))
    
fig.update_layout(
    title="Correlating Sentiment & COVID cases",
    xaxis_title="log New COVID Cases per 100k (in 15 days)",
    yaxis_title='state total sentiment scores across time',
    #legend_title="States",
    title_x = .5,
    
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
)

iplot(fig)


# In[15]:


def choropleth_scores_plot(state_values, date, cmax, cmin, filename='choropleth.svg'):
    
    fig = go.Figure(data=go.Choropleth(
        locations = states, #['AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'],
        locationmode='USA-states',
        colorscale = 'Viridis',
        z = state_values,
        marker = dict(line = dict(color='rgb(255,255,255)', width=2),
#                      cmax = cmax,
#                      cmin = cmin,
                     #colorbar= dict(title='Average Polarity<br> Scorescore/tweet'),  
                     ),
        zmax = 0,
        zmin = cmin,     
        ))

    fig.update_layout(
        title_text='Number of Tweets: ' + date, 
        font = dict(size = 24),
        geo_scope='usa',
    )
    
    iplot(fig)
    fig.write_image(filename, format='png', width=1400, height=1000, scale=2)


# In[16]:





# In[18]:


for date in dates:
    choropleth_scores_plot(df.loc[date, :], date, cmax, cmin, filename='avg' + date + '.png')


# In[ ]:




