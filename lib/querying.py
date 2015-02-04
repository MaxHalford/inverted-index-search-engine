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

def logarithmic(index, words):
    # Assign weights to the words
    weights = [1] * len(words)
    # We rank each document based on query
    rankings = {}
    for word in words:
        # Inverted Document Frequency (independent from number of documents)
        DF = index[word]['document frequency']
        DF = 1 / DF
        for document in index[word]['document(s)'].keys():
            # Term Frequency (log to reduce document size scale effect)
            TF = index[word]['document(s)'][document]['frequency']
            if TF > 0:
                TF = 1 + log(TF)
            else:
                TF = 0
            # Store scores in the ranking dictionary
            if document not in rankings:
                rankings[document] = TF * DF
            else:
                rankings[document] += TF * DF
    # Order results according to the scores
    rankings = sorted(rankings.items(), key=lambda x: x[1])
    return rankings

# #def logarithmic(index, words):
# #    # Assign weights to the words
# #    weights = [1] * len(words)
# #    # We rank each document based on query
# #    docRanking = {}
# #    for word in words:
# #        # Inversed Document Frequency (independent from number of documents)
# #        DF = index[word]['document frequency']
# #        DF = 1 / DF
# #        for document in index[word]['document(s)'].keys():
# #            # Term Frequency (log to reduce document size scale effect)
# #            TF = index[word]['document(s)'][document]['frequency']
# #            if TF > 0:
# #                TF = 1 + log(TF)
# #            else:
# #                TF = 0
# #            # Store scores in the ranking dictionary
# #            if document not in docRanking:
# #                docRanking[document] = {}
# #                docRanking[document]['wordScores'] = [TF * DF]
# #                docRanking[document]['RFS'] = 0
# #            else:
# #                docRanking[document]['wordScores'].append(TF * DF)
# #    # Compute the scores thanks to linear algebra
# #    for document in docRanking:
# #        docScores = docRanking[document]['wordScores']
# #        # Dot product
# #        dotProduct = sum([docScores[i] * weights[i] for i in range(len(weights))])
# #        # Vector euclidian norms
# #        docNorm = sqrt(sum([score ** 2 for score in docScores]))
# #        queryNorm = sqrt(sum([weight ** 2 for weight in weights]))
# #        # Cosine distancce
# #        docRanking[document]['RFS'] = dotProduct / (docNorm * queryNorm)
# #    # Display ordered results in a neat way
# #    pp = pprint.PrettyPrinter()
# #    pp.pprint(docRanking)

    
