#Import Libraries
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re
from textblob import TextBlob
nltk.download("punkt")
stop_words = stopwords.words('english')

#Cleaning tweet
def text_process(tweet):
    tweet.lower()
    #Remove Urls
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    #Remove @ mentions
    tweet = re.sub(r'\@\w+|\#','', tweet)
    #Remove Emojis
    emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
    emoji_pattern.sub(r'', tweet) # no emoji
    #Remove punctuation
    tweet = [char for char in tweet if char not in string.punctuation]
    tweet = ''.join(tweet)
    #Remove Stopwords
    tweet_tokens = nltk.word_tokenize(tweet)
    filtered_tweet = [tokens for tokens in tweet_tokens if tokens not in stop_words]
    filtered_tweet = ' '.join(filtered_tweet)
    return filtered_tweet

#Analysing sentiment of a tweet
def get_tweet_sentiment(tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(text_process(tweet)) 
        return (analysis.sentiment.polarity * 100)
