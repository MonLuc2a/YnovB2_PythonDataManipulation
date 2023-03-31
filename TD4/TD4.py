import pandas as pd
import numpy as np

# EXERCICE 1 : Créer une série
# 1. Créer une série Pandas s contenant les nombres 1, 5, 3, 9 ainsi qu’une valeur NaN et
# afficher cette série.
# 2. Changer les valeurs inférieures à 5 en 99.
# 3. Changer la valeur NaN en 100.



def exo1():
    s = pd.Series([1, 5, 3, 9, float('nan')])
    print(s)
    s[s < 5] = 99
    s = s.fillna(100)
    print(s)

# EXERCICE 2 : Modification de valeurs
# Soit la série s = pd.Series(['a', 'b', 'c']).
# Remplacer les 'a' par des 'A' et 'b' par des 'B' et renvoyer une série modifiée

def exo2():
    s = pd.Series(['a', 'b', 'c'])
    s = s.replace({'a': 'A', 'b': 'B'})
    print(s)

# EXERCICE 3 : Index d'une série et résumé statistique
# 1. Créer une série ayant pour index les string 'a', 'b', 'c' et 'd' et pour valeurs 1, 2, 5, 7.
# 2. Réindexer cette série avec les string 'c', 'b', 'a' et 'e'.
# 3. Afficher la série. Que s’est-il passé ?


def exo3():
    s = pd.Series([1, 2, 5, 7], index=['a', 'b', 'c', 'd'])
    s = s.reindex(['c', 'b', 'a', 'e'])
    print(s)

# EXERCICE 4 : Indexation des séries
# 1. Soit la série s = pd.Series([2, 5, 7, 3], index = ['a', 'b', 'c', 'd']). Accéder à la valeur
# d'index 'b'.
# 2. Accéder aux 3ème et 4ème valeurs en une seule commande.

def exo4():
    s = pd.Series([2, 5, 7, 3], index = ['a', 'b', 'c', 'd'])
    print(s['b'])
    print(s[2:])


# EXERCICE 5 : Tri d'une série
# Soit la série s = pd.Series([2, 5, 7, 3], index = ['e', 'b', 'c', 'd']). Trier les valeurs d'une série en
# fonction du nom des index et afficher cette série triée.

def exo5():
    s = pd.Series([2, 5, 7, 3], index = ['e', 'b', 'c', 'd'])
    s = s.sort_index()
    print(s)


# EXERCICE 6 : Opérations sur les séries
# Soient les séries s1 = pd.Series([1, 2, 3], ['a', 'b', 'c']) et s2 = pd.Series([4, 5, 6], ['a', 'd', 'c']).
# Additionner ces deux séries et commenter le résultat.
# Éliminer les lignes avec NaN de cette série-somme.

def exo6():
    s1 = pd.Series([1, 2, 3], ['a', 'b', 'c'])
    s2 = pd.Series([4, 5, 6], ['a', 'd', 'c'])
    s = s1 + s2
    print(s)
    s = s.dropna()
    print(s)


# EXERCICE 7 :
# Soit la série s = pd.Series([1, 4, 3],['z', 'a', 'n']).
# Appliquer à s une fonction numérique permettant de multiplier les valeurs par 2 plus 1.

def exo7():
    s = pd.Series([1, 4, 3],['z', 'a', 'n'])
    s = s.apply(lambda x: x * 2 + 1)
    print(s)

# EXERCICE 8 : Comptage de valeurs
# Soit la série s = pd.Series([1, 3, 5, 3, 5, 2, 8, 3, 1, 7, 4, 2, 3, 6, 3]).
# Trouver une méthode renvoyant une série comptant le nombre d'occurrences pour chaque
# valeur.

def exo8():
    s = pd.Series([1, 3, 5, 3, 5, 2, 8, 3, 1, 7, 4, 2, 3, 6, 3])
    s = s.value_counts()
    print(s)


# EXERCICE 9 : Localiser des valeurs NaN
# Soit la série s = pandas.Series([1, 2, 3, np.nan]). Localiser les valeurs Nan

def exo9():
    s = pd.Series([1, 2, 3, float('nan')])
    print(s.isnull())


# EXERCICE 10 : Appartenance à une série
# Soit la série s = pd.Series(['a', 'b', 'c']).
# Tester l’appartenance à la série des string 'a', 'c' et 'x'.

def exo10():
    s = pd.Series(['a', 'b', 'c'])
    print(s.isin(['a', 'c', 'x']))


# EXERCICE 11 : Conversion de Series en DataFrame
# Soit la série s = pd.Series([10, 20, 30]).
# Convertir cette série en un DataFrame dont le nom de colonne sera ‘A’.

def exo11():
    s = pd.Series([10, 20, 30])
    df = pd.DataFrame(s, columns=['A'])
    print(df)


# EXERCICE 12 : Créer un dataframe (df)
# 1. Soit l’array a = np.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]]). Créer un
# DataFrame contenant a, dont les noms des colonnes seront 'A', 'B', 'C' et 'D et les
# noms des index seront 'a1', 'a2' et 'a3'.
# 2. Trouver une autre manière de créer ce même df en utilisant un dictionnaire.
# 3. Donner un nom à l’index et un nom aux colonnes.

def exo12():
    a = np.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
    df = pd.DataFrame(a, index=['a1', 'a2', 'a3'], columns=['A', 'B', 'C', 'D'])
    print(df)
    df = pd.DataFrame({'A': a[:, 0], 'B': a[:, 1], 'C': a[:, 2], 'D': a[:, 3]}, index=['a1', 'a2', 'a3'])
    print(df)
    df.index.name = 'index'
    df.columns.name = 'columns'
    print(df)

# EXERCICE 13 : Utiliser des Séries avec index pour construire un DataFrame
# Soient les séries s1 = pd.Series([2, 3, 4], index = ['a', 'b', 'c']) et s2 = pd.Series([6, 7, 8], index =
# ['b', 'a', 'd']).
# 1. Construire un df à l’aide de ces deux séries.
# 2. Afficher sa forme

def exo13():
    s1 = pd.Series([2, 3, 4], index = ['a', 'b', 'c'])
    s2 = pd.Series([6, 7, 8], index = ['b', 'a', 'd'])
    df = pd.DataFrame({'s1': s1, 's2': s2})
    print(df)
    print(df.shape)


# EXERCICE 14 : Accéder à un sous-ensemble du dataframe par noms ou indice
# Soit df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c']).
# 1. Accéder à la valeur en index ‘c’ et colonne ‘B’.
# 2. Réaffecter cette valeur en 96.
# 3. Renvoyer la série constituée de la 1ère colonne.
# 4. Renvoyer un df constitué de la 1ère colonne.
# 5. Renvoyer un df contenant la 2ème ligne.
# 6. Renvoie le dataframe avec les lignes 1 à 3 exclue et les colonnes numéros 0 ET 1 sans
# utiliser les noms des colonnes/index.


def exo14():
    df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c'])
    print(df.loc['c', 'B'])
    df.loc['c', 'B'] = 96
    print(df)
    print(df['A'])
    print(df[['A']])
    print(df.loc['b', :])
    print(df.iloc[1:3, 0:2])


# EXERCICE 15 : Accès selon une condition
# 1. Avec le df de l’exercice précédent, renvoyer un df booléen affichant True sur les
# valeurs supérieures à 2.
# 2. Renvoyer un df dans lequel les valeurs inférieures ou égales à 2 sont remplacées par
# NaN.

def exo15():
    df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c'])
    print(df > 2)
    print(df.where(df > 2))

#     EXERCICE 16 : Accès selon une condition (suite)
# Soit le dataframe df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c']).
# 1. Renvoyer un df booléen affichant True sur les valeurs égales à 5 en utilisant la
# méthode .isin()
# 2. Renvoyer un df dans lequel les valeurs différentes de 5 sont remplacées par NaN.


def exo16():
    df = pd.DataFrame({'A':[0, 1, 5], 'B':[2, 3, 6]}, index = ['a', 'b', 'c'])
    print(df.isin([5]))
    print(df.where(df.isin([5])))


# EXERCICE 17 : Création d’un fichier csv et écriture d'un dataframe dans le fichier
# Soit le dataframe :
# df_export = pd.DataFrame({'A':[0, 3, 4],'B':[2, 9, 7],'C':[6, 5, 5]}, index = ['a', 'b', 'c']).
# 1. Exporter ce df dans un fichier .csv et constater le résultat.
# 2. Formater cet export à l’aide du kwarg sep = ';' et constater le résultat.


def exo17():
    df_export = pd.DataFrame({'A':[0, 3, 4],'B':[2, 9, 7],'C':[6, 5, 5]}, index = ['a', 'b', 'c'])
    df_export.to_csv('df_export.csv')
    df_export.to_csv('df_export_sep.csv', sep=';')


# EXERCICE 18 : Lecture d'un dataframe à partir d'un fichier
# 1. Importer le df du fichier .csv précédent et formater correctement ce df.
# 2. Imposer les noms 'X1', 'X2' et 'X3' aux nouvelles colonnes lors de l’import.

def exo18():
    df_import = pd.read_csv('df_export_sep.csv', sep=';')
    print(df_import)
    df_import = pd.read_csv('df_export_sep.csv', sep=';', names=['X1', 'X2', 'X3'])
    print(df_import)




exo18()
