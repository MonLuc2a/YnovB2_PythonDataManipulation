# EXERCICE 1 : Remodeler un tableau
# Soit a = np.floor(10 * np.random.randn(3, 4)).
# 1. Afficher sa “forme”.
# 2. Remodeler ce tableau en forme 6x2.
import numpy as np

def exo1():
    a = np.floor(10 * np.random.randn(3, 4))
    print(a.shape)
    a = a.reshape(6, 2)
    print(a)


# EXERCICE 2 : Aplatir les tableaux multidimensionnels
# Soit x = np.array([[1 , 2, 3, 4, 5], [5, 6, 7, 8, 9], [9, 10, 11, 12, 13]]).
# Aplatir cet array.

def exo2():
    x = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [9, 10, 11, 12, 13]])
    print(x)
    print(x.flatten())


# EXERCICE 3 : Remodelage "automatique"
# Soit a = np.arange(40).
# Utiliser le remodelage automatique pour obtenir un tableau à 3 dimensions.

def exo3():
    a = np.arange(40)
    print(a)
    a = a.reshape(5, -1, 2)
    print(a)


# EXERCICE 4 : Empiler différents tableaux
# Soient a = np.floor(10 * np.random.randn(2, 2)) et b = np.floor(10 * np.random.randn(2, 2)).
# Empiler verticalement ces deux arrays, puis horizontalement.

def exo4():
    a = np.floor(10 * np.random.randn(2, 2))
    b = np.floor(10 * np.random.randn(2, 2))
    print(a)
    print(b)
    print(np.vstack((a, b)))
    print(np.hstack((a, b)))

# EXERCICE 5 : Diviser un tableau en plusieurs plus petits
# Soit a = np.floor(10 * np.random.randn(3, 15)).
# 1. Diviser cet array en 3 arrays de même dimensions sur son axe horizontal.
# 2. Diviser cet array en 3 arrays après la 3ème et la 4ème colonne.

def exo5():
    a = np.floor(10 * np.random.randn(3, 15))
    print(a)
    print(np.hsplit(a, 3))
    print(np.hsplit(a, [3, 4]))

# EXERCICE 6 : Convertir un tableau 1D en un tableau 2D
# Soit a = np.array([1, 2, 3, 4, 5, 6]).
# Ajouter une dimension à ce tableau et comparer les “formes” avant et après.

def exo6():
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a.shape)
    a = a[:, np.newaxis]
    print(a.shape)

# EXERCICE 7 : Obtenir des objets uniques et compte
# Soit a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20]).
# Générer une liste contenant les valeurs uniques et une liste contenant les indices
# correspondant, en une seule commande.

def exo7():
    a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
    print(np.unique(a, return_index=True))


# EXERCICE 8 : Inverser un tableau 1D
# 1. Soit arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]). Inverser l’array.
# 2. Soit arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]).
# Inverser uniquement les lignes, puis uniquement les colonnes, puis uniquement la ligne 1.

def exo8():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(arr[::-1])
    arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(arr_2d[::-1])
    print(arr_2d[:, ::-1])
    print(arr_2d[0, ::-1])

# EXERCICE 9 : Algèbre linéaire (facultatif)
# 1. Générer un array 3x3 composé de 0.
# 2. Générer une matrice identité 3x3 avec des 1 sur la diagonale et des 0 ailleurs.
# 3. Soit a = np.array([[1, 3, 3], [1, 4, 3], [1, 3, 4]]). Calculer sa transposée, son inverse et
# son déterminant.
# 4. Soient a = np.array([[1, 2, 3], [4, 5, 6]]) et b = np.array([[4], [2], [1]])
# Calculer le produit matriciel de a et de b

def exo9():
    print(np.zeros((3, 3)))
    print(np.eye(3))
    a = np.array([[1, 3, 3], [1, 4, 3], [1, 3, 4]])
    print(a)
    print(a.T)
    print(np.linalg.inv(a))
    print(np.linalg.det(a))
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[4], [2], [1]])
    print(a.dot(b))

#EXERCICE 10 : Résolution d’un système d’équations linéaires (facultatif)
# Résoudre le système d’équations linéaires 3 * x0 + x1 = 9 et x0 + 2 * x1 = 8.

def exo10():
    a = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    print(np.linalg.solve(a, b))

exo3()