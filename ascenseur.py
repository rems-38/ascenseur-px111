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

et1 = pygame.image.load("./media/et1.png").convert_alpha()
et2 = pygame.image.load("./media/et2.png").convert_alpha()
et3 = pygame.image.load("./media/et3.png").convert_alpha()
et4 = pygame.image.load("./media/et4.png").convert_alpha()
et5 = pygame.image.load("./media/et5.png").convert_alpha()
pos_et1 = (255, 100)
pos_et2 = (250, 175)
pos_et3 = (250, 250)
pos_et4 = (250, 325)
pos_et5 = (250, 400)

up = pygame.image.load("./media/up.png").convert_alpha()
down = pygame.image.load("./media/down.png").convert_alpha()
pos_up1 = (325, 100)
pos_up2 = (325, 175)
pos_up3 = (325, 250)
pos_up4 = (325, 325)
pos_down2 = (400, 175)
pos_down3 = (400, 250)
pos_down4 = (400, 325)
pos_down5 = (400, 400)

# Variables
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
                time.sleep(2)
            else:
                break
            print(afficher_afficheur(etage_reel))
    
    elif etage_reel > etage_vise:    
        while etage_reel > etage_vise:
            if descendre(etage_reel) != None:
                etage_reel = descendre(etage_reel)
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

    fenetre.blit(et1, pos_et1)
    fenetre.blit(et2, pos_et2)
    fenetre.blit(et3, pos_et3)
    fenetre.blit(et4, pos_et4)
    fenetre.blit(et5, pos_et5)

    click_up1 = fenetre.blit(up, pos_up1)
    click_up2 = fenetre.blit(up, pos_up2)
    click_up3 = fenetre.blit(up, pos_up3)
    click_up4 = fenetre.blit(up, pos_up4)
    click_down2 = fenetre.blit(down, pos_down2)
    click_down3 = fenetre.blit(down, pos_down3)
    click_down4 = fenetre.blit(down, pos_down4)
    click_down5 = fenetre.blit(down, pos_down5)
    
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

            elif click_up1.collidepoint(event.pos):
                print("up1")
            elif click_up2.collidepoint(event.pos):
                print("up2")
            elif click_up3.collidepoint(event.pos):
                print("up3")
            elif click_up4.collidepoint(event.pos):
                print("up4")
            elif click_down2.collidepoint(event.pos):
                print("down2")
            elif click_down3.collidepoint(event.pos):
                print("down3")
            elif click_down4.collidepoint(event.pos):
                print("down4")
            elif click_down5.collidepoint(event.pos):
                print("down5")

            else:
                pass # pour l'instant


