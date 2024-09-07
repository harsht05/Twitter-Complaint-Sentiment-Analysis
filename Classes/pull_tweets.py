import tweepy
import pandas as pd

api_key="El9D6nRuk029XbsXrHrCEnrO5"
api_secret="xdlnIz5gw2IHZX6cocotoh4G1bpBqM65W57gkOsoGa1wjKz1ld"
brerear_token = r"AAAAAAAAAAAAAAAAAAAAAM%2FlhwEAAAAAXPAgTTwb9PSLaVwlxJoJ7U2QAEU%3DcOI1qCd2OetwcPlCkTH8Ff3LWc4NO1IWuDb02F21T5TSrz7wd7"
access_token="1344932530953207808-lr4PbJmWlHYKTmm8NZtp6dVYphCEMs"
access_secret="3etQjNJdCyL0osXOmxEY7Gcadh09YrhpEEew2icJZeDTi"

auth=tweepy.OAuthHandler(api_key,api_secret)
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