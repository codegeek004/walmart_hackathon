import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from keybert import KeyBERT
from datetime import datetime

# NLP tools
analyzer = SentimentIntensityAnalyzer()
kw_model = KeyBERT(model='all-MiniLM-L6-v2')

df= pd.read_csv('/content/marketing_sample_for_walmart_com-walmart_product_reviews__20200401_20200630__30k_data.csv')
df.head()
print(df.columns.tolist())

# Normalize all column names to lowercase
df.columns = df.columns.str.strip().str.lower()

def get_sentiment_score(text):
    return analyzer.polarity_scores(text)['compound']  

# Convert 'review' column to string type and fill missing values
df['review'] = df['review'].astype(str).fillna('')

df['sentiment'] = df['review'].apply(get_sentiment_score)
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'positive' if x > 0.2 else 'negative' if x < -0.2 else 'neutral')

df[['review', 'sentiment', 'sentiment_label']].head()







