import math
import random

EMPTY = '.'
PLAYER = 'X'
AI = 'O'

WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

ADJACENT_POSITIONS = {
    0: [1, 3, 4], 1: [0, 2, 4], 2: [1, 4, 5],
    3: [0, 4, 6], 4: [0, 1, 2, 3, 5, 6, 7, 8],
    5: [2, 4, 8], 6: [3, 4, 7], 7: [4, 6, 8], 8: [4, 5, 7]
}


class Game:
    def __init__(self):
        self.board = [EMPTY] * 9
        self.player_pieces = 0
        self.ai_pieces = 0
        self.phase = 'placing'

    def print_board(self):
        for i in range(0, 9, 3):
            print(' '.join(self.board[i:i + 3]))
        print()

    def is_winner(self, symbol):
        return any(all(self.board[i] == symbol for i in line) for line in WINNING_LINES)

    def get_available_positions(self):
        return [i for i in range(9) if self.board[i] == EMPTY]

    def get_player_positions(self, symbol):
        return [i for i in range(9) if self.board[i] == symbol]

    def get_possible_moves(self, symbol):
        if self.phase == 'placing':
            return self.get_available_positions()
        moves = []
        for i in self.get_player_positions(symbol):
            for j in ADJACENT_POSITIONS[i]:
                if self.board[j] == EMPTY:
                    moves.append((i, j))  # from i to j
        return moves

    def make_move(self, move, symbol):
        if self.phase == 'moving' and isinstance(move, tuple):
            frm, to = move
            self.board[frm] = EMPTY
            self.board[to] = symbol
        else:
            self.board[move] = symbol
            if symbol == PLAYER:
                self.player_pieces += 1
            else:
                self.ai_pieces += 1
            if self.player_pieces == 3 and self.ai_pieces == 3:
                self.phase = 'moving'

    def undo_move(self, move, symbol):
        if self.phase == 'moving' and isinstance(move, tuple):
            # Movement undo
            frm, to = move
            self.board[to] = EMPTY
            self.board[frm] = symbol
        else:
            # Placement undo
            self.board[move] = EMPTY
            if symbol == PLAYER:
                self.player_pieces -= 1
            else:
                self.ai_pieces -= 1
            if self.player_pieces < 3 or self.ai_pieces < 3:
                self.phase = 'placing'


    def is_draw(self):
        return not self.is_winner(PLAYER) and not self.is_winner(AI) and not self.get_possible_moves(PLAYER) and not self.get_possible_moves(AI)

    def minimax(self, depth, alpha, beta, maximizing):
        if depth > 6:
            return 0, None
        if self.is_winner(AI):
            return 10 - depth, None
        if self.is_winner(PLAYER):
            return depth - 10, None
        if self.is_draw():
            return 0, None

        symbol = AI if maximizing else PLAYER
        moves = self.get_possible_moves(symbol)

        if not moves:
            return 0, None

        best_move = None

        if maximizing:
            max_eval = -math.inf
            for move in moves:
                self.make_move(move, symbol)
                score, _ = self.minimax(depth + 1, alpha, beta, False)
                self.undo_move(move, symbol)
                if score > max_eval:
                    max_eval = score
                    best_move = move
                    if max_eval == 10 - depth:
                        return max_eval, best_move  # early cutoff: winning move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in moves:
                self.make_move(move, symbol)
                score, _ = self.minimax(depth + 1, alpha, beta, True)
                self.undo_move(move, symbol)
                if score < min_eval:
                    min_eval = score
                    best_move = move
                    if min_eval == depth - 10:
                        return min_eval, best_move  # early cutoff: losing move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def player_turn(self):
        self.print_board()
        if self.phase == 'placing':
            while True:
                try:
                    move = int(input("Enter position to place (0-8): "))
                    if 0 <= move <= 8 and self.board[move] == EMPTY:
                        self.make_move(move, PLAYER)
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            while True:
                try:
                    frm = int(input("Move from: "))
                    to = int(input("Move to: "))
                    if (0 <= frm <= 8 and 0 <= to <= 8 and
                        self.board[frm] == PLAYER and
                        self.board[to] == EMPTY and
                        to in ADJACENT_POSITIONS[frm]):
                        self.make_move((frm, to), PLAYER)
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter valid numbers.")

    def ai_turn(self):
        _, move = self.minimax(0, -math.inf, math.inf, True)
        self.make_move(move, AI)

    def play(self):
        while True:
            self.player_turn()
            if self.is_winner(PLAYER):
                self.print_board()
                print("Player wins!")
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw.")
                break

            self.ai_turn()
            if self.is_winner(AI):
                self.print_board()
                print("AI wins!")
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw.")
                break

if __name__ == "__main__":
    game = Game()
    game.play()
