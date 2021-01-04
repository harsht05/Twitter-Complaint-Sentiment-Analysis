search_words="BTS_twt"
date_since=["2020-1-1","2020-2-1","2020-3-1","2020-4-1","2020-5-1","2020-6-1","2020-7-1","2020-8-1","2020-9-1","2020-10-1","2020-11-1","2020-12-1"]
date_until=["2020-1-31","2020-2-30","2020-3-31","2020-4-30","2020-5-31","2020-6-30","2020-7-31","2020-8-31","2020-9-30","2020-10-31","2020-11-30","2020-12-31"]

tweets_data=[]

for month in range(12):
    tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           lang="en",
                           since=date_since[month],
                           until=date_until[month]).items(200)
    month_tweets=[]
    for tweet in tweets:
        if tweet.text not in tweets_data:
            month_tweets.append(tweet.text)
    tweets_data.append(month_tweets)
