

import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    def __init__(self, color, dinos, leaves, feet, sides=6):
        self.color = color
        self.dinos = dinos
        self.leaves = leaves
        self.feet = feet

    def __str__(self):
        return 'A '+str(self.color)+' die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        Die.roll()

    def get_top(self):
        Die.get_top()

    def set_top(self):
        random.randrange()

class DinoPlayer:

    def __init__(self, name):
        self.name = name



def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    red_die = DinoDie("red", 1, 2, 3)
    yellow_die = DinoDie("red", 2, 2, 2)
    green_die = DinoDie("red", 3, 2, 1)



