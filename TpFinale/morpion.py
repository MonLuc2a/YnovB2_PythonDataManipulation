import tkinter as tk
from tkinter import messagebox, Button
import random


class Morpion:
    def __init__(self):
        self.joueur_actuel = "X"
        self.grille = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def jouer(self, ligne, colonne):
        if self.grille[ligne][colonne] == " ":
            self.grille[ligne][colonne] = self.joueur_actuel
            if self.joueur_actuel == "X":
                self.joueur_actuel = "O"
            else:
                self.joueur_actuel = "X"
        else:
            messagebox.showwarning("Erreur", "Case déjà occupée")

    def est_gagne(self):
        # Vérification des lignes
        for ligne in range(3):
            if self.grille[ligne][0] == self.grille[ligne][1] == self.grille[ligne][2] != " ":
                return True

        # Vérification des colonnes
        for colonne in range(3):
            if self.grille[0][colonne] == self.grille[1][colonne] == self.grille[2][colonne] != " ":
                return True

        # Vérification des diagonales
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != " ":
            return True
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != " ":
            return True

        return False

    def est_plein(self):
        for ligne in range(3):
            for colonne in range(3):
                if self.grille[ligne][colonne] == " ":
                    return False
        return True

    def gagnant(self):
        if self.est_gagne():
            if self.joueur_actuel == "X":
                return "O"
            else:
                return "X"
        return None

    def match_nul(self):
        return self.est_plein() and not self.est_gagne()

    def est_case_vide(self, ligne, colonne):
        return self.grille[ligne][colonne] == " "

    def jouer_coup(self, ligne, colonne, joueur):
        self.grille[ligne][colonne] = joueur

    def annuler_coup(self, ligne, colonne):
        self.grille[ligne][colonne] = " "

    def reinitialiser(self):
        self.joueur_actuel = "X"
        self.grille = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


class Player:
    def __init__(self, symbole, morpion, master):
        self.symbole = symbole
        self.morpion = morpion
        self.master = master
        self.cases = []

    def minimax(self, profondeur, joueur):
        """
        Fonction récursive qui implémente l'algorithme minimax pour déterminer le meilleur coup possible
        """
        if self.morpion.gagnant() == "O":
            return 10
        elif self.morpion.gagnant() == "X":
            return -10
        elif self.morpion.match_nul():
            return 0

        if joueur == "O":
            meilleur_score = -1000
            for i in range(3):
                for j in range(3):
                    if self.morpion.est_case_vide(i, j):
                        self.morpion.jouer_coup(i, j, joueur)
                        score = self.minimax(profondeur + 1, "X")
                        self.morpion.annuler_coup(i, j)
                        meilleur_score = max(meilleur_score, score)
            return meilleur_score
        else:
            meilleur_score = 1000
            for i in range(3):
                for j in range(3):
                    if self.morpion.est_case_vide(i, j):
                        self.morpion.jouer_coup(i, j, joueur)
                        score = self.minimax(profondeur + 1, "O")
                        self.morpion.annuler_coup(i, j)
                        meilleur_score = min(meilleur_score, score)
            return meilleur_score

    def jouer_coup(self):
        meilleur_score = -1000
        meilleur_coup = None
        for ligne in range(3):
            for colonne in range(3):
                if self.morpion.grille[ligne][colonne] == " ":
                    self.morpion.grille[ligne][colonne] = self.symbole
                    score = self.minimax(0, "X")
                    self.morpion.grille[ligne][colonne] = " "
                    if score > meilleur_score:
                        meilleur_score = score
                        meilleur_coup = (ligne, colonne)
        if meilleur_coup:
            self.morpion.jouer(meilleur_coup[0], meilleur_coup[1])
            for ligne in range(3):
                for colonne in range(3):
                    if self.morpion.grille[ligne][colonne] == self.symbole:
                        self.master.cases[ligne][colonne].configure(text=self.symbole)
            if self.morpion.est_gagne():
                messagebox.showinfo("Fin de partie", "Le joueur {} a gagné ! Clique sur replay pour rejouer".format(
                    self.morpion.gagnant()))
            elif self.morpion.est_plein():
                messagebox.showinfo("Fin de partie", "Match nul !")
            elif self.morpion.joueur_actuel == "O":
                self.jouer_coup()

        self.morpion.joueur_actuel = "X"


class Application:
    def __init__(self, master):
        self.morpion = Morpion()
        self.ia = Player("O", self.morpion, self)  # passer le paramètre self
        self.joueur = Player("X", self.morpion, self)  # passer le paramètre self
        self.master = master
        self.master.title("Morpion")
        self.cases = []
        for i in range(3):
            ligne = []
            for j in range(3):
                case = Button(self.master, width=10, height=5, font=("Helvetica", 20), command=lambda i=i, j=j: self.cliquer(i, j))
                case.grid(row=i, column=j)
                ligne.append(case)
            self.cases.append(ligne)
        self.replay_button = Button(self.master, text="Rejouer", command=self.rejouer)
        self.replay_button.grid(row=3, column=1)

    def cliquer(self, ligne, colonne):
        if self.morpion.est_case_vide(ligne, colonne):
            self.morpion.jouer(ligne, colonne)
            self.cases[ligne][colonne].configure(
                text=self.joueur.symbole)  # Utilisez self.joueur.symbole au lieu de self.morpion.joueur_actuel
            if self.morpion.est_gagne():
                messagebox.showinfo("Fin de partie", "Le joueur {} a gagné ! Clique sur replay pour rejouer".format(
                    self.morpion.gagnant()))
            elif self.morpion.est_plein():
                messagebox.showinfo("Fin de partie", "Match nul !")
            elif self.morpion.joueur_actuel == "O":
                self.ia.jouer_coup()  # utiliser l'attribut master pour accéder à self.cases
            else:
                return

    def rejouer(self):
        self.morpion.reinitialiser()
        for ligne in range(3):
            for colonne in range(3):
                self.cases[ligne][colonne].configure(text=" ")


if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Jeu de morpion")
    fenetre.geometry("900x600")
    jeu = Application(fenetre)
    fenetre.mainloop()
