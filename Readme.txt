Dependencies:-

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

Compilation:-

Any IDE suitable for compiling python files can be used. A python verison of 3.* is preffered as pip is pre installed in it.

Running:-
After sucessfully compiling the above project a User Interface will pop up. The dataset has to be added in the software. This can be done by using the "Enter the pth for documents to be 
preprocessed" Button. It takes the destination folder for the dataset (buisness in our case). After additon all the files are prprocessed and normalized. The user can input a query in the
form of raw text or a text file and has to input the corresponding upper bound of plagriasm content he wants to check. The software returns the list of all the files which staisfy the users 
query in decreasing order. 
 