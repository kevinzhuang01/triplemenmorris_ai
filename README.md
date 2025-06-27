# Triple Men Morris (3x3 Board) CLI Version
This is my python implementation of the classic Three Men's Morris game (3x3 board) with an AI opponent using the Minimax algorithm and alpha-beta pruning for efficient decision-making.

## Requirements
- Python 3.X

## Features

- 3x3 game board  
- Human vs AI gameplay  
- Intelligent AI using Minimax with alpha-beta pruning  
- Move placement and movement phases included


## Game Rules
- Each player has 3 pieces.

- Players take turns placing their pieces on empty spots.

- Once all pieces are placed, players take turns moving them to adjacent empty spaces.

- The first to form a straight line (horizontal, vertical, or diagonal) with all 3 pieces wins.


## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/triplemenmorris_ai.git
   cd triplemenmorris_ai
   ```

2. Run the game:
    ```bash
    python3 threemanmorris.py
    ```



## Why Minimax and Alpha-Beta Pruning?
- We use the Minimax algorithm for the AI because Three Men's Morris is a zero-sum, two-player, turn-based game with perfect information — meaning:

- No randomness (like dice rolls).

- Both players have full visibility of the board.

- One player’s gain is the other’s loss.

## Minimax:
- Goal: Minimize the possible loss for a worst-case scenario.

- The AI simulates all possible moves and counter-moves to determine the most optimal path to win or draw.

- It assumes the human player will always play optimally, and picks moves that give the AI the best possible outcome.

## Alpha-Beta Pruning:
- Problem: Without pruning, Minimax checks every possible move path, which becomes slow as the game progresses.

- Solution: Alpha-beta pruning eliminates entire branches of the game tree that won't influence the final decision — reducing the number of nodes evaluated.

- This makes the AI much faster without affecting its decision quality.
