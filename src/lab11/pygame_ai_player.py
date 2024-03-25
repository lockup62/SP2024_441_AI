import pygame
import random
from lab11.turn_combat import CombatPlayer

class PyGameAIPlayer:
    def __init__(self):
        pass

    def selectAction(self, state):
        #this lets the ai move to each city as long as its not at the last city
        if state.current_city == 10:
            return None
        else:
            #this returns the ascii value of whatever the city index is at
            return ord(str(state.current_city+1))

class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        self.weapon_select=random.randint(0,2)
        return self.weapon_select
