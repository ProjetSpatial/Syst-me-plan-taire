# Formation d'un système planétaire
## Introduction
Dans le cadre de l'ARE DYNAMIC, nous sommes conduits à mener un projet de modélisation sur un sujet que nous avons choisi. Le nôtre se porte sur la formation d'un système planétaire en débutant la modélisation une fois les platénétisimaux créés.

# Systeme-planetaire

qte de planetesimaux + taille = densite

Formation des cœurs planétaires

La formation de planète à partir des planétésimaux dure environ 100 000 ans et a fait l'objet de simulations numériques qui en donnent l'image suivante :
1.	au départ, des collisions aléatoires au sein d'un ensemble de milliards de planétésimaux engendrent la croissance de certains aux dépens des autres ;
2.	dès qu'un planétésimal a gagné une masse largement supérieure à la masse moyenne des planétésimaux voisins, il peut engloutir tout ce qui se trouve dans sa zone d'influence gravitationnelle ;
3.	une fois le vide fait autour de lui, sa croissance s'arrête faute de matériau : on a alors affaire à un cœur planétaire dont on dit qu'il a atteint sa « masse d'isolation ». À une UA, cette masse d'isolation représente environ le dixième de la masse terrestre et correspond à l'agglomération d'environ un milliard de planétésimaux.

- agents:
Planetesimaux, Etoile, Planete
Properties(micro): Position (cercle autour de etoile), 
Densité (du soleil), 
Masse (Rayon/taille), 
Vitesse

- temporal dimension: Million d'années

- observable propreties(macro):
Collision et creation de planete

https://raw.githubusercontent.com/ProjetSpatial/Systeme-planetaire/master/modelisation.png

https://raw.githubusercontent.com/ProjetSpatial/Systeme-planetaire/master/ideedebase.png

Commandes github

git clone (lien) -> permet de récupérer les fichiers en local depuis le dépot.

ls -> Permet de voir les fichiers

cd systeme-planetaire (ou autre nom de fichier) -> permet d'entrer dans dans un dossier

ls -> Permet de voir les fichiers dans le dossier précédemment pénétré

pwd -> Permet de localiser le dossier où l'on est

git status -> Permet de suivre les modifications au sein d'un dossier

git diff -> Permet de voir les modifications au sein d'un fichier du dossier

git add "nom du fichier"-> Permet de confirmer les modifications apportées dans le fichier modifié

git commit -m "message" -> Permet d'envoyer le fichier dans le dépot

git config --global user.email "you@example.com" -> identification

git config --global user.name "Your Name" -> identification

git log -> identification 

git commit origin master -> Permet d'enregistrer le fichier dans le dépot.

L'ordre est le suivabt : clone -> add -> commit -m "nom" -> commit origin master

