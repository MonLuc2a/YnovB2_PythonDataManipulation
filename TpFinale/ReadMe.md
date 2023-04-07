Ce script crée un jeu Connect 4 avec une interface utilisateur graphique (GUI) en utilisant les bibliothèques tkinter, numpy et pandas. L'utilisateur joue contre un adversaire IA, qui choisit les meilleurs mouvements possibles en se basant sur les données des parties précédentes stockées dans un DataFrame pandas.

Le script est divisé en trois classes :

Connect4 : représente le plateau de jeu et gère la logique du jeu, comme l'abandon d'une pièce, la recherche d'un gagnant et le passage d'un joueur à l'autre.

Connect4AI : Hérite de Connect4 et étend la fonctionnalité avec des méthodes spécifiques à l'IA comme la simulation des mouvements, les positions de score et l'évaluation des fenêtres.

Connect4GUI : Crée l'interface graphique du jeu à l'aide de tkinter, gère les entrées de l'utilisateur et met à jour le plateau de jeu.
Lorsque le script est exécuté, il crée une instance Connect4 et initialise l'interface graphique pour démarrer le jeu. L'IA choisit ses mouvements en recherchant dans le DataFrame les meilleurs mouvements possibles en fonction de l'état actuel du jeu.

