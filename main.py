import os
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt


from textblob import TextBlob
# keys and tokens from the Twitter Dev Console
from tweepy import OAuthHandler

# PSA: please input your Twitter API keys, secrets and tokens here
consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'
# attempt authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#jetblue"
date_since = "2019-09-12"
# Collect tweets
tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(10)
positive = 0
neutral = 0
negative = 0
for t in tweets:
    analysis = TextBlob(t.text)
    if analysis.sentiment.polarity > 0:
        positive += 1
    elif analysis.sentiment.polarity == 0:
        neutral += 1
    else:
        negative += 1

print(f"Number of positive tweets about {search_words}: {positive}")
print(f"Number of neutral tweets about {search_words}: {neutral}")
print(f"Number of negative tweets about {search_words}: {negative}")

s = pd.Series({"Positive": positive, "Neutral": neutral, "Negative": negative})
print(s)
s.plot.bar()
plt.show()
"""
search_words = "#jetblue"
date_since = "2019-09-12"
# Collect tweets
tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(10)
positive = 0
neutral = 0
negative = 0
for t in tweets:
    analysis = TextBlob(t.text)
    if analysis.sentiment.polarity > 0:
        positive += 1
    elif analysis.sentiment.polarity == 0:
        neutral += 1
    else:
        negative += 1
print(f"Number of positive tweets about {search_words}: {positive}")
print(f"Number of neutral tweets about {search_words}: {neutral}")
print(f"Number of negative tweets about {search_words}: {negative}")
"""