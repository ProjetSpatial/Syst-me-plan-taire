# Formation d'un système planétaire

## Introduction
Dans le cadre de l'ARE DYNAMIC, nous sommes conduits à mener un projet de modélisation sur un sujet que nous avons choisi. Le nôtre se porte sur la formation d'un système planétaire constitué d'une seule étoile en débutant la modélisation une fois les platénétisimaux créés.

## Formation des planètes

Après l'implosion d'une nébuleuse, suit la formation d'une étoile. Celle ci est entourrée d'un disque d'accrétion consituté de roches silicates et de nombreuses poussières. Tout celà va ensuite, par accrétion, former des planétésimaux.

La formation de planète à partir des planétésimaux dure environ 100 000 ans et a fait l'objet de simulations numériques qui en donnent l'image suivante :

1.	au départ, des collisions aléatoires au sein d'un ensemble de milliards de planétésimaux engendrent la croissance de certains aux dépens des autres

2.	dès qu'un planétésimal a gagné une masse largement supérieure à la masse moyenne des planétésimaux voisins, il peut engloutir tout ce qui se trouve dans sa zone d'influence gravitationnelle

3.	une fois le vide fait autour de lui, sa croissance s'arrête faute de matériau : on a alors affaire à un cœur planétaire.

## Aspects techniques

Notre modélisation va se baser sur 4 paramètres:

-Le rayon de l'étoile

-La densité de l'étoile

-Le nombre de planétessimaux (ou quantité de matière dont l'on dispose pour la formation des planètes)

-Un curseur temps. Cela nous permetra d'itérer nos algorithmes sur plusieurs dizaines de millions d'années. 

Le rayon et la densité nous permettront d'obtenir la masse de l'étoile ce qui influera sur la vitesse des planétessimaux ainsi que leur distance à l'étoile.
Ainsi on pourra observer de nombreux cas comme la formation d'une unique planète géante ou de nombreuses petites planètes ou encore un début de formation de système planétère sans pour autant le voir aboutir en fonction du temps sélectionné.

Schema de l'idée initiale: interface
<a href="http://zupimages.net/viewer.php?id=19/13/jrzz.png"><img src="https://zupimages.net/up/19/13/jrzz.png" alt="" /></a>


- agents:
Planetesimaux, Etoile, Planete
Properties(micro): Position (cercle autour de etoile), 
Densité (du soleil), 
Masse (Rayon/taille), 
Vitesse

- dimension temporelle : Million d'années

- propriétés observables (macro):
Collision et creation de planètes.


modélisation de la taille du disque post-accrétion
<a href="http://zupimages.net/viewer.php?id=19/13/rb7j.png"><img src="https://zupimages.net/up/19/13/rb7j.png" alt="" /></a>

## Formulaire
