# from nltk.corpus import stopwords
# sr = stopwords.words('norwegian')
# print(sr)

# import sys
# print(sys.getdefaultencoding())


# import json
#
# tweet=[]
# with open('data/stream_godt.json', 'r') as f:
#     for line in f:
#         tweet.append(line)
#     print(json.dumps(tweet, indent=4))
#     print(tweet)

#   line = f.readline() # read only the first tweet/line
#   tweet = json.loads(line) # load it as Python dict
# # print(json.dumps(tweet, indent=4)) # pretty-print
#   #print(tweet.keys())
#   print(tweet['text'])
#   print(tweet['geo'])

from langdetect import detect

if detect("godt dage") == 'da':
    print('damark')
