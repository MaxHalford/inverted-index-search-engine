<<<<<<< d8d0c578f026e06cf7ac2487ed4a52aaf7cdd816
# Inverted-Index
An inverted index is the basis of any search engine. I made this in preparation of the search engine my school assigned us in 2015. In this example I indexed the New Testament and stored the index with MongoDB (which proved perfect for this use case!). I implemented a very simple search engine, it returns a list of documents (in this case chapters of the New Testament) with a score assigned to each document based on the query. The UI is based on PyQt so you will have to download Qt Designer in order to modify everything related to the UI but also to launch it, indeed I haven't compiled it into an independant application.
=======
# Inverted index

## Theory

An inverted index is a data structure that indicates which documents contain a given word. In other words the inverted index contains the frequencies of each words in each document.

The first step is to index a collection of documents to build the inverted index. Once the inverted index is stored, queries can be parsed and compared to each document to return pertinent results.

In this case I simply computed the base logarithm of the summed up frequencies of each word of the query. However more sophisticated models exist (this wasn't the point of this project). Check out the [Perl search engine](https://github.com/MaxHalford/Wikisid) I coded for more advanced scoring methods.

## Database

The inverted indexs are stored as JSON files with MongoDB. Sadly if you want this run you will have to install MongoDB on your computer. You don't have to know *anything* about MongoDB to run this yourself. However if you are interested in MongoDB please check out the [IPython notebook tutorial](http://maxhalford.com/resources/notebooks/genetic-algorithms) I wrote.

## Interface

For the interface I used Qt. There is a very useful tool called QtDesigner where you can design your interface with a point-and-click interface. Once saved this produces a .ui file which you can convert to python with the ``uiToPython.sh`` script. This produces a python file which contains a class (normally called ``Ui_MainWindow``) with which you will have to work. The philosophy is that you connect interfaces actions (button clicks, scrolling, etc.) with python function.

## Example

As an example I parsed the New Testament. The following image is a query example with the list of pertinent documents.

![Example](example.png)

## Running it yourself

- Install MongoDB, Python3, Qt.
- Run ``Storage.py`` to store the files in ``data/New Testament`` in MongoDB.
- Run main.py.
- Profit!
>>>>>>> dcb01928e071379626fd6345f7d3128450edc979
