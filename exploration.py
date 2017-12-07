import json
from nltk.tokenize import word_tokenize
import re
from langdetect import detect
import pandas as pd
import matplotlib.pyplot as plt


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
emoticons_str,
r'<[^>]+>', # HTML tags
r'(?:@[\w_]+)', # @-mentions
r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
r'(?:[\w_]+)', # other words
r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
 return tokens_re.findall(s)

def preprocess(s, lowercase=False):
 tokens = tokenize(s)
 if lowercase:
  tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
 return tokens

# with open('data/stream_godt.json', 'r') as f:
#  for line in f:
#     tweet = json.loads(line)
#     print(json.dumps(tweet, indent=4))
#   tokens = preprocess(tweet)
#   print(tokens)

tweets_data=[]
count=0
text=[]
geo=[]
with open('data/stream_godt.json', 'r') as f:
    for line in f:
        if (count % 2) == 0:
            tweet = json.loads(line)
            if detect(tweet['text'])=='da':
                print(tweet.keys())
                print(tweet['lang'])
                print(tweet['place'])
                text.append(tweet['text'])
                geo.append(tweet['user']['location'])
                tweets_data.append(tweet)
        count+=1
    print(len(tweets_data))
    print(len(geo))
#    print(tweet[0][0])
#    tokens = preprocess(tweet)
#    print(tokens)

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')


# tweets_by_country = tweets['country'].value_counts()
#
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Countries', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
# tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()
print(tweets['text'])