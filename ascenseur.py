# -*- coding: utf-8 -*-

"""
Projet :
- Ascenseur 5 étages
- Afficheur des étages (de 1 à 5)
- Sur chaque palier, boutons pour appeler l'ascenseur (2 boutons : un si on veut monter et un si on veut descendre [pour le 1er et le dernier étage un seul bouton car on peut
    pas monter/descendre plus, déjà au max/min])
- Dans la cabine : 5 boutons pour aller sur chaque étages


Trouver une idée pour les boutons : lib msvcrt (https://stackoverflow.com/questions/2408560/non-blocking-console-input)
"""

import pygame
from pygame.locals import *

import time

fenetre = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ascenseur")
pygame.display.flip()

bt1 = pygame.image.load("./media/bouton1.png").convert_alpha()
bt2 = pygame.image.load("./media/bouton2.png").convert_alpha()
bt3 = pygame.image.load("./media/bouton3.png").convert_alpha()
bt4 = pygame.image.load("./media/bouton4.png").convert_alpha()
bt5 = pygame.image.load("./media/bouton5.png").convert_alpha()
pos_bt1 = (125, 25)
pos_bt2 = (200, 25)
pos_bt3 = (275, 25)
pos_bt4 = (350, 25)
pos_bt5 = (425, 25)

aff1 = pygame.image.load("./media/aff1.png").convert_alpha()
aff2 = pygame.image.load("./media/aff2.png").convert_alpha()
aff3 = pygame.image.load("./media/aff3.png").convert_alpha()
aff4 = pygame.image.load("./media/aff4.png").convert_alpha()
aff5 = pygame.image.load("./media/aff5.png").convert_alpha()
pos_aff = (25, 25)


# Def des variables
bt_cab_1 = 0 # Bouton dans cabine pour aller à l'étage 1
bt_cab_2 = 0
bt_cab_3 = 0
bt_cab_4 = 0
bt_cab_5 = 0
ap_et1_up = 0 # Bouton pour appeler l'ascenseur quand on est à l'étage 1 et qu'on veut monter
ap_et2_up = 0
ap_et2_dwn = 0 # Bouton pour appeler l'ascenseur quand on est à l'étage 2 et qu'on veut descendre
ap_et3_up = 0
ap_et3_dwn = 0
ap_et4_up = 0
ap_et4_dwn = 0
ap_et5_dwn = 0
afficheur = [0, 0, 0] # Tableau pour coder en binaire le n° des étages avec aff[0] bit poids fort et aff[2] bit poids faible
etage_reel = 0 # L'étage 0 en Python correspond à l'étage 1 en réalité
etage_vise = [0] # Tableau pour l'(es) étage(s) visé(s) (comprend la mémorisation)


def monter(etage):
    if etage + 1 == 5:
        return None
    else:
        return etage + 1

def descendre(etage):
    if etage - 1 == -1:
        return None
    else:
        return etage - 1

# Afficheur
def afficher_afficheur(etage_reel):
    if etage_reel == 0: # afficher 1
        afficheur[0] = 0
        afficheur[1] = 0
        afficheur[2] = 1
    elif etage_reel == 1: # afficher 2
        afficheur[0] = 0
        afficheur[1] = 1
        afficheur[2] = 0
    elif etage_reel == 2: # afficher 3
        afficheur[0] = 0
        afficheur[1] = 1
        afficheur[2] = 1
    elif etage_reel == 3: # afficher 4
        afficheur[0] = 1
        afficheur[1] = 0
        afficheur[2] = 0
    elif etage_reel == 4: # afficher 5
        afficheur[0] = 1
        afficheur[1] = 0
        afficheur[2] = 1
    else:
        afficheur[0] = 0
        afficheur[1] = 0
        afficheur[2] = 0
    return afficheur[0] * 4 + afficheur[1] * 2 + afficheur[2] * 1


def aller_a_etage(etage_reel, etage_vise):
    print(afficher_afficheur(etage_reel))
    if etage_reel < etage_vise:
        while etage_reel < etage_vise:
            if monter(etage_reel) != None:
                etage_reel = monter(etage_reel)
                time.sleep(2)
            else:
                break
            print(afficher_afficheur(etage_reel))
    
    elif etage_reel > etage_vise:    
        while etage_reel > etage_vise:
            if descendre(etage_reel) != None:
                etage_reel = descendre(etage_reel)
                time.sleep(2)
            else:
                break
            print(afficher_afficheur(etage_reel))

    return etage_reel
            

continuer = 1
while continuer:
    click_bt1 = fenetre.blit(bt1, pos_bt1)
    click_bt2 = fenetre.blit(bt2, pos_bt2)
    click_bt3 = fenetre.blit(bt3, pos_bt3)
    click_bt4 = fenetre.blit(bt4, pos_bt4)
    click_bt5 = fenetre.blit(bt5, pos_bt5)
    
    if etage_reel == 0:
        fenetre.blit(aff1, pos_aff)
    elif etage_reel == 1:
        fenetre.blit(aff2, pos_aff)
    elif etage_reel == 2:
        fenetre.blit(aff3, pos_aff)
    elif etage_reel == 3:
        fenetre.blit(aff4, pos_aff)
    elif etage_reel == 4:
        fenetre.blit(aff5, pos_aff)
    else:
        pass

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if click_bt1.collidepoint(event.pos):
                etage_reel = aller_a_etage(etage_reel, 0)
            elif click_bt2.collidepoint(event.pos):
                etage_reel = aller_a_etage(etage_reel, 1)
            elif click_bt3.collidepoint(event.pos):
                etage_reel = aller_a_etage(etage_reel, 2)
            elif click_bt4.collidepoint(event.pos):
                etage_reel = aller_a_etage(etage_reel, 3)
            elif click_bt5.collidepoint(event.pos):
                etage_reel = aller_a_etage(etage_reel, 4)
            else:
                pass # pour l'instant





#aller_a_etage(4, 2)