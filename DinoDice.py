

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
        Die.__init__(self, range(1,sides))

    def __str__(self):
        return 'A '+str(self.color)+' die with '+\
               str(self.get_top())+' on top'


    def get_top(self):
        Die.get_top()
        return self.top

class DinoPlayer:

    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def add_points(self, points):
        self.score += points

    def roll_dice(self):
        while True:
            user_roll = input("Press enter to roll 3 random dice.")
            if user_roll == "":
                break
            else:
                print("Please type enter.")
        random_dice = random.sample(dices,3)
        results = []
        for dice in random_dice:
            rolled_values = dice.roll()
            results.append(rolled_values)
        return results


def play_dino_hunt(): 
    numPlayers = int(input("How many players are playing?"))
    numRounds = int(input("How many rounds would you like to play?"))
    names = {}
    players = {}
    for x in range(1, numPlayers+1):
        player_name = input(f"What is player{x}'s name?")
        names[player_name] = 0
        players[player_name] = DinoPlayer(player_name)
    print(players)
    print(players['jason'])
    print(players['jason'].name)
    print(players['jason'].score)


    

    for g in range(6):
        dices.append(DinoDie('green', 3, 2, 1, sides=6))

    for y in range(4):
        dices.append(DinoDie('yellow', 2, 2, 2, sides=6))
    
    for r in range(3):
        dices.append(DinoDie('red', 1, 2, 3, sides=6))

    print(dices)
    print(len(dices))

    for dice in dices:
        print(dice['sides'])



    for playerName, player in players.items():
        print(playerName)
        results = player.roll_dice()
        print(results)



dices = []
numDice = 13

play_dino_hunt()
    
""" scoreCard = {"tony":{"1":0,"2":4,"3":0},"jason":{"1":0,"2":4,"3":0}}    
print(scoreCard)   
    
scoreCard2 = {}
scoreCard2['tony'] = {}
scoreCard2['tony'][1] = 0;

print(scoreCard2)
 """


