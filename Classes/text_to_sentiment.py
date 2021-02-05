#Import Libraries
import numpy as np
import pandas as pd
import nltk.corpus
import string
import re
from textblob import TextBlob

stop_words = nltk.corpus.stopwords.words('English')

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
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'Positive Percentage: ' + str(analysis.sentiment.polarity * 100)
        elif analysis.sentiment.polarity == 0: 
            return 'Neutral tweet'
        else: 
            return 'Negative Percentage: ' + str(analysis.sentiment.polarity * 100)

# Taking input from User
user_input = input("Enter your tweet to calculate its sentiment")

sentiment = get_tweet_sentiment(user_input)
cleaned_tweet = text_process(user_input)

#Printing its Sentiment along with cleaned_tweet
print("Your tweet:",user_input,"\nCleaned Tweet:",cleaned_tweet,"\nSentiment:",sentiment)