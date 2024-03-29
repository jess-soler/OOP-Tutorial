"""
    name: coin.py
    author: Jessica Soler
    created: 3/28/24
    assignment: 7.4 OOP Tutorial
    puprose: Coin class flips a coin
    and stores which side is up
"""

# import the random module
import random

class Coin:
    # the __init__ method initializes the 
    # _sideup data attribute with "Heads"
    def __init__(self):
        self._sideup = "Heads"
        
    # the toss method generates a random number
    # in the range of 0 through 1
    # 0 = heads
    # 1 = tails
    def toss(self):
        if random.randint(0, 1) == 0:
            self._sideup = "Heads"
        else:
            self._sideup = "Tails"
            
    # returns the value referenced by sideup
    @property
    def sideup(self):
        return self._sideup
    