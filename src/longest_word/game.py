"""Module used to randomized characters"""
import random
import string
import dataclasses


@dataclasses.dataclass
class Game:
    """This is the game class there's nothing to say about it but pylint wants it"""
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word):
        """check if word is a valid answer"""
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
