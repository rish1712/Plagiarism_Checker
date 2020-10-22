""" Preprocess """

""" imports here """
from tkinter.constants import NONE
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np

stop = stopwords.words('english') + list(string.punctuation)
import os
import re


class Document:
    """
    class Document
        name   - name of the file
        doc    - contains cleaned doc
        tokens - contains tokens
    """

    def __init__(self, filename, flag=True):
        """
        constructs a Document
            args: filename - Name of the file or a string depending on the flag value
            args: flag     - If true filename treated as name of file else treated as a string
        """
        s = None
        if flag:
            f = open(filename, "r", encoding='ISO-8859-1')
            self.name = os.path.basename(filename)
            s = f.read().lower()
        else:
            s = filename.lower()

        s = re.sub(r'[^\w\s]', '', s)
        self.doc = re.sub(r'[0-9]+', '', s)
        self.tokens = [i for i in word_tokenize(self.doc) if i not in stop]

    def printdoc(self):
        """
            prints the doc
        """
        print(self.doc)


class Corpus:
    """
    Class Corpus encapsulating many documents
    """

    def __init__(self):
        """
            Constructing a corpus
                doclist - list of docs
                vocab   - set of words
                dict    - dictionary for word and its index
                revdict - dictionary for index and its word
                indDoc  - dictionary for Doc and its index
                docind  - dictionary for index and its Doc
        """
        self.doclist = []
        self.vocab = set()
        self.dict = {}
        self.revdict = {}
        self.indDoc = {}
        self.docind = {}

    def addDoc(self, doc):
        """
            adds the doc object to doclist and its corresponding words in vocab
            args: doc (a document object)
        """

        self.doclist.append(doc)
        self.vocab |= set(doc.tokens)

    def makeDocTerm(self):
        """
            makes the document term matrix using doclist and vocab and stores it in matrix (a numpy array)
        """
        voc = list(self.vocab)
        voc.sort()
        for i in range(len(voc)):
            self.dict[voc[i]] = i
            self.revdict[i] = voc[i]
        self.matrix = np.zeros((len(self.doclist), len(voc)))
        for ind, document in enumerate(self.doclist):
            wordlist = document.tokens
            self.indDoc[ind] = document.name
            self.docind[document.name] = ind
            for word in wordlist:
                if word in self.vocab:
                    self.matrix[ind][self.dict[word]] += 1

    def makeIDF(self):
        """
            makes IDF and stores it in dfi (a numpy array)
        """
        voc = list(self.vocab)
        voc.sort()
        boolmat = self.matrix > 0
        n = len(self.doclist)
        dfi = np.sum(boolmat, axis=0)
        dfi = (n * 1.0) / dfi
        dfi = 1 + np.log(dfi)
        self.dfi = dfi.reshape((1, len(voc)))

    def printVocab(self):
        """
            prints the vocab
        """
        print(self.vocab)

    def getDocTerm(self):
        """
            return the document term matrix
        """
        return self.matrix

    def getNumDocs(self):
        """
            returns the number of docs added to the doclist
        """
        return len(self.doclist)

    def getTFIDF(self):
        """
            returns the tfidf matrix
        """
        return self.tfidf

    def getWordList(self):
        """
            get all words as a list
        """
        sz = len(self.revdict)
        lst = []
        for i in range(sz):
            lst.append(self.revdict[i])
        return lst

    def makeTFIDF(self):
        """
            makes tfidf matrix by tf*idf
        """
        matrix = self.getDocTerm()
        tf = np.sum(matrix, axis=1)
        tf = tf.reshape((-1, 1))
        tf = matrix / tf
        dfi = self.dfi
        self.tfidf = tf * dfi

    def run(self):
        """
            this function makes Docterm -> makes IDF -> makes TFIDF
        """
        self.makeDocTerm()
        self.makeIDF()
        self.makeTFIDF()

    def fit(self, doc):
        """
            args: doc (a document object)
            returns : a numpy array of  tfidf vector of the given doc
        """
        matrix = np.zeros((1, len(self.vocab)))
        wordlist = doc.tokens
        for word in wordlist:
            if word in self.vocab:
                matrix[0][self.dict[word]] += 1
        tf = np.sum(matrix, axis=1)
        if tf == 0:
            return None
        tf = tf.reshape((-1, 1))
        tf = matrix / tf
        dfi = self.dfi
        tfidf = tf * dfi
        return tfidf

    def cosineSimilarity(self, query):
        """
            returns a similarity score against all documents for a query
            uses fit to get the vector to multiply with all tfidf vectors already in doclist

        """
        tfidfq = self.fit(query)
        if tfidfq is None:
            return None
        matrix = self.getTFIDF()
        d1 = np.linalg.norm(tfidfq)
        d2 = np.linalg.norm(matrix, axis=1).reshape((-1, 1))
        div = d2 * d1
        res = np.dot(matrix, tfidfq.T) / div
        return res

    def getDocInd(self, name):
        """
            given a docname returns an index of document or None if doesn't exist in doclist
        """
        if name in self.docind:
            return self.docind[name]
        else:
            return None





