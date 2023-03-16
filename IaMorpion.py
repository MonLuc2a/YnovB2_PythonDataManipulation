import random

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(ligne))

def jouer(grille, joueur, x, y):
    if grille[x][y] == "-":
        grille[x][y] = joueur
        return True
    return False

def gagnant(grille):
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "-":
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] != "-":
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] != "-":
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] != "-":
        return True
    return False

def ia_jouer(grille, joueur):
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if jouer(grille, joueur, x, y):
            break

def morpion():
    grille = [["-" for _ in range(3)] for _ in range(3)]
    joueur = "X"
    nb_coups = 0

    while nb_coups < 9 and not gagnant(grille):
        afficher_grille(grille)
        if joueur == "X":
            x, y = map(int, input("Entrez les coordonnées (x y) séparées par un espace: \n").split())
            if jouer(grille, joueur, x, y):
                joueur = "O"
                nb_coups += 1
        else:
            ia_jouer(grille, joueur)
            joueur = "X"
            nb_coups += 1

    afficher_grille(grille)
    if gagnant(grille):
        print(f"Le joueur {joueur} a gagné!")
    else:
        print("Match nul!")

if __name__ == "__main__":
    morpion()
