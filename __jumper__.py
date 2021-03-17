"""
The game package contains specific classes for playing Jumper.
"""
class Jumper():
    def __init__(self):
        self.life = 4
        self.guess = ""
        self.prevGuesses = []
    
    def checkGameOver(self):
        if self.life <= 0:
            self.gameOver()
            return
        else:
            return

    # Stores the player's guess
    def makeGuess(self):
        #Stores the guess
        self.guess = input("Guess a letter [a-z] : ")

        #If the guess is longer than 1 character, it displays an error
        if len(self.guess) > 1:
            print("Guess a single letter.")
            self.makeGuess()
            return
        #If this guess has been made before it cuts a string
        elif self.guess in self.prevGuesses:
            print("You have guessed that letter before.")
            display.cutString()
            self.life -= 1
            return
        #If it's a new guess and it's valid, it goes through.
        else:
            self.prevGuesses.append(self.guess)
            director.checkGuess()
            return
    # Calls the game over function from director to end the game.
    def gameOver():
        director.gameOver():




