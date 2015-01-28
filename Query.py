import sys, os
projectpath = os.path.dirname(os.path.realpath('Storage.py'))
libpath = projectpath + '/lib'
sys.path.append(libpath)
os.chdir(projectpath)
from querying import cleanQuery as clean
from querying import logarithmic as logSearch
from pymongo import MongoClient

# Connect to the database containing inverted indexes
client = MongoClient()
db = client.Inverted_Index

# Choose a folder containing documents
folder = 'New Testament'
collection = db[folder]

# Make a query
query = input('What are you looking for?\n')
words = clean(query)

# Collect the information for each word of the query
index = {}
for word in words:
    index[word] = collection.find({'_id' : word})[0]['info']

# Rank the documents according to the query
logSearch(index, words)


