import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class NimGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Nim")

        self.lines = [random.randint(1, 10) for _ in range(3)]

        self.turn = "player"

        self.line_buttons = []
        for i, line in enumerate(self.lines):
            line_button = tk.Button(self.root, text=f"Ligne {i+1}: {line} allumettes", command=lambda i=i: self.take_matchsticks(i))
            line_button.grid(row=i, column=0, padx=10, pady=10)
            self.line_buttons.append(line_button)

        self.info_label = tk.Label(self.root, text="C'est votre tour. Choisissez une ligne.")
        self.info_label.grid(row=3, column=0, padx=10, pady=10)

    def take_matchsticks(self, line):
        if self.turn == "player":
            matches = simpledialog.askinteger("Allumettes", f"Combien d'allumettes voulez-vous prendre dans la ligne {line+1}?", minvalue=1, maxvalue=3)
            if matches is not None:
                self.lines[line] -= matches
                self.line_buttons[line].config(text=f"Ligne {line+1}: {self.lines[line]} allumettes")
                self.check_game_state()

    def bot_turn(self):
        # Votre logique d'intelligence artificielle pour le bot ici

        line, matches = self.bot_strategy()
        self.lines[line] -= matches
        self.line_buttons[line].config(text=f"Ligne {line+1}: {self.lines[line]} allumettes")
        self.check_game_state()

    def check_game_state(self):
        if sum(self.lines) == 0:
            winner = "Bot" if self.turn == "player" else "Joueur"
            messagebox.showinfo("Fin de la partie", f"{winner} a gagné!")
            self.root.quit()
        else:
            self.turn = "bot" if self.turn == "player" else "player"
            self.info_label.config(text=f"C'est au tour du {self.turn}.")

            if self.turn == "bot":
                self.bot_turn()

    def bot_strategy(self):
        # Implémentez la stratégie du bot ici
        # Pour l'instant, le bot choisit simplement une ligne et prend un nombre aléatoire d'allumettes.
        line = random.choice([i for i, count in enumerate(self.lines) if count > 0])
        matches = random.randint(1, self.lines[line])
        return line, matches

if __name__ == "__main__":
    root = tk.Tk()
    game = NimGame(root)
    root.mainloop()
