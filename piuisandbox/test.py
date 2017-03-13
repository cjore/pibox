#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

# Initialisation
pygame.init()

# Définition résolution
largeur = 800
hauteur = 480

RED = (245,34,34)
epaisseur_trait = 4

# Création de la fenêtre principale
fenetre = pygame.display.set_mode((largeur,hauteur))

# Affichage du logo
logo = pygame.image.load("red_honda.png").convert_alpha()
logo_redim = pygame.transform.scale(logo, (200,200))

fenetre.blit(logo_redim, (largeur/2-logo_redim.get_width()/2,hauteur/2-logo_redim.get_height()/2))

# Affichage du cercle central 
pygame.draw.circle(fenetre, RED, (largeur/2,hauteur/2), 130, epaisseur_trait)

# Affichage du menu
pygame.draw.line(fenetre, RED, (largeur/2, hauteur/2+130), (largeur/2, hauteur), epaisseur_trait)
pygame.draw.line(fenetre, RED, (largeur/2, hauteur/2-130), (largeur/2, 0), epaisseur_trait)
pygame.draw.line(fenetre, RED, (0, hauteur/2), (largeur/2-130, hauteur/2), epaisseur_trait)
pygame.draw.line(fenetre, RED, (largeur/2+130, hauteur/2), (largeur, hauteur/2), epaisseur_trait)
pygame.draw.line(fenetre, RED, (largeur/2+91, hauteur/2+91), (largeur, hauteur), epaisseur_trait)
pygame.draw.line(fenetre, RED, (largeur/2+91, hauteur/2-91), (largeur, 0), epaisseur_trait)
pygame.draw.line(fenetre, RED, (largeur/2-91, hauteur/2-91), (0, 0), epaisseur_trait)
pygame.draw.line(fenetre, RED, (largeur/2-91, hauteur/2+91), (0, hauteur), epaisseur_trait)

# Initilisation de la olice de caractère
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 12)

# Création des labels
lprogram1 = font_renderer.render("Program1", 1, RED)
fenetre.blit(lprogram1, (largeur/4,hauteur/8))


# Rafraichissement de l'écran
pygame.display.flip()


continuer = 1

# Boucle du programme
while continuer:
	continue



