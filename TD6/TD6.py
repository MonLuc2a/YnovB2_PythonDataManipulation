import pandas as pd
import numpy as np


# EXERCICE 1 : Juxtaposition de lignes de dataframes
# 1. Soient df1 = pd.DataFrame({'A': [9, 50], 'B': [51, 92]}, index = [1, 2]) et df2 =
# pd.DataFrame({'A': [64, 77], 'B': [24, 93]}, index = [1, 2]).
# a. Concaténer les deux dataframes df1 avec au-dessus de df2.
# b. Refaire la concaténation en ignorant les valeurs de l’index dans la
# concaténation.
# c. Refaire la concaténation en ajoutant un niveau hiérarchique d'index en
# attribuant une clef à chaque dataframe de départ
# 2. Soient df1 = pandas.DataFrame({'A': [3, 5], 'B': [1, 2]}) et df2 =
# pandas.DataFrame({'A': [6, 7], 'C': [4, 9]}).
# a. Concaténer les deux dataframes df1 avec au-dessus de df2.
# b. Commenter le résultat.
# c. Refaire la concaténation en ne conservant que les colonnes communes
# d. Reprendre les df de l’exercice et les concaténer côte-à-côte.

def exo1():
    df1 = pd.DataFrame({'A': [9, 50], 'B': [51, 92]}, index = [1, 2])
    df2 = pd.DataFrame({'A': [64, 77], 'B': [24, 93]}, index = [1, 2])
    print(pd.concat([df1, df2]))
    print(pd.concat([df1, df2], ignore_index = True))
    print(pd.concat([df1, df2], keys = ['df1', 'df2']))
    df1 = pd.DataFrame({'A': [3, 5], 'B': [1, 2]})
    df2 = pd.DataFrame({'A': [6, 7], 'C': [4, 9]})
    print(pd.concat([df1, df2]))
    print(pd.concat([df1, df2], join = 'inner'))
    print(pd.concat([df1, df2], axis = 1))


# EXERCICE 2 : Jointures
# 1. Soient df1 = pandas.DataFrame({'A': [31, 54], 'B': [11, 92]}) et df2 =
# pandas.DataFrame({'A': [500, 33, 78], 'C': [19, 12, 0]})
# a. Effectuer une jointure simple qui, par défaut, utilise les noms des colonnes
# qui sont communs.
# b. Comparer avec une jointure externe de ces deux dataframes.
# 2. Soient df1 = pandas.DataFrame({'A': [3, 5], 'B': [1, 2]}, index = [0, 1]) et df2 =
# pandas.DataFrame({'D': [5, 3, 7], 'E': [9, 2, 0]}, index = [2, 1, 0]).
# a. Effectuer une jointure interne sur l’index de ces deux dataframes.
# b. Puis une jointure externe.


def exo2():
    df1 = pd.DataFrame({'A': [31, 54], 'B': [11, 92]})
    df2 = pd.DataFrame({'A': [500, 33, 78], 'C': [19, 12, 0]})
    print(pd.merge(df1, df2))
    print(pd.merge(df1, df2, how = 'outer'))
    df1 = pd.DataFrame({'A': [3, 5], 'B': [1, 2]}, index = [0, 1])
    df2 = pd.DataFrame({'D': [5, 3, 7], 'E': [9, 2, 0]}, index = [2, 1, 0])
    print(pd.merge(df1, df2, left_index = True, right_index = True))
    print(pd.merge(df1, df2, left_index = True, right_index = True, how = 'outer'))


# EXERCICE 3 : Pivotage
# Soit df = pandas.DataFrame({'A': ['a', 'a', 'b', 'b', 'c', 'c'], 'T': ['yes', 'no', 'yes', 'no', 'yes', 'no'],
# 'V': [4, 2, 5, 2, 7, 3]}).
# Renvoyer un dataframe pivot de df et commenter

def exo3():
    df = pd.DataFrame({'A': ['a', 'a', 'b', 'b', 'c', 'c'], 'T': ['yes', 'no', 'yes', 'no', 'yes', 'no'],
                       'V': [4, 2, 5, 2, 7, 3]})
    print(df.pivot(index = 'A', columns = 'T', values = 'V'))



# EXERCICE 4 : Stacking : consiste à empiler les différentes colonnes d'un dataframe
# Soit df = pandas.DataFrame({'A': [5, 4, 1], 'B': [8, 9, 6]}).
# 1. Renvoyer une série composée des colonnes de df empilée.
# 2. Transformer cette série en un df dont les anciens noms de colonnes formeront une
# nouvelle colonne.
# 3. Réinitialiser l’index et renommer les colonnes.

def exo4():
    df = pd.DataFrame({'A': [5, 4, 1], 'B': [8, 9, 6]})
    print(df.stack())
    print(df.stack().reset_index())
    print(df.stack().reset_index().rename(columns = {'level_0': 'index', 'level_1': 'col', 0: 'val'}))


# EXERCICE 5 : Réorganisation avec melt
# Soit df = pandas.DataFrame({'A': ['a', 'b', 'b'], 'B': ['yes', 'no', 'no'], 'val1': [4, 2, 5], 'val2': [7, 8,
# 10], 'val3': [9, 3, 15]}).
# Réorganiser ce df afin que les trois dernières colonnes se regroupent et en forment deux
# (une pour les noms de colonnes et une pour les valeurs empilées)

def exo5():
    df = pd.DataFrame({'A': ['a', 'b', 'b'], 'B': ['yes', 'no', 'no'], 'val1': [4, 2, 5], 'val2': [7, 8, 10], 'val3': [9, 3, 15]})
    print(df.melt(id_vars = ['A', 'B'], var_name = 'col', value_name = 'val'))


# EXERCICE 6 : Utilisation de la méthode groupby
# Soit df = pandas.DataFrame({'A': ['a', 'b', 'a', 'a', 'b'], 'B': [8, 4, 5, 10, 8], 'C': ['x', 'x', 'y', 'y', 'x'],
# 'D': [0, 1, 2, 3, 4]}).
# Créer une instance groupby indexé sur la colonne ‘A’ et l’afficher.
# Appliquer les méthodes sum(), reset_index() et size() et commenter.
# Faire de même avec une instance groupby indexé sur les colonnes ‘A’ et ‘C’.

def exo6():
    df = pd.DataFrame({'A': ['a', 'b', 'a', 'a', 'b'], 'B': [8, 4, 5, 10, 8], 'C': ['x', 'x', 'y', 'y', 'x'],
                       'D': [0, 1, 2, 3, 4]})
    print(df.groupby('A').sum())
    print(df.groupby('A').sum().reset_index())
    print(df.groupby('A').size())
    print(df.groupby(['A', 'C']).sum())
    print(df.groupby(['A', 'C']).sum().reset_index())
    print(df.groupby(['A', 'C']).size())


# EXERCICE 7 : Agrégation de plusieurs statistiques
# Soit df = pandas.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5],'C': [6, 7, 8], 'D': [9, 10, 11]}).
# Renvoyer un df groupby avec ‘A’ en index et affichant pour chaque colonne : min, max,
# moyenne, médiane.

def exo7():
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5],'C': [6, 7, 8], 'D': [9, 10, 11]})
    print(df.groupby('A').agg([np.min, np.max, np.mean, np.median]))

