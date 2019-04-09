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
for
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


## Modélisation

Modéliser les collisions grâce à Pygame. Notre modélisation finale est visible dans la partie "Abstract".
<a href="http://zupimages.net/viewer.php?id=19/15/b618.gif"><img src="https://zupimages.net/up/19/15/b618.gif" alt="" /></a>

## Abstract

Our purpose in this project was to be able to model the creation of a planetary system by using probabilities in programing. We agreed that our planetary system would contain only one star (it would have been too hard to code a planetary system with several stars because the number of criterias would drastically increase and we would need much more time). We therefore started by coding the main components of our planetary system, the planetesimals. The planetesimals are rocks, bigger than asteroids, coliding with each other. These collisions will create planet's hearts which will later on form planets. At this point, the purpose was to have spheres placed at different positions around the star and everytime we would run the program, the sphere's positions would change. Here you can see an example of what we had:
<a href="http://zupimages.net/viewer.php?id=19/15/14j3.png"><img src="https://zupimages.net/up/19/15/14j3.png" alt="" /></a>

We then began coding our star. We wanted the density, the diameter and the star's mass to be variables that we can change. Later on we also put a mass for the planetesimals that can also be changed. Once we had all the components, we started coding the collisions between the planetesimals and therefore, also their mouvement thanks to Pygame, which is a program that unables the possibility to create animations. We had several issues with that part. At first, the program would stop after one collision, then it would go on after the first collision but it wouldn't make any more. After finally solving the problems, we now have a forming planetary system. We can clearaly see the collisions between the planetesimals that grow everytime. Here you can see a screenshot of our final model of a planetary system:
<a href="http://zupimages.net/viewer.php?id=19/15/gf47.png"><img src="https://zupimages.net/up/19/15/gf47.png" alt="" /></a>


