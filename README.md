[![All Contributors](https://img.shields.io/badge/Contributors-3-green.svg?style=square)](#contributors-) [![All Technologies](https://img.shields.io/badge/Technologies-4-orange.svg?style=square)](#technologies-)
# RealTime-Twitter-Sentiment-Analysis
  A **_Real-time Twitter sentiment analysis_** showcased with the help of **Twitter API's** , **NLTK** and **WORD2VEC**
  
  **Visit our Website [here](https://twitter-sentiment-analysis-znv.herokuapp.com/ "Twitter-Sentiment-Analysis")**

---
## Live Demo
  <p align='center'><img src='./Readme/home.png' width=75%><img src='./Readme/mobile_home.png' width=25%></p>

  - You will see this home page on visiting the site via Desktop and Mobile.
  - Select any topic:
    - **COVID**
    - **BTS**
    - **UEFA**
    - **REACT**
    - **BCCI**
  - On selecting any topic, suppose say **UEFA**, it will open sentiment analysis on **UEFA**
  <p align='center'><img src='./Readme/uefa.png' width=75%><img src='./Readme/uefa_mobile.png' width=25%></p>

  - On the left side, we have chart depicting the percentage of tweets sentiment for over an year.
  - On the right side, we see a text bar, where u can enter tweet to find its sentiment percentage.
  - Bottom to the text bar, you see live tweets with its sentiment emoji at right. 
  - Enter any tweet in the tweet bar to check its sentiment percentage
  <p align='center'><img src="./Readme/uefa_tweet.png" alt="drawing" width=75%/><img src="./Readme/uefa_tweet_mobile.png" alt="drawing" width=25%/></p>

---
## Technologies Used
### 1. Tweepy API
 - _Tweepy is an open source Python package that gives you a very convenient way to access the Twitter API with Python._
 - It's easy to understand its documentation [here](https://docs.tweepy.org/en/latest/api.html "docs.tweepy.org")
 - To start pulling tweets from tweepy, you need to install tweepy using `!pip install tweepy` and then import as follows: 
 ```python
  import tweepy

  auth=tweepy.OAuthHandler(api_key,api_secret)
  auth.set_access_token(access_token,access_secret)
  api=tweepy.API(auth,wait_on_rate_limit=True)
 ```
- To authorize API, you need to create a **Twitter Developer Account** from [here](https://developer.twitter.com/ "Twitter Developer")
- We used this API for live pulling of tweets and showcasing them on live website
```python
def pull_tweets(query, co=50):
    fetch_tweets = api.search(q="#"+query,count=co)
```
 - To check out full code, click [here](https://github.com/Zeph-T/RealTime-Twitter-Sentiment-Analysis/blob/main/Classes/pulling_tweets.ipynb)
---
### 2. Twint API
  - _"Twint is an advanced tool for Twitter scrapping. We can use this tool to scrape any user’s followers, following, tweets, etc. **without having to use Twitter API**"._
  - You can check out more about **TWINT API** [here](https://github.com/twintproject/twint "ProjectTwint")

  - **Twint API** is more preferable than **Tweepy API** because of its many benifits
    - No restriction in scrapping tweets
    - No hassle in setting up
    - Can be used **anonymously** without Twitter sign-up.
  
  - In this project, we extracted over **3 lakh tweets for 5 topics** via **Twint API** ranging from start of **2020** to present date.
---
### 3. NLTK
  - **NLTK** also known as **Natural Language Toolkit** is the library used mainly for _Natural Language text processing_
  - **NLTK** is used for data cleaning and removal of unnecessary words which doesn't make sense.
  - We use NLTK's stopwords and lemmatizer to clean the unwanted part of tweets.
  ``` python
  from nltk.corpus import stopwords
  from nltk.stem import WordNetLemmatizer
  
  lemm = WordNetLemmatizer()

  stop_words = stopwords.words("english")
  ```
  - You can check out whole data cleaning of tweets [here](https://github.com/Zeph-T/RealTime-Twitter-Sentiment-Analysis/blob/main/Classes/Data_cleaning.ipynb "Data Cleaning.ipynb")
---
### 4. Gensim's Word2Vec model

  - After cleaning of Raw tweets, they are passed into Word2Vec model
  - We import Gensim's Word2Vec model as follows
  ```python
  from gensim.models.phrases import Phrases, Phraser
  from gensim.models import Word2Vec
  from gensim.test.utils import get_tmpfile
  from gensim.models import KeyedVectors
  ```
  - Model is set to the following parameters
  ```python
  w2v_model = Word2Vec(min_count=3,
                     window=4,
                     size=300,
                     sample=1e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=20,
                     )

w2v_model.build_vocab(sentences, progress_per=50000)
  ```
  For full code of how to build Word2Vec model, click [here](https://github.com/Zeph-T/RealTime-Twitter-Sentiment-Analysis/blob/main/Classes/Word2vec_model_traning.ipynb)

---
### 5.  KMeans Clustering
  - The obtained vector forms of words from Word2Vec model are processed next into **KMeans** to divide it into 3 clusters and sentiment score of corresponding cluster is saved as per the cluster value.
  - The parameters of the KMeans is as follows
    ```python
    model = KMeans(n_clusters=3, max_iter=1000, random_state=True, n_init=50).fit(X=word_vectors.vectors.astype('double'))
    ```
  - To view the full code of KMeans, click [here](https://github.com/Zeph-T/RealTime-Twitter-Sentiment-Analysis/blob/main/Classes/KMeans.ipynb "KMeans.ipynb")

---
### 6. Tf-Idf Vectorizer
  - **Tf-Idf Vectorizer** is applied on the cleaned dataset to calculate the tf-idf score of every word and is combined with the previous sentiment score
  - Import **Tf-Idf vectorizer** as follows
  ```python
  from sklearn.feature_extraction.text import TfidfVectorizer
  ```
  - You can view the full code of how we utilized Tf-Idf [here](https://github.com/Zeph-T/RealTime-Twitter-Sentiment-Analysis/blob/main/Classes/Predictions.ipynb "Predictions.ipynb")    

---
## Deployment

A basic responsive Flask App which is designed using:
  - HTML,CSS
  - Basic JavaScript and Python
  - Used ChartJS for better visualisation of Data
  - Visualising the percentage using ChartJS\
  - Depoyed using Heroku
---
## Setting up the Project
  1. Clone the repo
  ```python
  git clone https://github.com/Zeph-T/RealTime-Twitter-Sentiment-Analysis.git
  ```
  2. Navigate to Flask Folder, create a virtual environment
  ```python
  python3 -m venv <your_environment_name>
  ```
  3. Activate the virtual environment using the following command
  ```python
  Source <environment name>/bin/activate
  ```

  4. Install all the required Packages using the command
  ```python
  pip install -r requirements.txt
  ```
  5. Run the .py file
  ```python
  run python3 app.py
  ```