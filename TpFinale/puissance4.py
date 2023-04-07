# L'objectif est de créer un jeu de Puissance 4 avec une IA qui joue contre l'utilisateur.
# L'IA cherche la meilleure solution possible en se basant sur les parties précédentes stockées dans une base de données.
# Chaque solution est associée à un score pour choisir le meilleur coup suivant en utilisant la bibliothèque pandas.

import os
import pickle
import numpy as np
import tkinter as tk
import pandas as pd

ROWS = 6
COLUMNS = 7
PLAYER1 = 1
PLAYER2 = 2
EMPTY = 0


class Connect4:
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS), dtype=int)
        self.current_player = PLAYER1
        self.game_over = False
        self.moves = []
        self.winner = None

    def drop_piece(self, column):
        row = ROWS - 1
        while row >= 0:
            if self.board[row][column] == EMPTY:
                self.board[row][column] = self.current_player
                self.moves.append((self.current_player, row, column))
                return True
            row -= 1
        return False

    def is_winner(self, player):
        # Check horizontal locations for win
        for c in range(COLUMNS - 3):
            for r in range(ROWS):
                if self.board[r][c] == player and self.board[r][c + 1] == player and self.board[r][c + 2] == player and self.board[r][c + 3] == player:
                    return True

        # Check vertical locations for win
        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if self.board[r][c] == player and self.board[r + 1][c] == player and self.board[r + 2][c] == player and self.board[r + 3][c] == player:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if self.board[r][c] == player and self.board[r + 1][c + 1] == player and self.board[r + 2][c + 2] == player and self.board[r + 3][c + 3] == player:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if self.board[r][c] == player and self.board[r - 1][c + 1] == player and self.board[r - 2][c + 2] == player and self.board[r - 3][c + 3] == player:
                    return True

        return False

    def is_board_full(self):
        return np.all(self.board != EMPTY)

    def switch_player(self):
        if self.current_player == PLAYER1:
            self.current_player = PLAYER2
        else:
            self.current_player = PLAYER1




class Connect4GUI:
    def __init__(self, connect4):
        self.connect4 = connect4

        self.root = tk.Tk()
        self.root.title("Puissance 4")
        self.root.geometry("420x420")
        self.canvas = tk.Canvas(self.root, width=420, height=420, bg='blue')
        self.canvas.pack()

        self.draw_board()

        self.root.bind('<Button-1>', self.click_event)

        self.restart_button = tk.Button(text="Restart", command=self.restart)
        self.restart_button.pack()

        self.root.mainloop()


    def draw_board(self):
        self.canvas.delete('all')

        for row in range(ROWS):
            for col in range(COLUMNS):
                x1 = col * 60
                y1 = row * 60
                x2 = x1 + 60
                y2 = y1 + 60
                color = 'white'
                if self.connect4.board[row][col] == PLAYER1:
                    color = 'red'
                elif self.connect4.board[row][col] == PLAYER2:
                    color = 'yellow'
                self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def restart(self):
        self.connect4.__init__()
        self.draw_board()

    def click_event(self, event):
        if self.connect4.game_over:
            return

        x = event.x
        column = x // 60

        if self.connect4.drop_piece(column):
            self.draw_board()
            if self.connect4.is_winner(PLAYER1):
                self.connect4.game_over = True
                self.connect4.winner = PLAYER1
                self.canvas.create_text(210, 210, text="Player {} wins!".format(self.connect4.winner),
                                        font=("Helvetica", 32))
                self.connect4.append_and_save_game_data()
            elif self.connect4.is_board_full():
                self.connect4.game_over = True
                self.canvas.create_text(210, 210, text="Draw!", font=("Helvetica", 32))
                self.connect4.append_and_save_game_data()
            else:
                self.connect4.switch_player()
                self.connect4.ai_move()
                self.draw_board()
                if self.connect4.is_winner(PLAYER2):
                    self.connect4.game_over = True
                    self.connect4.winner = PLAYER2
                    self.canvas.create_text(210, 210, text="AI wins!", font=("Helvetica", 32))
                    self.connect4.append_and_save_game_data()
                elif self.connect4.is_board_full():
                    self.connect4.game_over = True
                    self.canvas.create_text(210, 210, text="Draw!", font=("Helvetica", 32))
                    self.connect4.append_and_save_game_data()
                else:
                    self.connect4.switch_player()


class Connect4AI(Connect4):
    def __init__(self):
        super().__init__()
        self.db_file = 'game_data.csv'
        if os.path.exists(self.db_file):
            self.game_data = pd.read_csv(self.db_file)
        else:
            self.game_data = pd.DataFrame(columns=['moves', 'winner'])

    def save_game_data(self):
        self.game_data.to_csv(self.db_file, index=False)

    def get_score(self, moves):
        score = 0
        moves_str = '-'.join([f"{move[0]}{move[1]}{move[2]}" for move in moves])
        for _, game in self.game_data.iterrows():
            if game['winner'] == PLAYER2:
                score_increment = 1
            else:
                score_increment = -1

            if moves_str in game['moves']:
                score += score_increment

        return score

    def choose_best_move(self):
        possible_moves = self.get_possible_moves()
        best_score = -np.inf
        best_move = None

        for move in possible_moves:
            moves_copy = self.moves.copy()
            row = ROWS - 1
            while row >= 0:
                if self.board[row][move] == EMPTY:
                    moves_copy.append((self.current_player, row, move))
                    break
                row -= 1

            score = self.get_score(moves_copy)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def ai_move(self):
        if self.game_over:
            return

        best_move = self.choose_best_move()
        if best_move is not None and self.drop_piece(best_move):
            if self.is_winner(PLAYER2):
                self.game_over = True
                self.winner = PLAYER2
                print("AI wins!")
                self.append_and_save_game_data()
            elif self.is_board_full():
                self.game_over = True
                print("Draw!")
                self.append_and_save_game_data()
            else:
                self.switch_player()

    def get_valid_moves(self):
        valid_moves = []
        for c in range(COLUMNS):
            if self.board[0][c] == EMPTY:
                valid_moves.append(c)
        return valid_moves

    def append_and_save_game_data(self):
        moves_str = '-'.join([f"{move[0]}{move[1]}{move[2]}" for move in self.moves])
        new_row = pd.DataFrame({'moves': [moves_str], 'winner': [self.winner]})
        self.game_data = pd.concat([self.game_data, new_row], ignore_index=True)
        self.save_game_data()

    def get_best_move_from_data(self, game_data):
        valid_moves = self.get_valid_moves()
        move_scores = {}

        for move in valid_moves:
            move_data = game_data[game_data['moves'].str.startswith(str(move))]
            move_wins = move_data[move_data['winner'] == PLAYER1].shape[0]
            move_losses = move_data[move_data['winner'] == PLAYER2].shape[0]

            if move_wins + move_losses == 0:
                move_scores[move] = 0.5
            else:
                move_scores[move] = move_wins / (move_wins + move_losses)

        best_move = max(move_scores, key=move_scores.get)
        return best_move

    def make_ai_move(self, game_data=None):
        if game_data is None:
            game_data = self.game_data

        valid_moves = self.get_valid_moves()
        move_scores = {}

        for move in valid_moves:
            move_data = self.get_move_data(move, game_data)
            move_wins = move_data[move_data['winner'] == self.player1_id].shape[0]
            move_losses = move_data[move_data['winner'] == self.player2_id].shape[0]
            move_scores[move] = move_wins - move_losses

        # Ajoutez cette vérification ici
        if not move_scores:
            self.game_over = True
            return None

        best_move = max(move_scores, key=move_scores.get)
        return best_move


class Connect4AIAutoPlay(Connect4AI):
    def autoplay(self, num_games=1, game_data=None):
        for _ in range(num_games):
            self.reset()
            moves = []
            while not self.game_over:
                move = self.make_ai_move(game_data)
                moves.append(move)
                self.drop_piece(move)
            moves_str = ' '.join(str(m) for m in moves)
            new_row = pd.DataFrame({'moves': [moves_str], 'winner': [self.winner]})
            self.game_data = pd.concat([self.game_data, new_row], ignore_index=True)

    def reset(self):
        self.__init__()
        self.game_over = False
        self.winner = None
        self.moves = []

    def get_move_data(self, move, game_data):
        move_data = game_data[game_data['move'] == move]
        return move_data




game_data = pd.read_csv('game_data.csv')


if __name__ == '__main__':
    game_data = pd.read_csv('game_data.csv')
    connect4_train = Connect4AIAutoPlay()
    connect4_train.autoplay(num_games=10, game_data=game_data)
    connect4_train.save_game_data()


