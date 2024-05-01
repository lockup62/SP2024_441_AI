ABSTRACT:
I explored the advanced AI functionalities integrated into my turn-based battle game, developed using Python and Pygame. My aim was to enhance player engagement by incorporating intelligent decision-making, strategic combat tactics, and dynamic dialogue interactions within the game environment. Much of the skeleton code was already provided.
At the forefront is the PyGameAIPlayer component, designed to let players have decision-making capabilities. By analyzing the current game state and opponent actions, this AI entity computes optimal player actions and changes based on what the player chooses for their combat.
Also included is the PyGameAICombatPlayer and PyGameComputerCombatPlayer. These components excel in orchestrating tactical combat encounters. These entities analyze factors such as health, opponent actions, and available weaponry to make combat strategies, which makes the gameplay experience more engaging.
Additionally, my integration of Ollama, an advanced Natural Language Processing (NLP) model, introduces immersive dialogue interactions within the game. Ollama processes input prompts, such as dialogue queries and contextual cues, to generate coherent and contextually relevant responses. This feature allows player immersion, showing lifelike interactions with AI characters and enhancing the narrative depth of the gaming experience. I made it so the AI’s response upon entering a fight is a response to the prompt, "say something as if you just approached me in battle.” This aims to give each AI you battle a unique dialogue. 
In summary, the combination of these AI components offers players an fun and engaging gaming experience. By leveraging AI techniques such as heuristic algorithms and natural language processing, my turn-based battle game promises an immersive journey where strategic choices and dynamic interactions shape the outcome of each encounter.





 
List of AI components in the project
1.	PyGameAIPlayer
2.	PyGameAICombatPlayer
3.	ComputerCombatPlayer
4. 	Ollama

Report on AI Components in the Game
Introduction: Artificial Intelligence (AI) plays a pivotal role in shaping modern video games, providing them with dynamic interactions, challenging gameplay, and immersive experiences. In this report, I delve into the AI components integrated into a turn-based battle game developed using Python and Pygame. Each AI component serves a distinct purpose, solving specific problems related to decision-making, combat strategies, and natural language processing. By analyzing the functionalities and implementations of these AI components, we gain insights into their contributions to enhancing the overall gaming experience.

1.	PyGameAIPlayer: 
The PyGameAIPlayer component is designed to provide AI behavior for the player character in the game. Its main function is to enable the player to make decisions based on the current game state and environment. Through sophisticated algorithms and decision-making processes, PyGameAIPlayer analyzes various factors such as map layout, opponent positions, and available resources to determine the optimal course of action. It considers if a player just moved to a city, it considers their weapon choices, and it considers their money and health. This component empowers the player with intelligent behavior, enhancing their immersion in the game world and facilitating dynamic interactions with the environment and non-player characters (NPCs).
2.	PyGameAICombatPlayer: 
In combat scenarios, the PyGameAICombatPlayer component takes center stage, offering AI-driven decision-making to enhance strategic depth and challenge. This component also uses tactical algorithms to select combat actions based on factors such as player health, opponent moves, and available weapons. By leveraging heuristic approaches and decision trees, PyGameAICombatPlayer aims to maximize the player's chances of success in combat encounters. It adapts its strategies dynamically to the evolving combat situation, providing engaging and challenging gameplay experiences.

4.	PyGameComputerCombatPlayer:
 Similar to PyGameAICombatPlayer, the PyGameComputerCombatPlayer component contributes AI behavior for combat scenarios, even though it has potential variations in strategy. This component may employ predefined rules or heuristics to determine combat actions, prioritizing certain tactics based on situational factors such as terrain conditions, opponent behavior, and available resources. PyGameComputerCombatPlayer adds diversity and unpredictability to combat encounters, ensuring that each battle presents unique challenges and opportunities for the player to overcome.

6.	Ollama for Natural Language Processing: 
Ollama, an advanced NLP model, enriches the game with dialogue interactions and narrative depth. This component processes textual prompts and generates coherent, contextually relevant responses, simulating realistic dialogue interactions between players and NPCs. By analyzing semantic and contextual cues, Ollama produces dynamic and engaging dialogue sequences, enhancing the storytelling and immersion within the game world. It enables players to engage in meaningful battle, make impactful decisions, and shape the outcome of the game through their interactions with AI characters. This is done by using the ollama library. After initializing the Ollama, I prompted it with the message, “say something as if you just approached me in battle.” The generative response is then printed to the screen allowing the player to see a unique dialogue for each of the enemies they encounter on their journey. This is intended to make the game more immersive and give the game a little more realism. 

7.	Extra:
We also used genetic algorithms in class to generate a realistic looking map with realistically spread cities and routes. This serves as the game environment allowing the player to play the game with a map procedurally generated with a genetic algorithm.
Conclusion: 
The integration of AI components in the turn-based battle game elevates its gameplay experience to new heights, offering players dynamic interactions, strategic challenges, and immersive storytelling. Using intelligent algorithms, heuristic approaches, and advanced computational techniques, these AI components enhance everything about the gaming experience, from decision-making and combat strategies to dialogue interactions and narrative depth. Without AI, this game would not be possible, and enemies would not function as they do now. 

APPENDIX:

![Chat1](https://github.com/lockup62/SP2024_441_AI/assets/36246100/5777451a-7e48-42e1-9d27-ee02aab338d8)

![CHAT2](https://github.com/lockup62/SP2024_441_AI/assets/36246100/c8d9786b-a180-4c29-82a3-88b73dc6efb0)

![Chat3](https://github.com/lockup62/SP2024_441_AI/assets/36246100/475ffbb8-7e3f-48bc-a01b-2fdc966e768c)

