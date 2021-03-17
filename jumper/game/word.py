import random
import textwrap

class Word:
    def random_word():
        with open("wordlist.10000.txt", "rt") as file:
            string=file.read()
            quotes=string.splitlines()
            random_quotes=random.choice(quotes)
        