import sys, os
projectpath = os.path.dirname(os.path.realpath('Storage.py'))
libpath = projectpath + '/lib'
sys.path.append(libpath)
os.chdir(projectpath)
import parsing
import re
import time

# Indexing
startTime = time.time()
index = {}
# What collection to index?
collection = 'New Testament'
# Indicate the path where relative to the collection
os.chdir(projectpath + '/data/' + collection)
# List all files in the collection
files = [file for file in os.listdir('.') if os.path.isfile(file)]
# Iterate through every file
for file in files:
    # Split the file in lines
    data = open(file).read().splitlines()
    # Normalize the content
    words = parsing.clean(data)
    # Remove the extension from the file for storage
    name = re.match('(^[^.]*)', file).group(0)
    # Add the words to the index
    parsing.index(name, words, index)
print("Indexation took " + str(time.time() - startTime) + " seconds.")

# Storage
startTime = time.time()       
parsing.store(index, collection)
print("Storage took " + str(time.time() - startTime) + " seconds.")
