# coder un programme qui permet de jouer au jeu de Nim
# Les règles sont les suivantes : p lignes d’allumettes (ou de pions) sont disposées devant les joueurs et comportent respectivement N1 allumettes, N2 allumettes, …, Np allumettes.
# Les joueurs jouent à tour de rôle et chacun des deux joueurs prend autant d’allumettes qu’il veut dans une ligne (mais au moins une). Celui qui prend la dernière allumette a gagné.
#

import numpy as np
import random
import tkinter

def main():
    nbLignes = 3
    nbAllumettesParLigne = np.array([random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)])
    nbAllumettesRestantes = nbAllumettesParLigne.sum()
    joueur = 1
    canvas = screen()
    while nbAllumettesRestantes > 0:
        print("Joueur", joueur, "à toi de jouer !")
        ligne = int(input("Quelle ligne ? "))
        nbAllumettes = int(input("Combien d'allumettes ? "))
        nbAllumettesParLigne[ligne - 1] -= nbAllumettes
        nbAllumettesRestantes -= nbAllumettes
        print("Il reste", nbAllumettesRestantes, "allumettes.")
        joueur = 2 if joueur == 1 else 1
        draw(canvas, nbAllumettesParLigne)
    print("Joueur", joueur, "a gagné !")

def screen():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width = 400, height = 400)
    canvas.pack()
    return canvas

def draw(canvas, nbAllumettesParLigne):
    canvas.delete("all")
    for i in range(3):
        for j in range(nbAllumettesParLigne[i]):
            canvas.create_rectangle(10 + 100 * i, 10 + 20 * j, 90 + 100 * i, 30 + 20 * j, fill = "red")
    canvas.update()

main()



