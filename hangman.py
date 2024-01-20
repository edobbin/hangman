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
        while self.user.wrong < 6:
            
            print("Pick a letter: ")
            x = input()
            temp = self.user.checkLetter(x)
            if x is True:
                continue
            else:
                if self.word.find(x) !=-1:
                    self.printWord()
                else:
                    self.user.isWrong()
                    chance = 6-self.user.getWrong()
                    print("You guessed the wrond letter, try again\nYou have "+str(chance)+ " chances left.")
            
            
        
    
        
h = hangman()
h.hangman()