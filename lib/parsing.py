from snowballstemmer import FrenchStemmer as fs
from nltk.corpus import stopwords
import re
from pymongo import MongoClient

client = MongoClient()
db = client.Inverted_Index

frenchStopWords = stopwords.words('french')
p = re.compile('\w+')

def clean(data):
    # Concatenate the lines into a big string
    words = [word for word in ' '.join(data).split(' ')]
    # Search every word in the big string
    words = p.findall(' '.join(words))
    # Lower case
    words = [word.lower() for word in words]
    # Stem word
    words = [fs().stemWord(word) for word in words]
    # Remove stop words
    words = [word for word in words if word not in frenchStopWords]
    # Done!
    return words

def index(file, words, index):
    for position in range(len(words)):
        word = words[position]     
        # If the word is not in the index
        if words[position] not in index:
            index[word] = {'term frequency' : 1,
                           'document frequency' : 1,
                           'document(s)' : {file : {'frequency' : 1,
                                                  'position(s)' : [position]
                                                  }
                                          }
                           }
        # If the word is in the index
        else:
            index[word]['term frequency'] += 1
            # If the word has not been found in this document
            if file not in index[word]['document(s)']:
                index[word]['document frequency'] += 1
                index[word]['document(s)'][file] = {'frequency' : 1,
                                                  'position(s)' : [position]}
            # If the word has been found in this document
            else:
                 index[word]['document(s)'][file]['frequency'] += 1
                 index[word]['document(s)'][file]['position(s)'].append(position)
    return index

def store(index, folder):
    collection = db[folder]
    for word in index:
        collection.save({'_id' : word, 'info' : index[word]})
    
    
