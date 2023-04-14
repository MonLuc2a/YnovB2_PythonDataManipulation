import numpy as np
import random
import matplotlib.pyplot as plt


# EXERCICE 1 : Les fonctions de base
# 1. Définir deux listes de 4 entiers (une pour les abscisses et une pour les ordonnées) et
# tracer la courbe reliant les 4 points.
# 2. Tracer la fonction cosinus entre 0 et 4pi avec 100 points (on peut utiliser la fonction
# linspace de numpy).

def exo1():
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    plt.plot(x, y)
    plt.show()

    x = np.linspace(0, 4 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.show()

# EXERCICE 2 : Tracé de plusieurs fonctions
# 1. En reprenant le 2. de l’exercice précédent, ajouter la fonction sinus dans le même
# repère.
# 2. Ajouter une légende pour visualiser quelle courbe correspond à quelle fonction.

def exo2():
    x = np.linspace(0, 4 * np.pi, 100)
    y1 = np.cos(x)
    y2 = np.sin(x)
    plt.plot(x, y1, label="cosinus")
    plt.plot(x, y2, label="sinus")
    plt.legend()
    plt.show()


# EXERCICE 3 : Les diagrammes en bâtons
# A l’aide des listes x = [3, 5, 6, 7] et y = [4, 1, 3, 4], tracer un diagramme en bâtons et
# commenter le résultat.

def exo3():
    x = [3, 5, 6, 7]
    y = [4, 1, 3, 4]
    plt.bar(x, y)
    plt.show()

# EXERCICE 4 : Les histogrammes
# On considère une expérience aléatoire consistant à tirer deux dés et de faire la somme des
# faces supérieures.
# Simuler 1000 fois cette expérience aléatoire et affichez les résultats dans un histogramme

def exo4():
    x = []
    for i in range(1000):
        x.append(random.randint(1, 6) + random.randint(1, 6))
    plt.hist(x,11)
    plt.show()
    for i in range(11):
        print(i+2, ":", x.count(i+2))

# EXERCICE 5 : Les nuages de points
# 1. Générer deux listes random (abs et ord) pour modéliser 5000 points.
# 2. Afficher dans un graphique “nuage de points” entre -3 et 3.
# 3. Définir une fonction permettant de modifier la couleur des points s’ils sont au-dessus
# ou en dessous de la courbe y = x².

def exo5():
    x = []
    y = []
    for i in range(5000):
        x.append(random.uniform(-3, 3))
        y.append(random.uniform(-3, 3))
    plt.scatter(x, y)

    for i in range(5000):
        if y[i] > x[i] ** 2:
            plt.scatter(x[i], y[i], color="red")
        else:
            plt.scatter(x[i], y[i], color="blue")
    plt.show()

# EXERCICE 6 : Paramétriser des courbes
# 1. Tracer la courbe y = 2x² + 3x -4 à l’aide de 10 points dans un repère.
# 2. Paramétriser la courbe pour qu’elle s’affiche en magenta, avec des hexagone à la
# place des markers, ainsi qu’une alternance point/tiret entre les markers.
# 3. Changer la couleur et la taille des markers.
# 4. Augmenter la taille des pointillés.

def exo6():
    x = np.linspace(-5, 5, 10)
    y = 2 * x ** 2 + 3 * x - 4
    plt.plot(x, y, color="magenta", marker="h", linestyle=":", markerfacecolor="blue", markersize=10, markevery=2)
    plt.show()

exo6()