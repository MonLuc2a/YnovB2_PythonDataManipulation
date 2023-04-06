# EXERCICE 1 : Attribution d'un multi-index à 2 niveaux, ici aux colonnes
# Soit le DataFrame : df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5], 'C': [6, 7, 8], 'D': [9, 10, 11]})
# 1. Créer un multi-index pour regrouper les deux premières colonnes en ‘x’ et deux
# suivantes en ‘y’ et telles que les sous-colonnes soient ‘X’ et ‘Y’.
# 2. Afficher le Multi Index avec la commande : df.columns.
# 3. Regrouper les colonnes pour en obtenir deux ‘x’ et ‘y’ (utiliser les méthodes groupby
# et sum)
# 4. Faire de même avec les colonnes ‘X’ et ‘Y’.
# 5. Aplatir ce multi index et afficher le DF.

import pandas as pd
import numpy as np
def exo1():
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5], 'C': [6, 7, 8], 'D': [9, 10, 11]})
    print(df)
    df.columns = pd.MultiIndex.from_tuples([('x', 'X'), ('x', 'Y'), ('y', 'X'), ('y', 'Y')])
    print(df)
    print(df.groupby(level=0, axis=1).sum())
    print(df.groupby(level=1, axis=1).sum())
    print(df.stack().unstack(0))


# EXERCICE 2 : Modifications de Dataframes
# Soit df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
# 1. Renommer toutes les colonnes d’un coup en 'D', 'G' et 'H'.
# 2. Renommer seulement la colonne ‘D’ en ‘A’ et l’index ‘b’ en ‘m’ (attention, la
# modification doit se faire sur place).
# 3. Stocker la valeur en ligne 3 et colonne 2 sans utiliser leurs noms respectifs.
# 4. Réordonner les colonnes en ['G', 'H', 'A'] et les lignes en ['c', 'a', 'm'] (attention à bien
# faire la modification SUR le df).


def exo2():
    df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
    print(df)
    df.columns = ['D', 'G', 'H']
    print(df)
    df.rename(columns={'D': 'A'}, index={'b': 'm'}, inplace=True)
    print(df)
    print(df.loc['c', 'G'])
    df = df.reindex(columns=['G', 'H', 'A'], index=['c', 'a', 'm'])
    print(df)


# EXERCICE 3 : Ajout d'une colonne à un dataframe
# Soit df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c']).
# 1. Ajouter une colonne ‘E’ (de votre choix) au df à l’aide des Series de Pandas.
# 2. Ajouter une colonne ‘D’ remplie de 0 sans les Series.
# 3. Insérer une colonne ‘F’ (de votre choix) au début du df

def exo3():
    df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
    print(df)
    df['E'] = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    print(df)
    df['D'] = 0
    print(df)
    df.insert(0, 'F', pd.Series([1, 2, 3], index=['a', 'b', 'c']))
    print(df)


# EXERCICE 4 : Destruction de colonnes ou de lignes d'un dataframe
# Soit df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c']).
# 1. Détruire le colonne ‘A’ et les les lignes d'index 'a' et 'c'.
# 2. Reprendre le même df de départ, et scinder en deux pour obtenir un df avec les
# colonnes ‘A’ et ‘C’ et une série constituée de la colonne ‘B’.


def exo4():
    df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
    print(df)
    df.drop(['A'], axis=1, inplace=True)
    df.drop(['a', 'c'], axis=0, inplace=True)
    print(df)
    df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
    print(df)
    df2 = df[['A', 'C']]
    print(df2)
    df3 = df['B']
    print(df3)

# EXERCICE 5 : Modification des valeurs d'une colonne
# Soit df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c']).
# Modifier la colonne ‘B’ à l’aide de la méthode apply et des fonctions lambda afin que les
# valeurs inférieures à 5 deviennent NaN.

def exo5():
    df = pd.DataFrame({'A':[0, 1, 2], 'B':[3, 4, 5], 'C':[6, 7, 8]}, index = ['a', 'b', 'c'])
    print(df)
    df['B'] = df['B'].apply(lambda x: x if x >= 5 else None)
    print(df)

# EXERCICE 6 : Valeurs non définies
# Soit df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 20, 30], 'C': [7, 6, 5], 'D': [np.nan,
# np.nan, np.nan]}). Tester les commandes ci-dessous et les commenter.
# 1. df.dropna(how = 'all', axis = 0)
# 2. df.dropna(how = 'all', axis = 1)
# 3. df.dropna(how = 'any', axis = 0)
# 4. df.dropna(how = 'any', axis = 1)
# 5. df.fillna(123456)


def exo6():
    df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 20, 30], 'C': [7, 6, 5], 'D': [np.nan, np.nan, np.nan]})
    print(df)
    print(df.dropna(how = 'all', axis = 0)) # Supprime les lignes qui sont entièrement vides
    print(df.dropna(how = 'all', axis = 1)) # Supprime les colonnes qui sont entièrement vides
    print(df.dropna(how = 'any', axis = 0)) # Supprime les lignes qui ont au moins une valeur vide
    print(df.dropna(how = 'any', axis = 1)) # Supprime les colonnes qui ont au moins une valeur vide
    print(df.fillna(123456))


# EXERCICE 7 : Opérations sur tout le dataframe avec une ligne ou une colonne
# Soit df = pd.DataFrame({'A':[1, 4, 7], 'B':[2, 5, 8], 'C':[3, 6, 9]}, index = ['a', 'b', 'c']).
# Ajouter la colonne ‘A’ à toutes les colonnes.
# Ajouter la 1ère ligne à toutes les lignes.
# Renvoyer une série contenant les moyennes sur chaque ligne.
# Renvoyer une série contenant les moyennes sur chaque colonne.

def exo7():
    df = pd.DataFrame({'A':[1, 4, 7], 'B':[2, 5, 8], 'C':[3, 6, 9]}, index = ['a', 'b', 'c'])
    print(df)
    df = df + df['A']
    print(df)
    df = df + df.iloc[0]
    print(df)
    print(df.mean(axis=1))
    print(df.mean(axis=0))

# EXERCICE 8 : Tri selon les noms des lignes ou colonnes
# Soit df = pd.DataFrame({'Ex':[0, 1, 2], 'Ab':[3, 4, 5], 'Bio':[6, 7, 8]}, index = ['test', 'puis',
# 'quid']).
# 1. Classer les lignes par ordre alphabétique.
# 2. Classer les lignes par ordre alphabétique inversé.
# 3. Classer les colonnes par ordre alphabétique.
# 4. Classer les colonnes par ordre alphabétique inversé.
# 5. Renvoyer un df avec les lignes ET les colonnes par ordre alphabétique.
# 6. Classer la colonne Bio par ordre décroissant.


def exo8():
    df = pd.DataFrame({'Ex':[0, 1, 2], 'Ab':[3, 4, 5], 'Bio':[6, 7, 8]}, index = ['test', 'puis', 'quid'])
    print(df)
    print(df.sort_index(axis=0))
    print(df.sort_index(axis=0, ascending=False))
    print(df.sort_index(axis=1))
    print(df.sort_index(axis=1, ascending=False))
    print(df.sort_index(axis=0).sort_index(axis=1))
    print(df.sort_values(by='Bio', axis=0, ascending=False))


# EXERCICE 9 : Fonctions arrondi et valeur absolue
# Soit df = pd.DataFrame({'A':[-0.12345, 1.32165], 'B':[4.46287, -3.98764]}).
# Renvoyer un df dont toutes les valeurs sont arrondies au centième et positives.

def exo9():
    df = pd.DataFrame({'A':[-0.12345, 1.32165], 'B':[4.46287, -3.98764]})
    print(df)
    df = df.abs().round(2)
    print(df)

# EXERCICE 10 : Quelques résultats utiles en statistique
# Soit df = pd.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]},
# index = ['a1', 'a2', 'a3']).
# 1. Renvoyer une série contenant la ligne sur laquelle se trouve le min de chaque
# colonne.
# 2. Renvoyer une série contenant la colonne sur laquelle se trouve le min de chaque
# ligne.
# 3. Renvoyer la valeur seuil telle que 90% des valeurs sont en dessous.
# 4. Renvoyer pour chaque variable en colonne les valeurs des différents quantiles en
# ligne.
# 5. Effectuer les sommes de ligne en ligne puis de colonnes en colonnes (comme pour
# des effectifs cumulés croissants)

def exo10():
    df = pd.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]}, index = ['a1', 'a2', 'a3'])
    print(df)
    print(df.idxmin(axis=0))
    print(df.idxmin(axis=1))
    print(df.quantile(0.9))
    print(df.quantile([0.25, 0.5, 0.75]))
    print(df.cumsum(axis=0).cumsum(axis=1))

# EXERCICE 11 : Application d'une fonction à un dataframe
# Soit df = pd.DataFrame({'A': [1, 2, 3], 'B': [9, 8, 7]}).
# 1. Appliquer à df une fonction ajoutant 1 à chaque valeurs.
# 2. Appliquer à df une fonction d’agrégat donnant le max sur chaque ligne


def exo11():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [9, 8, 7]})
    print(df)
    print(df.apply(lambda x: x + 1))
    print(df.apply(lambda x: x.max(), axis=1))



