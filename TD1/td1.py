import math
import os
import random
import time
from unittest import case


def exo1():
    print(eval("7+3**6"))
    print(eval("(3 + 4)**3"))
    print(eval("3**6 - 5"))
    print(eval("(1+2**8)*5"))
    print(eval("(2+1**8)*7"))


def exo2():
    # (1 + 2) ** 3 = 27
    # "da" * 4 = 'dadadada'
    # "Da" + 3 = erreur
    # ("Pa" + "La") * 2 = 'PaLaPaLa'
    # ("Da" * 4) / 2 = erreur
    # 5 / 2 = 2.5
    # 5 // 2 = 2
    # 5 % 2 = 1
    # str(4) * int("3") = '444'
    # int("3") + float("3.2") = 6.2
    # str(3) * float("3.2") = erreur
    # str(3 / 4) * 2 = '0.75.75'
    pass

# Générez une chaîne de caractères qui ne contient que des A de longueur 20, sans taper
# littéralement toutes les lettres, suivie d’une chaîne de caractères qui contient B et C alternés
# de longueur 40.

def exo3a():
    n = 0
    while n < 20:
        print("A")
        n += 1
    n = 0
    while n < 20:
        print("BC")
        n += 1

def exo3b():
    print("A" * 20)
    print("BC" * 20)

# En utilisant l’écriture formatée, affichez en une seule ligne les variables a, b et c dont les
# valeurs sont respectivement la chaîne de caractères "salut", le nombre entier 102 et le float
# 10.318. La variable c sera affichée avec 2 décimales.

def exo4():
    a = "salut"
    b = 102
    c = 10.318

    print(f"{a} {b} {c:.2f}")


# Constituez une liste “semaine” contenant les 7 jours de la semaine.
# 1. À partir de cette liste, comment récupérez-vous seulement les 5 premiers jours de la
# semaine d’une part, et ceux du week-end d’autre part ? Utilisez pour cela l’indiçage.
# 2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre
# indiçage).
# 3. Trouvez deux manières d'accéder au dernier jour de la semaine.
# 4. Inversez les jours de la semaine en une commande.

def exo5():
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    print(jours[:5])
    print(jours[5:])

    print(jours[:-2])
    print(jours[-2:])

    print(jours[-1])
    print(jours[6])

    print(jours[::-1])

# Créez 4 listes “hiver”, “printemps”, “été” et “automne” contenant les mois correspondants à
# ces saisons. Créez ensuite une liste “saisons” contenant les listes hiver, printemps, été et
# automne. Prévoyez ce que renvoient les instructions suivantes, puis vérifiez-le dans
# l’interpréteur :
# 1. saisons[2]
# 2. saisons[1][0]
# 3. saisons[1:2]
# 4. saisons[:][1]. Comment expliquez-vous ce dernier résultat ?
def exo6():
    hiver = ["janvier", "février", "mars"]
    printemps = ["avril", "mai", "juin"]
    ete = ["juillet", "août", "septembre"]
    automne = ["octobre", "novembre", "décembre"]

    saisons = [hiver, printemps, ete, automne]

    print(saisons[2])
    print(saisons[1][0])
    print(saisons[1:2])
    print(saisons[:][1])

    # ['juillet', 'août', 'septembre']
    # avril
    # [['avril', 'mai', 'juin']]
    # ['avril', 'mai', 'juin']


# Affichez la table de multiplication par 9 en une seule commande avec les instructions
# range() et list().
def exo7():
    for i in range(0, 11):
        print(list(range(i * 9, i * 9 + 9, 9)))


# Répondez à la question suivante en une seule commande.
# Combien y a-t-il de nombres pairs dans l’intervalle [2, 10000] inclus ?
def exo8():
    print(len([i for i in range(2, 10000) if i % 2 == 0]))

# Soit la liste de nombres [8, 3, 12.5, 45, 25.5, 52, 1]. Triez les nombres de cette liste par ordre
# croissant, sans utiliser la fonction sort(). Les fonctions et méthodes min(), .append() et
# .remove() vous seront utiles
def exo9():
    l = [8, 3, 12.5, 45, 25.5, 52, 1]
    l2 = []
    while l:
        m = min(l)
        l2.append(m)
        l.remove(m)
    print(l2)

# Créez une fonction “seq_alea()” qui prend comme argument un entier positif “taille”
# représentant le nombre de bases de la séquence et qui renvoie une séquence d’ADN
# aléatoire sous forme d’une liste de bases. Utilisez la méthode .append() pour ajouter les
# différentes bases à la liste et la fonction random.choice() du module random pour choisir
# une base parmi les 4 possibles : “A” , “T” , “G” , “C”.
# Utilisez cette fonction pour générer aléatoirement une séquence d’ADN de 15 bases.
def seq_alea(taille): #exo10
    import random
    seq = []
    for i in range(taille):
        seq.append(random.choice(["A", "T", "G", "C"]))
    print(seq)

# La liste ci-dessous représente la séquence d’un brin d’ADN :
# ["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
# Créez un script qui transforme cette séquence en sa séquence complémentaire.
# Rappel : la séquence complémentaire s’obtient en remplaçant A par T, T par A, C par G et G
# par C
def exo11():
    seq=["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
    seq2 = []
    for i in seq:
        if i == "A":
            seq2.append("T")
        elif i == "T":
            seq2.append("A")
        elif i == "C":
            seq2.append("G")
        elif i == "G":
            seq2.append("C")
    print(seq2)

# Soit la liste de nombres liste = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2].
# À partir de liste, créez une nouvelle liste sans les doublons, triez-la et affichez-la
def exo12():
    liste = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
    liste2 = []
    for i in liste:
        if i not in liste2:
            liste2.append(i)
    liste2.sort()
    print(liste2)

# Trouvez le nombre mystère qui répond aux conditions suivantes :
# ❖ Il est composé de 3 chiffres.
# ❖ Il est strictement inférieur à 300.
# ❖ Il est pair.
# ❖ Deux de ses chiffres sont identiques.
# ❖ La somme de ses chiffres est égale à 7.
# On vous propose d’employer une méthode dite « brute force », c’est-à-dire d’utiliser une
# boucle et à chaque itération de tester les différentes conditions.
def exo13():
    for i in range(100, 300):
        chiffres = [int(chiffre) for chiffre in str(i)]
        if i % 2 == 0:
            if sum(chiffres) == 7:
                if chiffres[0] == chiffres[1] or chiffres[0] == chiffres[2] or chiffres[1] == chiffres[2]:
                    print(f"Le nombre mystère est: {i}")
                    break
# Voici le début du triangle de Pascal :
# 1| 1
# 2| 1 1
# 3| 1 2 1
# 4| 1 3 3 1
# 5| 1 4 6 4 1
# 6| 1 5 10 10 5 1
# 7| [...]
# Déduisez comment une ligne est construite à partir de la précédente. Par exemple, à partir
# de la ligne 2 (1 1), construisez la ligne suivante (ligne 3 : 1 2 1) et ainsi de suite.
# Implémentez cette construction en Python. Généralisez à l’aide d’une boucle.
# Écrivez dans un fichier pascal.out les 10 premières lignes du triangle de Pascal.
def exo14():
    nb_lignes = 10
    ligne_courante = [1]
    print(" ".join(str(x) for x in ligne_courante))
    for i in range(nb_lignes - 1):
        ligne_suivante = [1]

        for j in range(len(ligne_courante) - 1):
            ligne_suivante.append(ligne_courante[j] + ligne_courante[j + 1])

        ligne_suivante.append(1)
        print(" ".join(str(x) for x in ligne_suivante))
        ligne_courante = ligne_suivante


# Constituez une liste “semaine” contenant le nom des sept jours de la semaine.
# En utilisant une boucle, écrivez chaque jour de la semaine ainsi que les messages suivants :
# ❖ “Au travail” s’il s’agit du lundi au jeudi;
# ❖ “Chouette c'est vendredi” s’il s’agit du vendredi;
# ❖ “Repos ce week-end” s’il s’agit du samedi ou du dimanche.
# Ces messages ne sont que des suggestions, vous pouvez laisser libre cours à votre
# imagination.
def exo15():
    semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    for i in semaine:
        if i == "lundi" or i == "mardi" or i == "mercredi" or i == "jeudi":
            print(f"{i} : Au travail")
        elif i == "vendredi":
            print(f"{i} : Chouette c'est vendredi")
        elif i == "samedi" or i == "dimanche":
            print(f"{i} : Repos ce week-end")

# La fonction min() de Python renvoie l’élément le plus petit d’une liste constituée de valeurs
# numériques ou de chaînes de caractères. Sans utiliser cette fonction, créez un script qui
# détermine le plus petit élément de la liste [8, 4, 6, 1, 5].
def exo16():
    liste = [8, 4, 6, 1, 5]
    min = liste[0]
    for i in liste:
        if i < min:
            min = i
    print(min)

# La liste ci-dessous représente une liste de lettres :
# ["A", "R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
# Calculez la fréquence des lettres "W", "R", "A", "G" dans cette liste.
def exo17():
    liste = ["A", "R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
    dico = {}
    for i in liste:
        if i in dico:
            dico[i] += 1
        else:
            dico[i] = 1
    print(dico)

# Voici les notes d’un étudiant : 14, 9, 13, 15 et 12. Créez un script qui affiche la note
# maximum (utilisez la fonction max()), la note minimum (utilisez la fonction min()) et qui
# calcule la moyenne.
# Affichez la valeur de la moyenne avec deux décimales. Affichez aussi la mention obtenue
# sachant que la mention est « passable » si la moyenne est entre 10 inclus et 12 exclus, «
# assez bien » entre 12 inclus et 14 exclus et « bien » au-delà de 14.

def exo18():
    notes = [14, 9, 13, 15, 12]
    print(f"La note maximum est: {max(notes)}")
    print(f"La note minimum est: {min(notes)}")
    print(f"La moyenne est: {round(sum(notes) / len(notes), 2)}")
    if 10 <= sum(notes) / len(notes) < 12:
        print("La mention est: passable")
    elif 12 <= sum(notes) / len(notes) < 14:
        print("La mention est: assez bien")
    elif sum(notes) / len(notes) >= 14:
        print("La mention est: bien")


# Construisez une boucle qui parcourt les nombres de 0 à 20 et qui affiche les nombres pairs
# inférieurs ou égaux à 10 d’une part, et les nombres impairs strictement supérieurs à 10
# d’autre part.
# Pour cet exercice, vous pourrez utiliser l’opérateur modulo % qui renvoie le reste de la
# division entière entre deux nombres et dont voici quelques exemples d’utilisation :
# 1| >>> 4 % 3
# 2| 1
# 3| >>> 5 % 3
# 4| 2
# 5| >>> 4 % 2
# 6| 0
# 7| >>> 5 % 2
# 8| 1
# 9| >>> 6 % 2
# 10| 0
# 11| >>> 7 % 2
# 12| 1
# Vous remarquerez qu’un nombre est pair lorsque le reste de sa division entière (opérateur
# modulo %) par 2 est nul.

def exo19():
    for i in range(21):
        if i % 2 == 0 and i <= 10:
            print(i)
        elif i % 2 != 0 and i > 10:
            print(i)

# La conjecture de Syracuse est une conjecture mathématique qui reste non prouvée à ce jour
# et qui est définie de la manière suivante : soit un entier positif n. Si n est pair, alors le diviser
# par 2. Si il est impair, alors le multiplier par 3 et lui ajouter 1. En répétant cette procédure, la
# suite de nombres atteint la valeur 1 puis se prolonge indéfiniment par une suite de trois
# valeurs triviales appelée cycle trivial 4 ; 2 ; 1.
# Jusqu’à présent, la conjecture de Syracuse, selon laquelle depuis n’importe quel entier
# positif la suite de Syracuse atteint 1, n’a pas été mise en défaut.
# Par exemple, les premiers éléments de la suite de Syracuse si on prend comme point de
# départ 10 sont : 10, 5, 16, 8, 4, 2, 1. . .
# Créez un script qui, partant d’un entier positif n (par exemple 10 ou 20), crée une liste des
# nombres de la suite de Syracuse.
# Avec différents points de départ (c’est-à-dire avec différentes valeurs de n), la conjecture de
# Syracuse est-elle toujours vérifiée ?
# Remarque : pour cet exercice, vous avez besoin de faire un nombre d’itérations inconnu
# pour que la suite de Syracuse atteigne le chiffre 1 puis entame son cycle trivial. Vous pourrez
# tester votre algorithme avec un nombre arbitraire d’itérations, typiquement 20 ou 100,
# suivant votre nombre n de départ. Pensez à la boucle while

def exo20():
    n = int(input("Entrez un nombre: "))
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        liste.append(int(n))
    print(liste)

# Un nombre premier est un entier naturel qui admet exactement deux diviseurs distincts
# entiers et positifs (qui sont alors 1 et lui-même). Cette définition exclut 1, qui n’a qu’un seul
# diviseur entier positif. Par opposition, un nombre non nul produit de deux nombres entiers
# différents de 1 est dit composé. Par exemple 6 = 2×3 est composé, tout comme 21 = 3×7,
# mais 11 est premier car 1 et 11 sont les seuls diviseurs de 11. Les nombres 0 et 1 ne sont ni
# premiers ni composés.
# Déterminez les nombres premiers inférieurs à 100. Combien y a-t-il de nombres premiers
# entre 0 et 100 ? Pour vous aider, nous vous proposons plusieurs méthodes.
# Deux méthodes différentes :
# 1. Pour chaque nombre de 2 à 100, calculez le reste de la division entière (avec
# l’opérateur modulo %) depuis 1 jusqu’à lui-même. Si c’est un nombre premier, il aura
# exactement deux nombres pour lesquels le reste de la division entière est égal à 0 (1
# et lui-même). Si ce n’est pas un nombre premier, il aura plus de deux nombres pour
# lesquels le reste de la division entière est égal à 0.
# 2. [Plus efficace] Parcourez tous les nombres de 2 à 100 et vérifiez si ceux-ci sont
# composés, c’est-à-dire qu’ils sont le produit de deux nombres premiers.
# Pratiquement, cela consiste à vérifier que le reste de la division entière entre le
# nombre considéré et chaque nombre premier déterminé jusqu’à maintenant est nul.
# Le cas échéant, ce nombre n’est pas premier. Attention, pour cette méthode, il faudra
# initialiser la liste de nombres premiers avec le premier nombre premier (donc 2 !).

def exo21():
    liste = []
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            liste.append(i)
    print(liste)

# Défi n° 22 : Recherche d’un nombre par dichotomie
# La recherche par dichotomie est une méthode qui consiste à diviser (en général en parties
# égales) un problème pour en trouver la solution. À titre d’exemple, voici une discussion
# entre Pierre et Patrick dans laquelle Pierre essaie de deviner le nombre (compris entre 1 et
# 100 inclus) auquel Patrick a pensé.
# — [Patrick] « C’est bon, j’ai pensé à un nombre entre 1 et 100. »
# — [Pierre] « OK, je vais essayer de le deviner. Est-ce que ton nombre est plus petit ou plus
# grand que 50 ? »
# — [Patrick] « Plus grand. »
# — [Pierre] « Est-ce que ton nombre est plus petit, plus grand ou égal à 75 ? »
# — [Patrick] « Plus grand. »
# — [Pierre] « Est-ce que ton nombre est plus petit, plus grand ou égal à 87 ? »
# — [Patrick] « Plus petit. »
# — [Pierre] « Est-ce que ton nombre est plus petit, plus grand ou égal à 81 ? »
# — [Patrick] « Plus petit. »
# — [Pierre] « Est-ce que ton nombre est plus petit, plus grand ou égal à 78 ? »
# — [Patrick] « Plus grand. »
# — [Pierre] « Est-ce que ton nombre est plus petit, plus grand ou égal à 79 ? »
# — [Patrick] « Égal. C’est le nombre auquel j’avais pensé. Bravo ! »
# Pour arriver rapidement à deviner le nombre, l’astuce consiste à prendre à chaque fois la
# moitié de l’intervalle dans lequel se trouve le nombre.
# Créez un script qui reproduit ce jeu de devinettes et qui compte le nombre d’essais. Vous
# pensez à un nombre entre 1 et 100 et l’ordinateur essaie de le deviner par dichotomie en
# vous posant des questions.
# Votre programme utilisera la fonction input() pour interagir avec l’utilisateur. Voici un
# exemple de son fonctionnement :
# 1| >>> lettre = input (" Entrez une lettre : ")
# 2| Entrez une lettre : P
# 3| >>> print ( lettre )
# 4| P

def exo22():
    min = 1
    max = 100
    trouve = False
    while not trouve:
        nb = (min + max) // 2
        print("Est-ce que ton nombre est plus petit, plus grand ou égal à", nb, "?")
        reponse = input()
        if reponse == "plus petit" or reponse == "-":
            max = nb - 1
        elif reponse == "plus grand" or reponse == "+":
            min = nb + 1
        elif reponse == "égal" or reponse == "=":
            trouve = True
        else :
            print("Je n’ai pas compris votre réponse.")
    print("C’est le nombre auquel j’avais pensé. Bravo !")

# Soit la liste ["vache", "souris", "levure", "bactérie"]. Affichez l’ensemble des éléments de
# cette liste (un élément par ligne) de trois manières différentes (deux avec for et une avec
# while).

def exo23():
    liste = ["vache", "souris", "levure", "bactérie"]
    for i in liste:
        print(i)

    i = 0
    while i < len(liste):
        print(liste[i])
        i += 1

    i = 0
    while True:
        print(liste[i])
        i += 1
        if i == len(liste):
            break

# Avec une boucle, affichez les nombres de 1 à 10 sur une seule ligne.
# Conseil : n’hésitez pas à relire le début du chapitre sur l’affichage qui discute de la fonction
# print().

def exo24():
    for i in range(1, 11):
        print(i, end=" ")

# Défi n° 25 : Nombres pairs et impairs
# Soit impairs la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. Écrivez un programme
# qui, à partir de la liste impairs, construit une liste pairs dans laquelle tous les éléments de
# impairs sont incrémentés de 1.

def exo25():
    impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    pairs = []
    for i in impairs:
        pairs.append(i + 1)
    print(pairs)

#Avec les fonctions list() et range(), créez la liste “entiers” contenant les nombres entiers pairs
# de 2 à 20 inclus.
# Calculez ensuite le produit des nombres consécutifs en utilisant une boucle. Exemple pour
# les premières itérations :
# 1| 8
# 2| 24
# 3| 48
# 4| [...]

def exo26():
    entiers = list(range(2, 21, 2))
    produit = 1
    for i in entiers:
        produit *= i
    print(produit)

#Créez un script qui dessine un triangle comme celui-ci :
# 1| *
# 2| **
# 3| ***
# 4| ****
# 5| *****
# 6| ******
# 7| *******
# 8| ********
# 9| *********
# 10| **********
# 2. Essayez de faire évoluer votre script pour dessiner la pyramide à partir d’un nombre
# arbitraire de lignes N. Vous pourrez demander à l’utilisateur le nombre de lignes de la
# pyramide avec les instructions suivantes qui utilisent la fonction input().
# 3. Essayez de faire évoluer votre script pour qu’il affiche un sapin (avec tronc !)

def exo27():
    nb = int(input("Nombre de lignes ? "))
    for i in range(1, nb + 1):
        print("*" * i)
    print(" " * (nb // 2) + "|")


# Imaginons que l’on souhaite parcourir tous les éléments d’une matrice carrée, c’est-à-dire
# d’une matrice qui est constituée d’autant de lignes que de colonnes.
# 1. Créez un script qui parcourt chaque élément de la matrice et qui affiche le numéro
# de ligne et de colonne uniquement avec des boucles for.
# Pour une matrice 2 × 2, l’affichage attendu est :
# 1| ligne colonne
# 2| 1 1
# 3| 1 2
# 4| 2 1
# 5| 2 2
# 2. Testez pour une matrice 3 × 3, puis 5 × 5, et enfin 10 × 10.
# 3. Créez une seconde version de votre script, cette fois-ci avec deux boucles while.

def exo28():
    nb = int(input("Taille de la matrice ? "))
    print("ligne colonne")
    for i in range(1, nb + 1):
        for j in range(1, nb + 1):
            print(i, j)

    print("ligne colonne")
    i = 1
    while i <= nb:
        j = 1
        while j <= nb:
            print(i, j)
            j += 1
        i += 1


# On imagine une puce qui se déplace aléatoirement sur une ligne, en avant ou en arrière, par
# pas de 1 ou -1. Par exemple, si elle est à l’emplacement 0, elle peut sauter à l’emplacement 1
# ou -1; si elle est à l’emplacement 2, elle peut sauter à l’emplacement 3 ou 1, etc.
# Avec une boucle while, simuler le mouvement de cette puce de l’emplacement initial 0 à
# l’emplacement final 5. Combien de sauts sont nécessaires pour réaliser ce parcours ?
# Relancez plusieurs fois le programme.
# Trouvez-vous le même nombre de sauts à chaque exécution ?
# Conseil : vous utiliserez l’instruction random.choice([-1,1]) qui renvoie au hasard les valeurs
# -1 ou 1 avec la même probabilité. Avant d’utiliser cette instruction vous mettrez au tout
# début de votre script la ligne import random.

def exo29():
    import random
    nb = 0
    position = 0
    while position != 5:
        position += random.choice([-1, 1])
        nb += 1
    print(nb)

# La suite de Fibonacci est une suite mathématique qui porte le nom de Leonardo Fibonacci,
# un mathématicien italien du XIIIe siècle. Initialement, cette suite a été conçue pour décrire la
# croissance d’une population de lapins, mais elle peut également être utilisée pour décrire
# certains motifs géométriques retrouvés dans la nature (coquillages, fleurs de tournesol. . . ).
# Pour la suite de Fibonacci (xn), le terme au rang n (avec n > 1) est la somme des nombres
# aux rangs n−1 et n−2 : xn = xn−1 +xn−2
# Par définition, les deux premiers termes sont x0 = 0 et x1 = 1.
# À titre d’exemple, les 10 premiers termes de la suite de Fibonacci sont donc 0, 1, 1, 2, 3, 5, 8,
# 13, 21 et 34.
# Créez un script qui construit une liste fibo avec les 15 premiers termes de la suite de
# Fibonacci puis l’affiche.
# Améliorez ce script en affichant, pour chaque élément de la liste fibo avec n > 1, le rapport
# entre l’élément de rang n et l’élément de rang n−1. Ce rapport tend-il vers une constante ? Si
# oui, laquelle ?

def exo30():
    fibo = [0, 1]
    for i in range(2, 15):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    print(fibo)
    for i in range(2, 15):
        print(fibo[i] / fibo[i - 1])

# Affichez sur la même ligne les nombres de 10 à 20 (inclus) ainsi que leur racine carrée avec 3
# décimales. Utilisez pour cela le module math avec la fonction sqrt(). Exemple :
# 1 10 3.162
# 2 11 3.317
# 3 12 3.464
# 4 13 3.606
# 5 [...]

def exo31():
    for i in range(10, 21):
        print(i, round(math.sqrt(i), 3))

# Calculez le cosinus de π/2 en utilisant le module math avec la fonction cos() et la constante
# pi.
def exo32():
    print(math.cos(math.pi / 2))

# Affichez le nom et le contenu du répertoire courant (celui depuis lequel vous avez lancé
# l’interpréteur Python).
# Déterminez également le nombre total de fichiers et de répertoires présents dans le
# répertoire courant.

def exo33():
    path = os.getcwd()
    print("Le répertoire courant est : " + path)

    listeFichiers = os.listdir()
    print("Le contenu du répertoire courant est : " + str(listeFichiers))

    lenFichiers = len(os.listdir())
    print("Le nombre total de fichiers et de répertoires est : " + str(lenFichiers))

# Défi n° 34 : Affichage temporisé
# Affichez les nombres de 1 à 10 avec 1 seconde d’intervalle. Utilisez pour cela le module time
# et sa fonction sleep().

def exo34():
    for i in range(1, 11):
            print(i)
            time.sleep(1)


# Défi n° 35 : Séquences aléatoires de chiffres
# Générez une séquence aléatoire de 6 chiffres, ceux-ci étant des entiers tirés entre 1 et 4.
# Utilisez le module random avec la fonction randint().

def exo35():
    for i in range(6):
        print(random.randint(1, 4), end="")

# Défi n° 36 : Puissance
# Créez une fonction calc_puissance(x, y) qui renvoie 𝑥 en utilisant l’opérateur **. 𝑦
# 1| >>> 2**2
# 2| 4
# 3| >>> 2**3
# 4| 8
# Dans le programme principal, calculez et affichez à l’écran 2 avec i variant de 0 à 20 inclus. 𝑖
# On souhaite que le résultat soit présenté avec le formatage suivant :
# 1| 2^ 0 = 1
# 2| 2^ 1 = 2
# 3| 2^ 2 = 4
# 4| [...]
# 5| 2^20 = 1048576


def calc_puissance(x, y):
    return x ** y

def exo36():
    for i in range(21):
        resultat = calc_puissance(2, i)
        print(f"2^{i} = {resultat}")

# Défi n° 37 : Nombres premiers
# Reprenez l’exercice sur les nombres premiers.
# Créez une fonction est_premier() qui prend comme argument un nombre entier positif n
# (supérieur à 2) et qui renvoie le booléen True si n est premier et False si n n’est pas premier.
# Déterminez tous les nombres premiers de 2 à 100. On souhaite avoir une sortie similaire à
# celle-ci :
# 1| 2 est premier
# 2| 3 est premier
# 3| 4 n' est pas premier
# 4| [...]
# 5| 100 n' est pas premier

def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Défi n° 38 : Distance 3D
# Créez une fonction calc_distance_3D() qui calcule la distance euclidienne en trois
# dimensions entre deux points de l’espace.
# Testez votre fonction sur les 2 points A(0,0,0) et B(1,1,1). Trouvez-vous bien √3 ?
# On rappelle que la distance euclidienne d entre deux points A et B de coordonnées
# cartésiennes respectives (xA, yA,zA) et (xB, yB,zB) se calcule comme suit :
# d = sqrt( (xB −xA)² + (yB −yA)² + (zB −zA)² )

def calc_distance_3D(xA, yA, zA, xB, yB, zB):
    return math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2 + (zB - zA) ** 2)


# Défi n° 39 : Distribution et statistiques
# 1. Créez une fonction gen_distrib() qui prend comme argument trois entiers : debut, fin
# et n. La fonction renverra une liste de n floats aléatoires entre debut et fin. Pour
# générer un nombre aléatoire dans un intervalle donné, utilisez la fonction uniform()
# du module random dont voici quelques exemple d’utilisation :
# 1| >>> import random
# 2| >>> random . uniform (1 , 10)
# 3| 8.199672607202174
# 4| >>> random . uniform (1 , 10)
# 5| 2.607528561528022
# 2. Créez une autre fonction calc_stat() qui prend en argument une liste de floats et qui
# renvoie une liste de trois éléments contenant respectivement le minimum, le
# maximum et la moyenne de la liste. La moyenne pourra être calculée avec les
# fonctions sum() et len(). Vous pouvez reprendre le code du défi 18.
# 3. Dans le programme principal, générez 20 listes aléatoires de 100 floats compris entre
# 0 et 100 et affichez le minimum (min()), le maximum (max()) et la moyenne pour
# chacune d’entre elles.
# 4. Pour chacune des 20 listes, affichez les statistiques (min, max, et moyenne) avec
# deux chiffres après la virgule :
# 10
# 1| Liste 1 : min = 0.17 ; max = 99.72 ; moyenne = 57.38
# 2| Liste 2 : min = 1.25 ; max = 99.99 ; moyenne = 47.41
# 3| [...]
# 4| Liste 19 : min = 1.05 ; max = 99.36 ; moyenne = 49.43
# 5| Liste 20 : min = 1.33 ; max = 97.63 ; moyenne = 46.53
# 5. Les écarts sur les statistiques entre les différentes listes sont-ils importants ?
# Relancez votre script avec des listes de 1000 éléments, puis 10 000 éléments. Les
# écarts changent-ils quand le nombre d’éléments par liste augmente ?

import random

def gen_distrib(debut, fin, n):
    return [random.uniform(debut, fin) for i in range(n)]

def calc_stat(liste):
    return [min(liste), max(liste), sum(liste)/len(liste)]

def exo39():
    for i in range(20):
        liste = gen_distrib(0, 100, 100)
        stat = calc_stat(liste)
        print(f"Liste {i+1}: min = {stat[0]:.2f} ; max = {stat[1]:.2f} ; moyenne = {stat[2]:.2f}")


# Défi n° 40 : Prédire la sortie
# Prédisez le comportement des quatre codes suivants

def exo40():
    print("NameError: name 'x' is not defined")
    print("Bonjour Patrick 10")
    print("Bonjour Patrick 10 10")
    print("Bonjour Patrick 42 10 ")

#Défi n° 41 : Passage de liste à une fonction
# Créez une fonction ajoute_nb_alea() qui prend en argument une liste et qui ajoute un
# nombre entier aléatoire entre -10 et 10 (inclus) à chaque élément. La fonction affichera à
# l’écran cette nouvelle liste modifiée.
# Dans le programme principal, on effectuera les actions suivantes :
# 1. Créez une variable ma_liste = [7, 3, 8, 4, 5, 1, 9, 10, 2, 6].
# 2. Affichez ma_liste à l’écran.
# 3. Appelez la fonction ajoute_nb_alea() en lui passant ma_liste en argument.
# 4. Affichez à nouveau ma_liste à l’écran. Comment expliquez-vous le résultat obtenu ?

def ajoute_nb_alea(liste):
    for i in range(len(liste)):
        liste[i] += random.randint(-10, 10)
    print(liste)

def exo41():
    ma_liste = [7, 3, 8, 4, 5, 1, 9, 10, 2, 6]
    print(ma_liste)
    ajoute_nb_alea(ma_liste)
    print(ma_liste)

# Soit la liste ['girafe', 'tigre', 'singe', 'souris']. Avec une boucle, affichez chaque élément ainsi
# que sa taille (nombre de caractères).

def exo42():
    liste = ['girafe', 'tigre', 'singe', 'souris']
    for i in liste:
        print(i, len(i))

# Un palindrome est un mot ou une phrase dont l’ordre des lettres reste le même si on le lit de
# gauche à droite ou de droite à gauche. Par exemple, « ressasser » est un palindrome.
# 1. Créez la fonction test_palindrome() qui prend en argument une chaîne de caractères
# et qui affiche xxx est un palindrome si la chaîne de caractères xxx passée en
# argument est un palindrome ou xxx n'est pas un palindrome sinon. Pensez à vous
# débarrasser au préalable des majuscules et des espaces.
# 2. Testez ensuite si les expressions suivantes sont des palindromes :
# a. radar
# b. never odd or even
# c. karine alla en Irak
# d. engage le jeu que je le gagne
# e. un roc si biscornu
# f. ce cours est trop cool

def test_palindrome(chaine):
    chaine = chaine.lower().replace(" ", "")
    if chaine == chaine[::-1]:
        print(f"{chaine} est un palindrome")
    else:
        print(f"{chaine} n'est pas un palindrome")

def exo43():
    test_palindrome("radar")
    test_palindrome("never odd or even")
    test_palindrome("karine alla en Irak")
    test_palindrome("engage le jeu que je le gagne")
    test_palindrome("un roc si biscornu")
    test_palindrome("ce cours est trop cool")

# Défi n° 44 : Mot composable
# Un mot est composable à partir d’une séquence de lettres si la séquence contient toutes les
# lettres du mot. Chaque lettre de la séquence ne peut être utilisée qu’une seule fois. Par
# exemple, « coucou » est composable à partir de « uocuoceokzefhu ».
# 1. Écrivez la fonction test_composable() qui prend en argument un mot (sous la forme
# d’une chaîne de caractères) et une séquence de lettres (aussi comme une chaîne de
# caractères) et qui affiche “Le mot xxx est composable à partir de yyy” si le mot (xxx)
# est composable à partir de la séquence de lettres (yyy) ou “Le mot xxx n'est pas
# composable à partir de yyy” sinon.
# 2. Testez cette fonction avec les mots et les séquences suivantes :
# Mot Séquence
# python aophrtkny
# python aeiouyhpq
# coucou uocuoceokzezh
# fonction nhwfnitvkloco

def test_composable(mot, sequence):
    for i in mot:
        if i not in sequence:
            print(f"Le mot {mot} n'est pas composable à partir de {sequence}")
            return
    print(f"Le mot {mot} est composable à partir de {sequence}")


def exo44():
    test_composable("python", "aophrtkny")
    test_composable("python", "aeiouyhpq")
    test_composable("coucou", "uocuoceokzezh")
    test_composable("fonction", "nhwfnitvkloco")

# Défi n° 45 : Alphabet et pangramme
# Les codes ASCII des lettres minuscules de l’alphabet vont de 97 (lettre « a ») à 122 (lettre « z
# »). La fonction chr() prend en argument un code ASCII sous la forme d’un entier et renvoie le
# caractère correspondant (sous la forme d’une chaîne de caractères). Ainsi chr(97) renvoie 'a',
# chr(98) renvoie 'b' et ainsi de suite.
# 1. Créez la fonction get_alphabet() qui utilise une boucle et la fonction chr() et qui
# renvoie une chaîne de caractères contenant toutes les lettres de l’alphabet.
# 2. Un pangramme est une phrase comportant au moins une fois chaque lettre de
# l’alphabet. Créez la fonction pangramme() qui utilise la fonction get_alphabet()
# précédente, qui prend en argument une chaîne de caractères (xxx) et qui renvoie xxx
# est un pangramme si cette chaîne de caractères est un pangramme ou xxx n'est pas
# un pangramme sinon. Pensez à vous débarrasser des majuscules le cas échéant.
# 3. Testez ensuite si les expressions suivantes sont des pangrammes :
# a. Portez ce vieux whisky au juge blond qui fume.
# b. Monsieur Jack vous dactylographiez bien mieux que votre ami Wolf.
# c. Buvez de ce whisky que le patron juge fameux.

def get_alphabet():
    alphabet = ""
    for i in range(97, 123):
        alphabet += chr(i)
    return alphabet

def pangramme(s):
    alphabet = get_alphabet()
    s_lower = s.lower()
    for lettre in alphabet:
        if lettre not in s_lower:
            return f"{s} n'est pas un pangramme"
    return f"{s} est un pangramme"


def exo45():
    print(pangramme("Portez ce vieux whisky au juge blond qui fume."))
    print(pangramme("Monsieur Jack vous dactylographiez bien mieux que votre ami Wolf."))
    print(pangramme("Buvez de ce whisky que le patron juge fameux."))


# Défi n° 46 : Mots de 2 et 3 lettres dans une séquence d’ADN
# 1. Créez une fonction compte_mots_2_lettres() qui prend comme argument une
# séquence sous la forme d’une chaîne de caractères et qui renvoie tous les mots de 2
# lettres qui existent dans la séquence sous la forme d’un dictionnaire. Par exemple
# pour la séquence ACCTAGCCCTA, le dictionnaire renvoyée serait : {'AC': 1, 'CC': 3, 'CT':
# 2, 'TA': 2, 'AG': 1, 'GC': 1}
# 2. Créez une nouvelle fonction compte_mots_3_lettres() qui a un comportement
# similaire à compte_mots_2_lettres() mais avec des mots de 3 lettres.
# 3. Utilisez ces fonctions pour affichez les mots de 2 et 3 lettres et leurs occurrences
# trouvés dans la séquence d’ADN :
# ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG
# Voici un exemple de sortie attendue :
# 1| Mots de 2 lettres
# 2| AC : 1
# 3| CC : 3
# 4| CT : 8
# 5| [...]
# 6| Mots de 3 lettres
# 7| ACC : 1
# 8| CCT : 2
# 9| CTA : 5
# 10| [...]

def compte_mots_2_lettres(sequence):
    dico = {}
    for i in range(len(sequence) - 1):
        mot = sequence[i:i + 2]
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    return dico
def compte_mots_3_lettres(sequence):
    dico = {}
    for i in range(len(sequence) - 2):
        mot = sequence[i:i + 3]
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    return dico

def exo46():
    print(compte_mots_2_lettres("ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG"))
    print(compte_mots_3_lettres("ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG"))


# Défi n° 47 : Admis ou recalé
# 1. Créez un fichier notes.txt contenant les notes obtenues par des étudiants pour le
# cours de Python. Chaque ligne du fichier ne contient qu’une note. Enregistrez-le dans
# votre répertoire de travail.
# 2. Créez un script Python qui lit chaque ligne de ce fichier, extrait les notes sous forme
# de float et les stocke dans une liste. Le script réécrit ensuite les notes dans un fichier
# notes2.txt avec une note par ligne suivie de « recalé » si la note est inférieure à 10 et
# « admis » si la note est supérieure ou égale à 10. Toutes les notes seront écrites avec
# une décimale. À titre d’exemple, voici les 3 premières lignes attendues pour le fichier
# notes2.txt :
# 1| 13.5 admis
# 2| 17.0 admis
# 3| 9.5 recalé
# 3. Terminez le script en calculant et affichant la moyenne des notes avec deux
# décimales.

def exo47():
    with open('notes.txt', 'r') as f:
        notes = [float(line.strip()) for line in f]

    with open('notes2.txt', 'w') as f:
        for note in notes:
            if note >= 10:
                f.write(f"{note:.1f} admis\n")
            else:
                f.write(f"{note:.1f} recalé\n")

    moyenne = sum(notes) / len(notes)
    print(f"Moyenne : {moyenne:.2f}")


# Défi n° 49 : Classe Rectangle
# 1. Créez un script incluant une classe Rectangle ainsi qu’un programme principal qui :
# a. crée une instance rectangle de la classe Rectangle ;
# b. affiche les attributs d’instance largeur, longueur et couleur ;
# c. calcule et affiche la surface de rectangle ;
# d. affiche une ligne vide ;
# e. change le rectangle en carré de 30 m de côté ;
# f. calcule et affiche la surface de ce carré ;
# g. crée une autre instance rectangle2 aux dimensions et à la couleur que vous
# souhaitez (soyez créatif !) et qui affiche les attributs et la surface de ce
# nouveau rectangle.
# 2. Entraînez-vous avec la classe Rectangle. Créez la méthode calcule_perimetre() qui
# calcule le périmètre d’un objet rectangle. Testez sur un exemple simple (largeur = 10
# m, longueur = 20 m).

def exo49():
    class Rectangle:
        def __init__(self, largeur, longueur, couleur):
            self.largeur = largeur
            self.longueur = longueur
            self.couleur = couleur

        def calcule_surface(self):
            return self.largeur * self.longueur

        def calcule_perimetre(self):
            return 2 * (self.largeur + self.longueur)

        def __str__(self):
            return f"Rectangle de {self.largeur} m de largeur, {self.longueur} m de longueur et de couleur {self.couleur}"

    rectangle = Rectangle(10, 20, "bleu")

    print(rectangle)
    print(f"Surface : {rectangle.calcule_surface()} m²")
    print(f"Périmètre : {rectangle.calcule_perimetre()} m")


# Défi n° 50 : Classe Atome
# 1. Créez une nouvelle classe Atome avec les attributs x, y, z (qui contiennent les
# coordonnées atomiques) et la méthode calcul_distance() qui calcule la distance entre
# deux atomes. Testez cette classe sur plusieurs exemples.
# 2. Améliorez la classe Atome en lui ajoutant un nouvel attribut masse qui correspond à
# la masse atomique ainsi qu’une nouvelle méthode .calcule_centre_masse().
# Redéfinissez le comportement avec print() (à l’aide de la méthode magique
# .__str__()) de manière à afficher les coordonnées et la masse de l’atome.


def exo50():
    class Atome:
        def __init__(self, x, y, z, masse):
            self.x = x
            self.y = y
            self.z = z
            self.masse = masse

        def calcul_distance(self, autre_atome):
            dx = self.x - autre_atome.x
            dy = self.y - autre_atome.y
            dz = self.z - autre_atome.z
            return (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5

        def calcule_centre_masse(self, autre_atome):
            total_masse = self.masse + autre_atome.masse
            xmoy = (self.x * self.masse + autre_atome.x * autre_atome.masse) / total_masse
            ymoy = (self.y * self.masse + autre_atome.y * autre_atome.masse) / total_masse
            zmoy = (self.z * self.masse + autre_atome.z * autre_atome.masse) / total_masse
            return Atome(xmoy, ymoy, zmoy, total_masse)
        def __str__(self):
            return f"Atome de masse {self.masse} au point ({self.x}, {self.y}, {self.z})"


    a1 = Atome(0, 0, 0, 12)
    a2 = Atome(1, 1, 1, 16)

    print(a1)  # Atome(0, 0, 0, 12)
    print(a2)  # Atome(1, 1, 1, 16)

    distance = a1.calcul_distance(a2)
    print(distance)

    cm = a1.calcule_centre_masse(a2)
    print(cm)
