# Plagiarism_Checker
The aim of this Project is to develop a small version of a Plagiarism Checker. The major task is to build a plagiarism checker which will rank documents based on similarity. The Plagiarism Checker developed by us takes the user’s query in form of text file or raw data and fetches the documents from where the data has been copied based on vector space model of information retrieval. It preprocesses documents and indexes it for future use. Vector Space Model is used to retrieve the required  output based on user's query.We have used tf-idf ranking method to compute the vector for every document and query. 

#### Dependencies:-

1) IRFINAL/Preprocess.py: 2,4,5
nltk == 3.5

2) IRFINAL/Preprocess.py: 6
numpy == 1.18.4

3) IRFINAL/Preprocess.py: 8
pandas == 1.0.3

4) IRFINAL/Spell_Check.py: 1
spellchecker == 0.4

5) pyspellchecker == 0.5.5

All the above specified libraries should be installed in your system\enviorment by using pip.

#### Compilation:-

Any IDE suitable for compiling python files can be used. A python verison of 3.* is preffered as pip is pre installed in it.

#### Running:-
After sucessfully compiling the above project a User Interface will pop up. The dataset has to be added in the software. This can be done by using the "Enter the pth for documents to be preprocessed" Button. It takes the destination folder for the dataset (buisness in our case). After additon all the files are prprocessed and normalized. The user can input a query in the form of raw text or a text file and has to input the corresponding upper bound of plagriasm content he wants to check. The software returns the list of all the files which staisfy the users query in decreasing order. 


## Authors
* [Rishab Nahar]
* [Nipun Wahi]
* [Samkit Jain]
* [Aditya Pandey]
