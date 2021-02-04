[![All Contributors](https://img.shields.io/badge/Contributors-3-green.svg?style=flat-square)](#contributors-)
# RealTime-Twitter-Sentiment-Analysis
  A **_Real-time Twitter sentiment analysis_** showcased with the help of **Twitter API's** , **NLTK** and **WORD2VEC**
  
  **You can visit our website [here](https://twitter-sentiment-analysis-znv.herokuapp.com/ "Twitter-Sentiment-Analysis")**
## Live Demo
  ![Home page](home.png)
  - You will see this home page on visiting the site.
  - Select any topic:
    - **COVID**
    - **BTS**
    - **UEFA**
    - **REACT**
    - **BCCI**
  - On selecting any topic, suppose say **UEFA**, it will open sentiment analysis on **UEFA**
  ![Uefa page](uefa.png)
  - On the left side, we have chart depicting the percentage of tweets sentiment for over an year.
  - On the right side, we see a text bar, where u can enter tweet to find its sentiment percentage.
  ![bottom tweets](bottom_tweets.png)
  - Scroll down to bottom to see live tweets with its sentiment emoji at right. 

## Technologies Used
### 1. Tweepy API
![Tweepy API](https://twilio-cms-prod.s3.amazonaws.com/images/twitter-python-logos.width-808.jpg "Tweepy API")
 - _Tweepy is an open source Python package that gives you a very convenient way to access the Twitter API with Python._
 - It's easy to understand its documentation [here](https://docs.tweepy.org/en/latest/api.html "docs.tweepy.org") 
 - We used this API for live pulling of tweets and showcasing them on live website

### 2. Twint API
![Twint API](https://jakecrepscom.files.wordpress.com/2019/06/untitled-design-1.png?w=640 'Twint API')
  - _"Twint is an advanced tool for Twitter scrapping. We can use this tool to scrape any user’s followers, following, tweets, etc. without having to use Twitter API"._
  - You can check out more about **TWINT API** [here](https://github.com/twintproject/twint "ProjectTwint")
  - In this project, we extracted over 3 lakh tweets for 5 topics via **Twint API** ranging from start of **2020** to present date
  - **Twint API** is more preferable than **Tweepy API** because of its many benifits
    - **Twitter API** has restrictions to scrape only the **last 3200 Tweets**. But Twint can fetch almost **all Tweets.**
    - Set up is really quick as there is no hassle of setting up Twitter API.
    - Can be used **anonymously** without Twitter sign-up.
    It’s free!! No pricing limitations.

### 3. NLTK
  - **NLTK** also known as **Natural Language Toolkit** is the library used mainly for _Natural Language text processing_
  - 
### 4. Gensim's Word2Vec model
### 

We performed the Analysis for the last 1 year and found out the percentage of positive,negative and neutral tweets in the last 1 year.

## Deployment
A basic responsive Flask App which is designed using HTML,CSS, basic JavaScript and Python\
Used ChartJS for better visualisation of Data\
Used TextBlob for getting the sentiment of a user input tweet and visualising the percentage using ChartJS\
Depoyed using Heroku

Link : [Visit our website](https://twitter-sentiment-analysis-znv.herokuapp.com/ "Twitter-Sentiment-Analysis")
