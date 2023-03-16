# Défi n° 48 : Spirale
# Créez un script spirale.py qui calcule les coordonnées cartésiennes d’une spirale à deux
# dimensions.
# Les coordonnées cartésiennes xA et yA d’un point A sur un cercle de rayon r s’expriment en
# fonction de l’angle θ comme :
# xA = cos(θ) × r et yA = sin(θ) × r
# Pour calculer les coordonnées cartésiennes qui décrivent la spirale, vous allez faire varier
# deux variables en même temps :
# — l’angle θ, qui va prendre des valeurs de 0 à 4π radians par pas de 0.1, ce qui correspond à
# deux tours complets ;
# — le rayon du cercle r, qui va prendre comme valeur initiale 0.5 puis que vous allez
# incrémenter (c’est-à-dire augmenter) pas par pas de 0.1.
# Les fonctions trigonométriques sinus et cosinus sont disponibles dans le module math. Pour
# les utiliser, vous ajouterez au début de votre script l’instruction : import math.
# La fonction sinus sera math.sin() et la fonction cosinus math.cos(). Ces deux fonctions
# prennent comme argument une valeur d’angle en radian. La constante mathématique π sera
# également accessible grâce à ce module via math.pi. Par exemple :
# 1| >>> math . sin (0)
# 2| 0.0
# 3| >>> math . sin ( math . pi /2)
# 4| 1.0
# 5| >>> math . cos ( math . pi )
# 6| -1.0
# Sauvegardez ensuite les coordonnées cartésiennes dans le fichier spirale.txt en respectant le
# format suivant :
# — un couple de coordonnées (xA et yA) par ligne ;
# — au moins un espace entre les deux coordonnées xA et yA ;
# — les coordonnées affichées avec 5 chiffres après la virgule.
# Les premières lignes de spirale.txt devrait ressembler à :
# 0.50000 0.00000
# 0.59700 0.05990
# 0.68605 0.13907
# 0.76427 0.23642
# 0.82895 0.35048
# 0.87758 0.47943
# [...] [...]

# Path: spirale.py
import math

# Fonction qui calcule les coordonnées cartésiennes d'un point sur une spirale
def coord_spirale(angle, rayon):
    x = math.cos(angle) * rayon
    y = math.sin(angle) * rayon
    return x, y

# Définition des paramètres de la spirale
angle_debut = 0
angle_fin = 4 * math.pi
pas_angle = 0.1
rayon_debut = 0.5
pas_rayon = 0.1

# Initialisation de la liste des coordonnées
coordonnees = []

# Boucle de calcul des coordonnées
rayon = rayon_debut
while rayon <= 2.5:
    angle = angle_debut
    while angle <= angle_fin:
        x, y = coord_spirale(angle, rayon)
        coordonnees.append((x, y))
        angle += pas_angle
    rayon += pas_rayon

# Ecriture des coordonnées dans le fichier spirale.txt
with open("spirale.txt", "w") as fichier:
    for x, y in coordonnees:
        fichier.write("{:.5f} {:.5f}\n".format(x, y))

# Calcul et affichage de la moyenne des rayons
moyenne_rayon = sum(r for r in range(5, 26)) / 21
print("Moyenne des rayons : {:.2f}".format(moyenne_rayon))


# Explications :
#
# La fonction coord_spirale(angle, rayon) prend en argument l'angle et le rayon du point à calculer
# sur la spirale, et renvoie les coordonnées cartésiennes (x, y) correspondantes.

# Les variables angle_debut, angle_fin et pas_angle définissent la plage
# et le pas d'angle pour les calculs. De même, rayon_debut, pas_rayon et
# la condition d'arrêt de la boucle while définissent la plage et le pas de rayon.

# Les coordonnées calculées sont stockées dans une liste coordonnees sous forme de tuples (x, y).
# Les coordonnées sont ensuite écrites dans le fichier "spirale.txt" en utilisant la méthode write()
# des objets fichiers. Le formatage est assuré avec la méthode format() et la spécification
# de précision ".5f" pour afficher 5 chiffres après la virgule.

# Enfin, la moyenne des rayons est calculée en utilisant la fonction sum() et la notation
# de compréhension de liste [r for r in range(5, 26)], qui renvoie la liste [5, 6, 7, ..., 24, 25].
# Le résultat est affiché avec la méthode format() pour n'afficher que 2 chiffres après la virgule.