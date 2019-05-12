import pygame
from pygame.locals import *
from random import randint
import time
pygame.init()
pygame.display.set_caption('pac-man') 
ecran = pygame. display.set_mode((1200, 800))
fond = pygame.Surface((1200,800))
fond.convert()
ecran_rect = ecran.get_rect()

pacman = pygame.image.load('pacman.png')  #charger l'image
pacman.set_colorkey((255,255,255))   #transparence
pacman.convert()
position_pacman=pacman.get_rect()

fantome = pygame.image.load('fantome.png')
fantome.set_colorkey((255,255,255))
fantome.convert()
position_fantome=fantome.get_rect()

fantome2 = pygame.image.load('fantome2.png')
fantome2.set_colorkey((255,255,255))
fantome2.convert()
position_fantome2 = fantome2.get_rect()

fantome3 = pygame.image.load('fantome3.png')
fantome3.set_colorkey((255,255,255))
fantome3.convert()
position_fantome3 = fantome3.get_rect()

fantome4 = pygame.image.load('fantome4.png')
fantome4.set_colorkey((255,255,255))
fantome4.convert()
position_fantome4 = fantome4.get_rect()





#création du labyrinthe
COTE = 40
COULEURS = { 'bleu' : (0,0,150), 'rouge' : (200,0,0)}



def fichier_to_matrice(fichier):
    """Ouvre un fichier texte de type csv et récupère les données
    pour les stocker dans un tableau à 2 dimensions"""
    f = open(fichier, 'r')
    t = []
    for ligne in f:
        champs_texte = ligne.rstrip().split(',')
        print(champs_texte) #pour visualiser
        champs_entier = [int(c) for c in champs_texte]
        print(champs_entier) #pour visualiser
        t.append(champs_entier)
    #en une ligne :
    #return [list(map(int, ligne.rstrip().split(','))) for ligne in f]
    f.close()
    return t
    
def matrice_to_laby(matrice):
    """Convertit en surface un tableau à deux dimensions représentant un labyrinthe"""
    #Largeur w (en briques) : le nombre d'éléments (ou colonnes) de la première ligne de l matrice
    #Hauteur h le nombre de lignes de la matrice
    largeur, hauteur = len(matrice[0]), len(matrice)
    laby = pygame.surface.Surface((largeur*COTE, hauteur*COTE))
    laby.convert()
    for x in range(largeur):
        for y in range(hauteur):
            if matrice[y][x] == 1:
                laby.blit(MUR, (x*COTE, y*COTE))
            else:
                laby.blit(PASSAGE, (x*COTE, y*COTE))
    return laby
    
    


#mise en place  de l'environnement graphique du labyrinthe
matrice = fichier_to_matrice('labyrinthe_pacman.csv')
largeur, hauteur = len(matrice[0]), len(matrice)
ecran = pygame.display.set_mode((largeur*COTE, hauteur*COTE))
MUR = pygame.surface.Surface((COTE, COTE))
MUR.fill(COULEURS['rouge'])
MUR.convert()
PASSAGE =  pygame.surface.Surface((COTE, COTE))
PASSAGE.fill(COULEURS['bleu'])
PASSAGE.convert()
labyrinthe = matrice_to_laby(matrice)

"""
#musique
pygame.mixer.music.load('pacman.wav')
pygame.mixer.music.play()

"""

clock = pygame.time.Clock()
#collage du labyrnthe
ecran.blit(labyrinthe,(0,0)) #blit sur l'écran principal du labyrinthe



#collages initiaux de pacman
pacmatrice = [4, 1]
position_pacman = position_pacman.move((pacmatrice[1]*40,pacmatrice[0]*40))
ecran.blit(pacman,position_pacman)  #blit sur l'écran principal de pacman


#collages initiaux des fantomes
fantomatrice = [11,2]
position_fantome = position_fantome.move((fantomatrice[1]*40,fantomatrice[0]*40))
ecran.blit(fantome,position_fantome)

fantomatrice2 = [8,20]
position_fantome2 = position_fantome2.move((fantomatrice2[1]*40,fantomatrice2[0]*40))
ecran.blit(fantome2, position_fantome2)

fantomatrice3 = [9,12]
position_fantome3 = position_fantome3.move((fantomatrice3[1]*40,fantomatrice3[0]*40))
ecran.blit(fantome3, position_fantome3)

fantomatrice4 = [1,10]
position_fantome4 = position_fantome4.move((fantomatrice4[1]*40,fantomatrice4[0]*40))
ecran.blit(fantome4,position_fantome4)




def deplacer_pacman(n):
    global position_pacman
    i, j = pacmatrice 
    if n == 0: #droite
        j += 1
    elif n == 1: #gauche
        j += -1
    elif n == 2: #haut
        i += -1
    elif n == 3:
        i += 1
    if  matrice[i][j] == 0:
        print(i, j)
        pacmatrice[0], pacmatrice[1] = i, j
        position_pacman.topleft = (pacmatrice[1]*40, pacmatrice[0]*40)
        


def deplacer_fantome(n):
    global position_fantome
    x, y = fantomatrice
    if n == 0: #droite
        y += 1
    elif n == 1: #gauche
        y += -1
    elif n == 2: #haut
        x += -1
    elif n == 3:
        x += 1
    if  matrice[x][y] == 0:
        fantomatrice[0], fantomatrice[1] = x, y
        position_fantome.topleft = (fantomatrice[1]*40, fantomatrice[0]*40)
    return position_fantome

def deplacer_fantome2(n):
    global position_fantome2
    x, y = fantomatrice2
    if n == 0: #droite
        y += 1
    elif n == 1: #gauche
        y += -1
    elif n == 2: #haut
        x += -1
    elif n == 3:
        x += 1
    if  matrice[x][y] == 0:
        fantomatrice2[0], fantomatrice2[1] = x, y
        position_fantome2.topleft = (fantomatrice2[1]*40, fantomatrice2[0]*40)
    return position_fantome2




def deplacer_fantome3(n):
    global position_fantome3
    x, y = fantomatrice3
    if n == 0: #droite
        y += 1
    elif n == 1: #gauche
        y += -1
    elif n == 2: #haut
        x += -1
    elif n == 3: #bas
        x += 1
    if  matrice[x][y] == 0:
        fantomatrice3[0], fantomatrice3[1] = x, y
        position_fantome3.topleft = (fantomatrice3[1]*40, fantomatrice3[0]*40)
    return position_fantome3


def deplacer_fantome4(n):
    global position_fantome4
    x, y = fantomatrice4
    if n == 0: #droite
        y += 1
    elif n == 1: #gauche
        y += -1
    elif n == 2: #haut
        x += -1
    elif n == 3:
        x += 1
    if  matrice[x][y] == 0:
        fantomatrice4[0], fantomatrice4[1] = x, y
        position_fantome4.topleft = (fantomatrice4[1]*40, fantomatrice4[0]*40)
    return position_fantome4
    
    
    
def perte_de_vie():
    """fonction qui vérifie quand le joueur perd une vie"""
    global life
    global pacmatrice
    if position_pacman == position_fantome or position_pacman == position_fantome2 or position_pacman == position_fantome3 or position_pacman == position_fantome4:
        life -= 1
        pacmatrice = [4, 4]
        if life == -1:
            pygame.quit()
        
        
def afficher_vie():
    font = pygame.font.SysFont('comicsansms',50)
    afficher_vies = font.render(str(life), 1, (255, 255, 0))
    ecran.blit(afficher_vies,(0,0))


fromage = pygame.image.load('fromage.png')
fromage.set_colorkey((255,255,255))
fromage.convert()

def creation_fromages():
    """Convertit en surface un tableau à deux dimensions représentant un labyrinthe"""
    #Largeur w (en briques) : le nombre d'éléments (ou colonnes) de la première ligne de l matrice
    #Hauteur h le nombre de lignes de la matrice
    largeur, hauteur = len(matrice[0]), len(matrice)
    i= 0
    for x in range(largeur):
        for y in range(hauteur):
            if matrice[y][x] == 0:
                ecran.blit(fromage, (x*COTE,y*COTE))
                
                







creation_fromages()


life = 3
#Boucles évènement
continuer = 1

pygame.display.flip()
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit() #permet de quitter le jeu en cliquant sur la X .
            pygame.mixer.music.stop()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:#déplacement à droite
                deplacer_pacman(0)
                n = randint(0,3)
                o = randint(0,3)
                p = randint(0,3)
                q = randint(0,3)
                deplacer_fantome(n)
                deplacer_fantome2(o)
                deplacer_fantome3(p)
                deplacer_fantome4(q)
                perte_de_vie()
                print(position_pacman.x, position_pacman.y)
                ecran.blit(labyrinthe,(0,0))
                ecran.blit(pacman,position_pacman)
                ecran.blit(fantome,position_fantome)
                ecran.blit(fantome2,position_fantome2)
                ecran.blit(fantome3,position_fantome3)
                ecran.blit(fantome4,position_fantome4)
                afficher_vie()
                pygame.display.flip()
            elif event.key == K_LEFT:#déplacement à droite
                pacman3= pygame.transform.rotate(pacman,180)
                deplacer_pacman(1)
                n = randint(0,3)
                o = randint(0,3)
                p = randint(0,3)
                q = randint(0,3)
                deplacer_fantome(n)
                deplacer_fantome2(o)
                deplacer_fantome3(p)
                deplacer_fantome4(q)
                perte_de_vie()
                print(position_pacman.x, position_pacman.y)
                ecran.blit(labyrinthe,(0,0))
                ecran.blit(pacman3,position_pacman)
                ecran.blit(fantome,position_fantome)
                ecran.blit(fantome2,position_fantome2)
                ecran.blit(fantome3,position_fantome3)
                ecran.blit(fantome4,position_fantome4)
                afficher_vie()
                pygame.display.flip()
            elif event.key == K_UP:#déplacement à droite
                pacman2= pygame.transform.rotate(pacman,90)
                deplacer_pacman(2)
                n = randint(0,3)
                o = randint(0,3)
                p = randint(0,3)
                q = randint(0,3)
                deplacer_fantome(n)
                deplacer_fantome2(o)
                deplacer_fantome3(p)
                deplacer_fantome4(q)
                perte_de_vie()
                print(position_pacman.x, position_pacman.y)
                ecran.blit(labyrinthe,(0,0))
                ecran.blit(pacman2,position_pacman)
                ecran.blit(fantome,position_fantome)
                ecran.blit(fantome2,position_fantome2)
                ecran.blit(fantome3,position_fantome3)
                ecran.blit(fantome4,position_fantome4)
                afficher_vie()
                pygame.display.flip()
            elif event.key == K_DOWN:#déplacement à droite
                pacman4= pygame.transform.rotate(pacman,270)
                deplacer_pacman(3)
                n = randint(0,3)
                o = randint(0,3)
                p = randint(0,3)
                q = randint(0,3)
                deplacer_fantome(n)
                deplacer_fantome2(o)
                deplacer_fantome3(p)
                deplacer_fantome4(q)
                perte_de_vie()
                print(position_pacman.x, position_pacman.y)
                ecran.blit(labyrinthe,(0,0))
                ecran.blit(pacman4,position_pacman)
                ecran.blit(fantome,position_fantome)
                ecran.blit(fantome2,position_fantome2)
                ecran.blit(fantome3,position_fantome3)
                ecran.blit(fantome4,position_fantome4)
                afficher_vie()
                pygame.display.flip()
            elif event.key == K_PRINT: #appuyer sur "impécran" pour faire une capture d'écran.
                pygame.image.save(ecran,'screenshot_pacman.png')
                    
                

                


