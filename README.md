# COVID19-Sentiment-Analysis
We collected a Covid19 tweets dataset by scraping from Twitter using snscrape and tweepy.<br/>
This dataset contains 3.7 million English tweets over the span of 6 months (May 1, 2020 to November 19,2020) and user profile locations, which can provide us with insights into how people's attitude towards the COIVD-19 pandemic changed over time.<br/>

We use the dataset to inestigate the following topics:<br/>
* What are people talking about when they mention COVID-19? - Generating word-clouds for most mentioned words per month.
* How do people's attitude towards the pandemic change as it evolves? - Sentiment scores analysis scaled from -1 to 1 using Flair, a pre-trained LSTM neural network used with natural language processing.
* How do people's sentiments differ based on the US state they come from/live in? - COVID-related tweets sentiment scores choropleth map visualization using Plotly: average sentiment per state over the course of 6 months
  * i.e. Pattern recognition based off these results show peak negativity in September

Interested in our observations? Please see "ECE143 Final Project.pdf" for the slides for our final presentation.

## File Structure
* python files can be run separately to generate the specific metric titled by the file
* ipynb can be used to visualize a subset of the outputs used in presentation. (random sample of 3000 for much faster runtime)
  * if full visualization is necessary, remove line 3 under 'load in data' in metrics.ipynb
* all code can be run normally with the following 3rd party modules installed:
  * NumPy==1.18.5
  * Pandas==1.1.4
  * matplotlib.pyplot==3.2.1
  * wordcloud==1.8.1
  * torch==1.5.1+cu92
  * flair==0.6.1.post1
  * spacy==2.3.4
  * tqdm==4.46.1
  * plotly==4.14.0, plotly.express==0.4.1
  * chart_studio==1.1.0
* code reads in the proper csv files that are now made available
