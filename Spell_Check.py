from spellchecker import SpellChecker

class SpellCheck:
    def __init__(self,misspelled):
        self.text=""
        spell = SpellChecker()
        j=0
        for i in misspelled:
            misspelled[j]=spell.correction(i)
            j+=1
        for i in misspelled:
            self.text+=i+" "

