class Director:
    '''
    Director Class
    '''

    def __init__(self):
        self.guess=[]
        self.word=''

    def start_game(self):
        pass


    def find_index(self, guess):
        self.guess.append(guess)
        return [i for i, ltr in enumerate(self.word) if ltr == guess]



