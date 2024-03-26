''' 
Lab 12: Beginnings of Reinforcement Learning

Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
def run_episode(player1, player2):
    # Initialize combat environment
    combat = Combat()

    #Make list for storing state action reward tuples
    episodes = []

    while not combat.gameOver:
        #get current state/health of both players
        state = (player1.health, player2.health)

        #player 1 turn
        action_player1 = player1.selectAction(state)
        combat.newRound()
        combat.takeTurn(player1, player2)
        reward_player1 = combat.checkWin(player1, player2)

        #store state action reward for player 1
        episodes.append((state, action_player1, reward_player1))

        #if combats done
        if combat.gameOver:
            break

        #get state/health again
        state = (player1.health, player2.health)

        #Player 2 turn
        action_player2 = player2.selectAction(state)
        combat.newRound()
        combat.takeTurn(player2, player1)
        reward_player2 = combat.checkWin(player2, player1)

        #Store state action rewardfor player 2
        episodes.append((state, action_player2, reward_player2))

    return episodes
