import numpy as np
import tkinter as tk
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

ROWS = 6
COLUMNS = 7
PLAYER1 = 1
PLAYER2 = 2
EMPTY = 0
NUM_EPOCHS = 10


class Connect4:
    def __init__(self):
        self.connect4_ai = None
        self.connect4 = None
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
                if self.board[r][c] == player and self.board[r][c + 1] == player and self.board[r][c + 2] == player and \
                        self.board[r][c + 3] == player:
                    return True

        # Check vertical locations for win
        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if self.board[r][c] == player and self.board[r + 1][c] == player and self.board[r + 2][c] == player and \
                        self.board[r + 3][c] == player:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if self.board[r][c] == player and self.board[r + 1][c + 1] == player and self.board[r + 2][
                    c + 2] == player and self.board[r + 3][c + 3] == player:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if self.board[r][c] == player and self.board[r - 1][c + 1] == player and self.board[r - 2][
                    c + 2] == player and self.board[r - 3][c + 3] == player:
                    return True

        return False

    def is_board_full(self):
        return np.all(self.board != EMPTY)

    def switch_player(self):
        if self.current_player == PLAYER1:
            self.current_player = PLAYER2
        else:
            self.current_player = PLAYER1


class Connect4AI:
    def __init__(self):
        self.model = Sequential([
            Flatten(input_shape=(ROWS, COLUMNS)),
            Dense(32, activation='relu'),
            Dense(COLUMNS, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='categorical_crossentropy')

    def train(self, X_train, Y_train):
        self.model.fit(X_train, Y_train, epochs=NUM_EPOCHS, verbose=0)

    def predict(self, player_board):
        return self.model.predict(player_board.reshape((1, ROWS, COLUMNS)))[0]

    def get_move(self, connect4):
        if connect4.current_player == PLAYER1:
            player_board = np.copy(connect4.board)
        else:
            player_board = np.copy(connect4.board) * -1
        player_board[player_board < 0] = 2

        predictions = self.predict(player_board)
        column = np.argmax(predictions)

        while not connect4.drop_piece(column):
            predictions[column] = 0
            column = np.argmax(predictions)

        return column

class Connect4GUI:
    def __init__(self, connect4, connect4_ai):
        self.connect4 = connect4
        self.connect4_ai = connect4_ai

        self.root = tk.Tk()
        self.root.title("Puissance 4")
        self.root.geometry("420x420")
        self.canvas = tk.Canvas(self.root, width=420, height=420, bg='blue')
        self.canvas.pack()

        self.draw_board()

        self.root.bind('<Button-1>', self.click_event)

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
                    color = 'yellow'
                elif self.connect4.board[row][col] == PLAYER2:
                    color = 'red'
                self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def click_event(self, event):
        if self.connect4.game_over:
            return

        column = event.x // 60
        if not self.connect4.drop_piece(column):
            return

        if self.connect4.is_winner(self.connect4.current_player):
            self.canvas.create_text(210, 210, text="Joueur {} a gagné !".format(self.connect4.current_player),
                                    font=('Arial', 20), fill='white')
            self.connect4.game_over = True
        elif self.connect4.is_board_full():
            self.canvas.create_text(210, 210, text="Match nul !", font=('Arial', 20), fill='white')
            self.connect4.game_over = True
        else:
            self.connect4.switch_player()

            if self.connect4.current_player == PLAYER2:
                column = self.connect4_ai.get_move(self.connect4)  # Modification ici
                self.connect4.drop_piece(column)
                if self.connect4.is_winner(self.connect4.current_player):
                    self.canvas.create_text(210, 210, text="Joueur {} a gagné !".format(self.connect4.current_player),
                                            font=('Arial', 20), fill='white')
                    self.connect4.game_over = True
                elif self.connect4.is_board_full():
                    self.canvas.create_text(210, 210, text="Match nul !", font=('Arial', 20), fill='white')
                    self.connect4.game_over = True
                else:
                    self.connect4.switch_player()  # Ajoutez cette ligne pour passer au joueur suivant

        self.draw_board()

    def handle_move(self):
        if self.connect4.is_winner(self.connect4.current_player):
            self.canvas.create_text(210, 210, text="Joueur {} a gagné !".format(self.connect4.current_player),
                                    font=('Arial', 20), fill='white')
            self.connect4.game_over = True
        elif self.connect4.is_board_full():
            self.canvas.create_text(210, 210, text="Match nul !", font=('Arial', 20), fill='white')
            self.connect4.game_over = True
        else:
            self.connect4.switch_player()

            if self.connect4.current_player == PLAYER2:
                self.root.after(500, self.bot_move)

        self.draw_board()

    def bot_move(self):
        column = self.connect4_ai.get_move(self.connect4)
        self.connect4.drop_piece(column)
        self.handle_move()


def generate_training_data(num_games):
    X_train = []
    Y_train = []

    for _ in range(num_games):
        connect4 = Connect4()
        while not connect4.game_over:
            move = np.random.randint(COLUMNS)
            if connect4.drop_piece(move):
                if connect4.current_player == PLAYER1:
                    player_board = np.copy(connect4.board)
                else:
                    player_board = np.copy(connect4.board) * -1
                player_board[player_board < 0] = 2

                target = np.zeros(COLUMNS)
                target[move] = 1

                X_train.append(player_board)
                Y_train.append(target)

                if connect4.is_winner(connect4.current_player) or connect4.is_board_full():
                    connect4.game_over = True
                else:
                    connect4.switch_player()

    return np.array(X_train), np.array(Y_train)


NUM_TRAINING_GAMES = 1000
X_train, Y_train = generate_training_data(NUM_TRAINING_GAMES)
X_train_df = pd.DataFrame(X_train.reshape(X_train.shape[0], -1))
Y_train_df = pd.DataFrame(Y_train)
X_train_df.to_csv('X_train.csv', index=False)
Y_train_df.to_csv('Y_train.csv', index=False)

X_train_np = X_train_df.to_numpy().reshape(-1, ROWS, COLUMNS)
Y_train_np = Y_train_df.to_numpy()



connect4_ai = Connect4AI()
connect4_ai.train(X_train_np, Y_train_np)

connect4 = Connect4()
gui = Connect4GUI(connect4, connect4_ai)


