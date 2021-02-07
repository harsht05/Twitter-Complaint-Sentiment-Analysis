from flask import Flask,render_template,request
from Classes.text_to_sentiment import text_process,get_tweet_sentiment
from Classes.pull_tweets import pull_tweets
from Classes.data import sentiment_data

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/<topic>",methods=["GET","POST"])
def page(topic):
    if request.method =="GET":
        title=topic.upper()
        temp=pull_tweets(topic)
        tweets=[]
        for tweet in temp:
            tweets.append(*tweet)
        f_tweets=[]
        final_tweets=[]
        for tweet in tweets:
            a=(text_process(tweet))
            f_tweets.append([1 if get_tweet_sentiment(a)>0 else 2 if get_tweet_sentiment(a)<0 else 0])
        for Sentiment in f_tweets:
            final_tweets.append(*Sentiment)
        length=len(final_tweets)
        return render_template("template.html",sentiment=final_tweets,tweets=tweets,length=length,name=topic.capitalize(),sentiment_data = sentiment_data[topic],title=title)
    else:
        tweet=request.form["Area"]
        Cleaned_Tweet=text_process(tweet)
        sentiment=get_tweet_sentiment(Cleaned_Tweet)
        if(sentiment>0):
            emo="POSITIVE"
            sentiment=int(sentiment)
            icon="../static/pictures/postive.png"
        elif sentiment==0:
            emo="NEUTRAL"
            icon="../static/pictures/neutral.png"
        else:
            emo="NEGATIVE"
            sentiment=int(abs(sentiment))
            icon="../static/pictures/angry.png"
        tweet=tweet.upper()
        sentiment=str(sentiment)
        return render_template("tweet.html",sentiment=sentiment,icon=icon,tweet=tweet,emo=emo)


if(__name__=="__main__"):
    app.run(debug=True)
