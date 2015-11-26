import codecs
from nltk.corpus import stopwords
import re
import json
import sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

stop_word = open('stopwords_id.txt','r')
list_stopword = stop_word.read().split(',')
#list_stopword = stop_word.readlines()
stop = stopwords.words('english')
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
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

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

with open('jokowi.txt', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens=preprocess(tweet['text'])
        removed_stopword = [term for term in tokens if term not in list_stopword]
        #print(removed_stopword)
print(stop)
print(list_stopword)