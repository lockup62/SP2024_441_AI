import pygame
from lab11.turn_combat import CombatPlayer

class PyGameHumanPlayer:
    def __init__(self, starting_money=100.0) -> None:
        self.money = starting_money

    def selectAction(self, state) -> int:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if ord("0") <= event.key <= ord("9"):
                    destination_city = int(chr(event.key))
                    # Check if there's a route between the current city and the destination city
                    if (
                        destination_city != state.current_city
                        and not state.travelling
                        and (state.cities[state.current_city][:2], state.cities[destination_city][:2]) in state.routes
                    ):
                        # Calculate travel cost based on elevation
                        elevation = state.cities[destination_city][2]  # Assuming elevation is the third element
                        if elevation > 0.9:
                            travel_cost = 10  # High elevation
                        elif elevation < 0.1:
                            travel_cost = 5  # Low elevation
                        else:
                            travel_cost = 0  # Normal elevation
                        # Deduct travel cost from player's money
                        self.money -= travel_cost
                        return event.key
        return ord(str(state.current_city))  # Not a safe operation for >10 cities

class PyGameHumanCombatPlayer(CombatPlayer):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def weapon_selecting_strategy(self) -> int:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [ord("s"), ord("a"), ord("f")]:
                        choice = {ord("s"): 1, ord("a"): 2, ord("f"): 3}[event.key]
                        self.weapon = choice - 1
                        return self.weapon

