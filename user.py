class User:
    def __init__(self):
      self.wrong = 0
      self.letters = ['']
      
    def checkLetter(self, let):
        if let in self.letters:
            print("Letter was already guessed")
            return True
        else:
            print("You guessed letter "+ let)
            self.letters.append(let)
            return False
        
    def getWrong(self):
        return self.wrong
    