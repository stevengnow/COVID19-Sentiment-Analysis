# COVID19-Sentiment-Analysis
Covid19 dataset taken scrapped using snscrape and tweepy.<br/>
Collected 3.7 million tweets over the span of 6 months (May 1, 2020 to November 19,2020).<br/>
We use the dataset to solve the following metrics:<br/>
* Wordcloud for most used words per month.
* Sentiment scale from -1 to 1 using Flair, a pre-trained LSTM neural network used with natural language processing.
* US map visualization: sentiment per state over the course of 6 months
  * i.e. Pattern recognition based off these results show peak negativity in September

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
