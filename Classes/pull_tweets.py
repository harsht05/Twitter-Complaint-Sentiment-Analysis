import tweepy
import pandas as pd

api_key="dwH2G54Nw25SGP2PyRvb50zu6"
api_secret="sYU3mfpPopw9uKGTnqIWTx7ccBnf92TAVDh6seCVLuk4DE7R2I"
access_token="1344932530953207808-lr4PbJmWlHYKTmm8NZtp6dVYphCEMs"
access_secret="3etQjNJdCyL0osXOmxEY7Gcadh09YrhpEEew2icJZeDTi"

auth=tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)

def pull_tweets(query, co=50):
    tweets = []
    #users = []
    fetch_tweets = api.search(q="#"+query,count=co)
    for w in fetch_tweets:
        parse_tweet = []
        parse_tweet.append(w.text)
        #parse_user = []
        #parse_user.append(w.user)
        if w.retweet_count > 0:
            if parse_tweet not in tweets:
                tweets.append(parse_tweet)
                #users.append(parse_user)
        else:
            tweets.append(parse_tweet)
            #users.append(parse_user)
    return tweets

#Example pull on COVID topic
covid_19 = pd.DataFrame(columns=['tweets'])

covid_19['tweets'] = pull_tweets('covid_19', 300)

print(covid_19['tweets'])