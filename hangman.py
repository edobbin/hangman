from user import User
import random


class hangman:
    def genWordBank(self):
        f = open('wordlist.txt', 'r')
        for x in f:
            self.wordBank.append(x)
    
            
    def __init__(self):
        self.user = User()
        self.wordBank = []
        
        self.genWordBank()
        self.word = random.choice(self.wordBank)
    
    def printWord(self):
        fin = ""
        for x in self.word:
            if x in self.user.letters:
               fin += x+" "
            else:
                fin+= "_ "
        print(fin)
                
    def hangman(self):
        self.printWord()
        # while self.user.wrong < 6:
            
        
    
        
h = hangman()
h.hangman()