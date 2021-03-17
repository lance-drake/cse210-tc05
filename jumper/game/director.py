class Director:
    '''
    Director Class
    '''

    def __init__(self):
        self.guess=[]
        self.word=''

    def start_game(self):
        pass


    def find_index(self, new_guess):
        self.guess.append(new_guess)
        return [i for i, ltr in enumerate(self.word) if ltr == new_guess]



