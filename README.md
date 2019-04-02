# Formation d'un système planétaire

## Introduction
Dans le cadre de l'ARE DYNAMIC, nous sommes conduits à mener un projet de modélisation sur un sujet que nous avons choisi. Le nôtre se porte sur la formation d'un système planétaire constitué d'une seule étoile en débutant la modélisation une fois les platénétisimaux créés.

## Formation des planètes

Implosion d'une nébuleuse-> formation d'une étoile (elle est entourrée d'un disque d'accrétion consituté de roches silicates et de nombreuses poussières)

A partir de là, notre système planétaire peut commencer à se former:

1.	au départ, des collisions aléatoires au sein d'un ensemble de milliards de planétésimaux engendrent la croissance de certains aux dépends des autres

2.	dès qu'un planétésimal a gagné une masse largement supérieure à la masse moyenne des planétésimaux voisins, il peut engloutir tout ce qui se trouve dans sa zone d'influence gravitationnelle

3.	une fois le vide fait autour de lui, sa croissance s'arrête faute de matériaux : on a alors à faire à un cœur planétaire.


## Aspects techniques

Notre modélisation sur 4 paramètres:

-Le rayon de l'étoile

-La densité de l'étoile

-Le nombre de planétesimaux (ou quantité de matière dont l'on dispose pour la formation des planètes)

-Un curseur temps. Cela nous permettra d'itérer nos algorithmes sur plusieurs dizaines de millions d'années. 

Schéma de l'idée initiale: interface
<a href="http://zupimages.net/viewer.php?id=19/13/jrzz.png"><img src="https://zupimages.net/up/19/13/jrzz.png" alt="" /></a>


- agents:
Planetesimaux, Etoile, Planete
Properties(micro): Position (cercle autour de etoile), 
Densité (du soleil), 
Masse (Rayon/taille), 
Vitesse

- dimension temporelle : Millions d'années

- propriétés observables (macro):
Collisions et creations de planètes.


modélisation de la taille du disque post-accrétion
<a href="http://zupimages.net/viewer.php?id=19/13/rb7j.png"><img src="https://zupimages.net/up/19/13/rb7j.png" alt="" /></a>

## Formulaire


# Modélisation

Modéliser les collisions grâce à Pygame.
