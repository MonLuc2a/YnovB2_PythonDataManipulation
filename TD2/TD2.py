import numpy as np

# EXERCICE 1 : Créer un tableau 1D
# 1. Lire l’introduction 1.1. du cours.
# 2. Créer un array contenant les nombre de 1 à 10.
# 3. Afficher le .dtype et le type de cet array.

def exo1():
    array = np.arange(1, 11)
    print(array.dtype, type(array))


# EXERCICE 2 : Accéder aux éléments d’un tableau 1D
# 1. Accéder au 5ème élément de l’array de l’exercice 1.
# 2. Accéder à son dernier élément via l’indiçage négatif.
# 3. Modifier la valeur du 2ème élément en 2023 et afficher cet array.

def exo2():
    array = np.arange(1, 11)
    print(array[4])
    print(array[-1])
    array[1] = 45
    print(array)


# EXERCICE 3 : La fonction numpy.arange()
# 1. Générer un array à la manière d’un range contenant les nombres impairs de 1 à 31.
# 2. Afficher son type.
# 3. A la différence de range, numpy.arange() accepte des arguments qui ne sont pas
# entiers : générer une liste contenant les multiples de pi jusqu’à 10*pi (sans le module
# math).

def exo3():
    array = np.arange(1, 32, 2)
    print(array)
    print(type(array))
    array = np.arange(0, 10 * np.pi, np.pi)
    print(array)


# EXERCICE 4 : La fonction numpy.linspace()
# Générer un tableau 1D allant d’une valeur de départ 3 à une valeur de fin 9 contenant 15
# valeurs également espacées les unes des autres .

def exo4():
    array = np.linspace(3, 9, 15)
    print(array)


# EXERCICE 5 : Créer un tableau 2D
# Créer un tableau 2D contenant les 10, 20, 30 sur la 1ère ligne et 40, 50, 60 sur la 2ème (une
# matrice 2x3).

def exo5():
    array = np.array([[10, 20, 30], [40, 50, 60]])
    print(array)


# EXERCICE 6 : Accéder aux éléments d’un tableau 2D
# Accéder aux éléments en position 1,2 et 2,3 de la matrice précédente.

def exo6():
    array = np.array([[10, 20, 30], [40, 50, 60]])
    print(array[0, 1])
    print(array[1, 2])

# EXERCICE 7 : Taille et forme d’un tableau
# 1. Afficher le nombre d'éléments de la matrice précédente.
# 2. Afficher la taille de la matrice précédente.
# 3. Afficher la taille de l’array : a = array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# 4. Remodeler l’array précédent en une matrice de taille 3x4

def exo7():
    array = np.array([[10, 20, 30], [40, 50, 60]])
    print(array.size)
    print(array.shape)
    a = np.arange(1, 13)
    print(a.size)
    print(a.shape)
    a = a.reshape(3, 4)
    print(a)


# EXERCICE 8 : Obtenir un tableau 2D ligne ou colonne
# Transformer le tableau 1D a = np.arange(1, 6) en un tableau “2D ligne” puis en tableau “2D
# colonne”.

def exo8():
    a = np.arange(1, 6)
    print(a)
    a = a.reshape(1, 5)
    print(a)
    a = a.reshape(5, 1)
    print(a)

# /*EXERCICE 9 : Action d’une fonction mathématique sur un tableau
# 1. Appliquer les fonctions cosinus et sinus à l’array a = np.linspace(-np.pi/2, np.pi/2, 3).
# 2. Appliquer les fonctions exponentielle, racine carré, valeur absolue, logarithme à
# l’array b = np.arange(3).
# 3. Additionner les tableaux a et b.

def exo9():
    a = np.linspace(-np.pi / 2, np.pi / 2, 3)
    print(np.cos(a))
    print(np.sin(a))
    b = np.arange(3)
    print(np.exp(b))
    print(np.sqrt(b))
    print(np.abs(b))
    print(np.log(b))
    print(a + b)

# EXERCICE 10 : Opérations de base
# On considère les arrays : a = np.array([20, 30, 40, 50]) et b = np.arange(4)
# Prédire les résultats de : a - b, b**2, a < 35, a*b.

def exo10():
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    print(a - b) # [20 29 38 47]
    print(b ** 2) # [0 1 4 9]
    print(a < 35) # [ True  True False False]
    print(a * b) #[  0  30  80 150]

# EXERCICE 11 : Tableaux et slicing des tableaux à 1D
# Soit l’array : a = np.array([12, 25, 34, 56, 87]).
# Récupérer les 2ème et 3ème éléments dans un array b.

def exo11():
    a = np.array([12, 25, 34, 56, 87])
    b = a[1:3]
    print(b)


#EXERCICE 13 : Ajouter, supprimer et trier des éléments
# Soient x = np.array([[1, 2], [3, 4]]) et y = np.array([[5, 6]]).
# Concaténer x et y pour obtenir un array 3x2.

def exo13():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6]])
    print(np.concatenate((x, y)))

# EXERCICE 14 : Accédez à plusieurs éléments selon une condition
# Soit x = np.arange(0, 1000, 100). Récupérer les valeurs comprises entre 200 et 800 incluses,
# mais sans slice et en une seule commande.

def exo14():
    x = np.arange(0, 1000, 100)
    print(x[(x >= 200) & (x <= 800)])

# EXERCICE 15 : Indexation, découpage et itération
# Générer array([[ 0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42,
# 43]]) à partir de la fonction : def f(x, y) : return 10 * x + y

def exo15(x,y):
    return 10 * x + y

print(np.fromfunction(exo15,(5,4)))


# EXERCICE 16 : Indexation avec des tableaux booléens
# Soient les arrays a = np.arange(12).reshape(3, 4), b1 = np.array([False, True, True]) et b2 =
# np.array([True, False, True, False]).
# Prédire les résultats des commandes : a[b1, :] et a[:, b2]

def exo16():
    a = np.arange(12).reshape(3, 4)
    b1 = np.array([False, True, True])
    b2 = np.array([True, False, True, False])
    print(a[b1, :])
    print(a[:, b2])