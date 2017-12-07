import numpy as np
from nltk.corpus import stopwords
import re
import io

das = stopwords.words('danish')
svs = stopwords.words('swedish')
nos = stopwords.words('norwegian')
#print(das)

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

da=[]
sv=[]
no=[]

with io.open('word frequency/da.txt','r',encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines[:80]:
        da_line = preprocess(line)
        da.append(da_line[0])
        # if da[0] not in das:
        #     print(da[0])

with io.open('word frequency/sv.txt','r',encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines[:80]:
        sv_line = preprocess(line)
        sv.append(sv_line[0])

with io.open('word frequency/no.txt','r',encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines[:80]:
        no_line = preprocess(line)
        no.append(no_line[0])

da_exclude=[]
sv_exclude=[]
no_exclude=[]

for da_word in da:
    if da_word not in das and da_word not in sv and da_word not in no:
        da_exclude.append(da_word)

for sv_word in sv:
    if sv_word not in svs and sv_word not in da and sv_word not in no:
        sv_exclude.append(sv_word)

for no_word in no:
    if no_word not in nos and no_word not in da and no_word not in sv:
        no_exclude.append(no_word)

print(da_exclude)
print(sv_exclude)
print(no_exclude)