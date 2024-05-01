# From https://codereview.stackexchange.com/questions/237601/simple-python-turn-based-battle-game
import random
import pygame
import sys
from pathlib import Path
from ollama import Ollama
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab4.rock_paper_scissor import Player

weapons = ["Sword", "Arrow", "Fire"]
ollama = Ollama()

def generate_ai_response(input_text):
    # Generate embedding for input text
    input_embedding = ollama.embed_sentence(input_text)

    # Calculate cosine similarity between input text and each sentence
    similarities = {}
    for sentence, embedding in sentence_embeddings.items():
        similarity = cosine_similarity([input_embedding], [embedding])[0][0]
        similarities[sentence] = similarity

    # Sorting
    sorted_sentences = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    # Getting top 3 most similar sentences
    top_sentences = sorted_sentences[:3]

    # Building the query prompt
    query_prompt = "CONTEXT:\n\n"
    for sentence, _ in sorted_sentences:
        query_prompt += sentence + "\n\n"

    query_prompt += "QUERY:\n\n"
    query_prompt += input_text + "\n\n"

    # Generate response
    response = ollama.generate(query_prompt)
    
    return response
class CombatPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.health = 100
        self.weapon = 0
        self.current_env_state = None
        input_text = "say something as if you just approached me in battle"
      # Output the AI response
        ai_response = generate_ai_response(input_text)

    def selectAction(self, percept):
        """
        > The function takes in the opponent's last move, updates the player's history of opponent's moves,
         and then updates the player's history of their own moves

        :param percept: Tuple of (environment state, opponent's last move)
        """
        env_state = percept
        # ** Previous round update **
        if percept is not None:
            self.current_env_state = env_state

        # ** Current round update **
        self._action = self.weapon_selecting_strategy()
        self.weapon = self._action
        self.my_choices.append(self.action)

    def damage(self):
        points = 10
        self.health -= points

    def weapon_selecting_strategy(self):
        choice = input("Choose your weapon s-Sword, a-Arrow or f-Fire:  ")
        choice = {"s": 1, "a": 2, "f": 3}[choice]
        self.weapon = choice - 1
        return self.weapon


class ComputerCombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        choice = random.randint(1, 3)
        self.weapon = choice - 1
        return self.weapon


class Combat:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print("\n***   Round: %d   ***\n" % (self.round))

    # Check if either or both Players is below zero health
    def checkWin(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            self.gameOver = True
            print("You Lose")
            player.money += 20  
            print(f"Player's money: {player.money}")   
            return -1
        elif opponent.health < 1 and player.health > 0:
            self.gameOver = True
            print("You Win")
            if isinstance(player, PyGameHumanCombatPlayer):  # Check if the player is human
                player.money += 20  
                print(f"Player's money: {player.money}")
            return 1
        elif player.health < 1 and opponent.health < 1:
            self.gameOver = True
            print("*** Draw ***")
            return 0
        return 0

    def displayResult(self, player, opponent):
        print(
            "%s used a %s, %s used a %s \n"
            % (
                player.name,
                weapons[player.weapon],
                opponent.name,
                weapons[opponent.weapon],
            )
        )
        print("%s caused damage to %s\n" % (player.name, opponent.name))

    def takeTurn(self, player, opponent):

        # Decision Array
        #
        #           Sword |  Arrow |  Fire
        #           ______|________|_______
        # Sword:    False |  False  |  True
        # Arrow:    True  |  True |  False
        # Fire :    False  |  True  |  True

        decisionArray = [  # Sword   Arrow   Fire
            [False, False, True],  # Sword
            [True, True, False],  # Arrow
            [False, True, True],  # Fire
        ]
        print(
            f"\n{player.name} used {weapons[player.weapon]}, {opponent.name} used {weapons[opponent.weapon]}"
        )
        if decisionArray[player.weapon][opponent.weapon]:
            opponent.damage()

        if decisionArray[opponent.weapon][player.weapon]:
            player.damage()


def run_console_combat():
    # Setup Combat Objects
    currentGame = Combat()
    human = Player("Mark")
    computer = ComputerCombatPlayer("Computer")

    players = [human, computer]

    # Main Combat Loop
    while not currentGame.gameOver:
        for player in players:
            player.selectWeapon()
        currentGame.newRound()
        currentGame.takeTurn(human, computer)
        print("%s's health = %d" % (human.name, human.health))
        print("%s's health = %d" % (computer.name, computer.health))
        currentGame.checkWin(human, computer)
