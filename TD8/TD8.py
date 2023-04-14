import numpy as np
import matplotlib.pyplot as plt


# EXERCICE 1 : Paramétriser des axes
# 1. Tracer la fonction exponentielle entre 0 et 6 à partir de 30 points reliés.
# 2. Ajouter une légende affichant ‘exp(x)’.
# 3. Paramétriser l’axe des abscisses entre -1 et 7, puis l’axe des ordonnées entre -10 et
# 450.
# 4. Ajouter un titre au graphique.
# 5. Ajouter des labels aux deux axes.
# 6. Ajouter un texte en (3, 200) avec une orientation de 45°.

def exo1():
    x = np.linspace(0, 6, 30)
    y = np.exp(x)
    plt.plot(x, y, label='exp(x)')
    plt.legend()
    plt.title('Exponentielle')
    plt.xlabel('x')
    plt.ylabel('exp(x)')
    plt.text(3, 200, 'exp(x)', rotation=45)
    plt.axis([-1, 7, -10, 450])
    plt.show()

# EXERCICE 2 : Tracé de formes géométriques
# 1. Tracer un carré à l’aide de deux listes de 0 et de 1 et de plot.
# 2. Théoriquement, le carré apparaît rectangle. Formater les axes afin d’afficher un carré
# propre.
# 3. Limiter les axes entre -1 et 2

def exo2():
    x = [0, 0, 1, 1, 0]
    y = [0, 1, 1, 0, 0]
    plt.plot(x, y)
    plt.axis('equal')
    plt.axis([-1, 2, -1, 2])
    plt.show()

# EXERCICE 3 : Tracé d’un cercle
# Trouver un moyen de tracer un cercle parfait (non ovale) entre -1, 5 et 1, 5 sur les deux axes.

def exo3():
    x = np.linspace(-1.5, 1.5, 100)
    y = np.sqrt(1 - x ** 2)
    plt.plot(x, y)
    plt.plot(x, -y)
    plt.axis('equal')
    plt.show()


# EXERCICE 4 : Affichage de plusieurs tracés dans la même figure
# Soient les fonction f et g telles que f(t) = exp(-t) *cos(2*pi*t) et g(t) = cos(2*pi*t).
# Créer un visualisation de 4 graphiques dans une unique fenêtre afin de visualiser ces deux
# fonctions entre 0 et 6, chacune avec un pas de 0,5 et avec un pas de 0,1.

def exo4():
    t = np.linspace(0, 6, 100)
    f = np.exp(-t) * np.cos(2 * np.pi * t)
    g = np.cos(2 * np.pi * t)
    plt.subplot(2, 2, 1)
    plt.plot(t, f)
    plt.subplot(2, 2, 2)
    plt.plot(t, f)
    plt.subplot(2, 2, 3)
    plt.plot(t, g)
    plt.subplot(2, 2, 4)
    plt.plot(t, g)
    plt.show()


# EXERCICE 5 : Animation avec Matplotlib
# Réaliser une animation avec effacement (sans le module animation) permettant de visualiser
# la fonction f(x) = cos(2*pi*x) en jouant avec le nombre de points du linspace 5, puis 50 puis
# 500 (utiliser une boucle et les méthodes .set_data et .pause)

def exo5():
    x = np.linspace(0, 1, 5)
    y = np.cos(2 * np.pi * x)
    plt.plot(x, y, 'ro')
    plt.show()
    for i in range(1, 500):
        x = np.linspace(0, 1, i)
        y = np.cos(2 * np.pi * x)
        plt.plot(x, y, 'ro')
        plt.pause(0.01)
        plt.clf()


exo5()