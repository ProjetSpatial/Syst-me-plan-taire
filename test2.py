# -*- coding: utf-8 -*
import random
import math
from tkinter import *
import pygame
from pygame.locals import *

def one_simal_taille():
	taille=0
	taille = random.randint(1,3)
	return taille

def one_simal_pos_init(ray_min, ray_max):
	x = random.randint(1, 1000) * random.choice([-1, 1]) #position sur l axe x
	y = random.randint(1, 1000) * random.choice([-1, 1]) #position sur l axe y
	
	while math.sqrt(x*x + y*y) > ray_max or math.sqrt(x*x + y*y) < ray_min:
		x = random.randint(1, 1000) * random.choice([-1, 1])
		y = random.randint(1, 1000) * random.choice([-1, 1])
	
	return (x,y)

densite = 3e12 #kg/km^3 densite des planetesimaux

def vitesse_one_simal(taille, pos):

	densite = 3e12 #kg/km^3 densite des planetesimaux

	x, y = pos
	masse = densite*(math.pi/6)*taille*taille*taille #changer a la masse du soleil
	G = 6.67*10**-11
	d = (x*x + y*y)**0.5
	v = (G*masse / d)**0.5 / d
	return v

def simal_angle(pos):
	x, y = pos
	angle = 0
	if x > 0:
		angle = math.atan(y/x)
	elif x < 0:
		angle = math.pi + math.atan(y/x)
	elif x == 0 and y > 0:
		angle = math.pi/2
	elif x == 0 and y < 0:
		angle = 3*math.pi/2
	elif x == 0 and y == 0:
		angle = 0
	return angle

def one_simal_pos_next_time(pre, v, angle_pre):
	x, y = pre
	d = (x*x+y*y)**0.5
	
	angle = angle_pre + v

	x = math.cos(angle) * d
	y = math.sin(angle) * d
	
	return (round(x),round(y))

def position(init, v):
	x, y = init
	angle = simal_angle((x,y))
	list_ = [(x,y)]
	for _ in range(20):
		x, y = one_simal_pos_next_time((x,y), v, angle)
		angle = simal_angle((x,y))
		list_.append((x,y))
	return list_

blue = (0,0,255)
navy = (0, 0, 128)
yellow = (255,255,0)
brown = (139,69,19)
tan = (210,180,140)
gold = (255, 215, 0)
steel = (70,130,180)

def color_simal():
    colors = [brown, tan]
    color = random.choice(colors)
    return color

def all_simal_init(ray_min, ray_max):
	x, y = one_simal_pos_init(ray_min, ray_max)
	taille = one_simal_taille()
	angle_i = simal_angle((x,y))
	v = vitesse_one_simal(taille, (x, y))
    color = color_simal()
	return (x, y, angle_i, v, taille, color)

def n_all_simal_init(n, ray_min, ray_max):
	list_n = list()
	for _ in range(n):
		list_n.append(all_simal_init(ray_min, ray_max))
	return list_n

pygame.init()

fenetre = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Système Planétaire")

ray_star = 70

menu = pygame.image.load("clique.png")
fenetre.blit(menu, (0,0))

bg = pygame.image.load("background.jpg")

n = 100

ray_min = 200
ray_max = 400
r=5

list_n = n_all_simal_init(n, ray_min, ray_max)

pygame.display.flip()
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
			pygame.display.quit()
			pygame.quit()
		if event.type == MOUSEBUTTONDOWN:
			for _ in range(50):
				fenetre.blit(bg, (0,0))
				for i in range(n):
					if list_n[i]:
						x, y, new_angle, v, taille, color = list_n[i]
						
						x, y = one_simal_pos_next_time((x,y), v, new_angle)
						new_angle = simal_angle((x,y))
						
						list_n[i] = (x, y, new_angle, v, taille, color)
					   
						for e in range(n):
							if e != i and list_n[e]:
								x_n, y_n, _, _, taille_n, color_n = list_n[e]

								if abs(x - x_n) <= r and abs(y - y_n) <=r:
									taille_c = taille_n + taille
									x_c = round((x + x_n)/2)
									y_c = round((y + y_n)/2)
									v_c = vitesse_one_simal(taille_c, (x_c, y_c))
                                    color_c = color

									new_angle_c = new_angle = simal_angle((x_n,y_n))

									list_n[i] = (x_c, y_c, new_angle_c, v_c, taille_c, color_c)
									list_n[e] = None
									#print(collision)
										
						x = x + 600 
						y = y + 300

						pygame.draw.circle(fenetre, gold, (600, 300 ), ray_star)
						pygame.draw.circle(fenetre, color, (x, y), taille)

				pygame.display.update()
				pygame.time.delay(100)