class Director:
    self.guess=[]
    self.word=''
    
    def __init__(self):
        self.guess=[]
        self.word=''

    def start_game(self):
        pass


    def find(self, guess):
        self.guess.append(guess)
        return [i for i, ltr in enumerate(self.word) if ltr == guess]



