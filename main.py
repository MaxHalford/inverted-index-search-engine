import sys, os
projectpath = os.path.dirname(os.path.realpath('main.py'))
libpath = projectpath + '/lib'
sys.path.append(libpath)
os.chdir(projectpath)
from PyQt4 import QtCore, QtGui
from browser import Ui_MainWindow
from querying import cleanQuery, rankDocuments
from pymongo import MongoClient

# Connect to the database containing inverted indexes
client = MongoClient()
db = client.Inverted_Index
# Choose a folder containing documents
folder = 'New Testament'
collection = db[folder]

class browser(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect the query function with the search button
        self.ui.pushButton.clicked.connect(self.query)
    def query(self):
        # Empty the list
        self.ui.listWidget.clear()
        # Get the words in the query
        words = cleanQuery(self.ui.lineEdit.text())
        # Collect the information for each word of the query
        index = {}
        for word in words:
            index[word] = collection.find({'_id' : word})[0]['info']
        # Rank the documents according to the query
        results = rankDocuments(index, words)
        for result in results:
            self.ui.listWidget.addItem(result[0]+' : '+str(round(result[1], 2)))
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = browser()
    myapp.show()
    sys.exit(app.exec_())
