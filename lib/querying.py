from math import log, sqrt
from snowballstemmer import FrenchStemmer as fs
from nltk.corpus import stopwords
import re

def cleanQuery(string):
    frenchStopWords = stopwords.words('french')
    p = re.compile('\w+')
    words = p.findall(string)
    words = [word.lower() for word in words]
    words = [fs().stemWord(word) for word in words]
    words = [word for word in words if word not in frenchStopWords]
    return words

def rankDocuments(index, words):
    # We rank each document based on query
    rankings = {}
    for word in words:
        for document in index[word]['document(s)'].keys():
            # Term Frequency (log to reduce document size scale effect)
            TF = index[word]['document(s)'][document]['frequency']
            if TF > 0:
                TF = 1 + log(TF)
            else:
                TF = 0
            # Store scores in the ranking dictionary
            if document not in rankings:
                rankings[document] = TF
            else:
                rankings[document] += TF
    # Order results according to the scores
    rankings = list(reversed(sorted(rankings.items(), key=lambda x: x[1])))
    return rankings

    
