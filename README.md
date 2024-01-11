# TicTacToeAI
## Overview
This Tic-Tac-Toe AI algorithm is an implementation of the minimax algorithm including alpha-beta pruning designed as part of the CS50 course. This project was my first attempt at developing AI algorithms. This showcases my ability to create basic intelligent systems using Python.
The GUI of the Tic-Tac-Toe game (runner.py) was written solely by the CS50 staff, and only the algorithm and implementation of functions (tictactoe.py) were done by me. 


## AI algorithm explanation
The AI algorithm uses minimax. This would mean that the algorithm computes all possible outcomes from taking a specific action and chooses the outcome which best provides the utility it is aiming towards. This maximises its chances of winning while minimising the player's. 
It does this by examining every possible step in the future, considering the optimised move that a player might take when it chooses an action. This process occurs recursively until there are no moves left to predict. To put it simply, it can be imagined that it asks itself "If I take this action, what would the player take if he/she is playing optimally?", the option to choose which action is deduced by choosing the best possible outcome after all these predictions have been calculated for every possible action.

One might consider that if a program has to fully consider every potential outcome for every possible action to make a decision, it might require an unnecessarily large amount of computational energy making this algorithm inefficient. Hence, introducing the concept of alpha-beta pruning reduces the frequency with which the program computes every possible outcome. A simple way to understand alpha-beta pruning is that we know a value can be disregarded if we know it would not be chosen by a player. 
For example, if the algorithm is aimed to minimise the value while the player maximises, whenever it takes an action it has to consider the maximised value which the player would take. When it is deciding to take an action, it can disregard the potential outcomes of the player which it knows the player would not take (values smaller than the predicted action the player would take), or the potential outcomes that are greater than the outcome of the action that the AI already calculated. 
This means that in the case of a minimising algorithm, the AI would disregard anything that isn't smaller than a value it has initially calculated. Hence, unless it provides a better utility, it would not be calculated.

## Challenges and learning
Due to Python being a relatively newer language to me, there were gaps in my knowledge regarding the kind of syntax that I could use. This presented a problem while I was implementing the minimax algorithm. Additionally, this program was relatively hard to understand at first, this could have been because I had no prior experience with designing algorithms. Hence, I had to do extra bits of research by watching YouTube videos explaining and visualising the minimax algorithm and alpha-beta pruning.


