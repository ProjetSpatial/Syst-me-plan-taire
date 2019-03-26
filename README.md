# Formation d'un système planétaire

## Introduction
Dans le cadre de l'ARE DYNAMIC, nous sommes conduits à mener un projet de modélisation sur un sujet que nous avons choisi. Le nôtre se porte sur la formation d'un système planétaire constitué d'une seule étoile en débutant la modélisation une fois les platénétisimaux créés.

## Formation des planètes

Après l'implosion d'une nébuleuse, suit la formation d'une étoile. Celle-ci est entourrée d'un disque d'accrétion consituté de roches silicates et de nombreuses poussières. Tout celà va ensuite, par accrétion, former des planétésimaux.

La formation de planètes à partir des planétésimaux dure environ 100 000 ans et a fait l'objet de simulations numériques qui en donnent l'image suivante :

1.	au départ, des collisions aléatoires au sein d'un ensemble de milliards de planétésimaux engendrent la croissance de certains aux dépends des autres

2.	dès qu'un planétésimal a gagné une masse largement supérieure à la masse moyenne des planétésimaux voisins, il peut engloutir tout ce qui se trouve dans sa zone d'influence gravitationnelle

3.	une fois le vide fait autour de lui, sa croissance s'arrête faute de matériaux : on a alors à faire à un cœur planétaire.

Dans un soucis de simplification, nous modélisons la collision de planétésimaux sans prendre en compe leur rayon. La collision se produit lorsque les centre de 2 planétismaux sont à une distance inférieur à une valeur R déterminée.

## Aspects techniques

Notre modélisation va se baser sur 4 paramètres:

-Le rayon de l'étoile

-La densité de l'étoile

-Le nombre de planétesimaux (ou quantité de matière dont l'on dispose pour la formation des planètes)

-Un curseur temps. Cela nous permettra d'itérer nos algorithmes sur plusieurs dizaines de millions d'années. 

Le rayon et la densité nous permettrons d'obtenir la masse de l'étoile ce qui influera sur la vitesse des planétessimaux ainsi que leur distance à l'étoile.
Ainsi on pourra observer de nombreux cas comme la formation d'une unique planète géante ou de nombreuses petites planètes ou encore un début de formation de système planétaire sans pour autant le voir aboutir en fonction du temps sélectionné.

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

Notre but est, non seulement, de faire marcher les programmes sur les diverses probabilités, mais aussi de réussir à mettre en mouvement notre système solaire et faire donc appliquer nos formules à un mouvement réel grâce à l'application Pygame. Le but est que l'on puisse voir la formation des planètes par les collisions des planétésimaux en temps accéléré. 
