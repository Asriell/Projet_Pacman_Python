import pygame
from pygame.locals import *
from random import randint
pygame.init()
#variables globales

life = 3
pacmatrice = [4,1]
score = 0
letableaudesscores = []
def charger_sprite(fichierimage, couleurclef=(255,255,255)):
        surf = pygame.image.load(fichierimage)  #charger l'image
        surf.set_colorkey(couleurclef)   #transparence
        surf.convert()
        rect = surf.get_rect()
        return surf, rect

def mainmenu():
    pygame.display.set_caption('pac-man','pacman-icone.ico') 
    ecran = pygame. display.set_mode((1200, 800))
    fond = pygame.Surface((1200,800))
    fond.convert()
    ecran_rect = ecran.get_rect()
    titre = pygame.image.load('titre_pacman.png')  #placement du titre 
    titre.set_colorkey((255,255,255))
    titre.convert()
    position_titre = titre.get_rect()
    position_titre.midbottom = ecran_rect.midtop
    ecran.blit(titre,position_titre)
    pygame.display.flip()
    clock = pygame.time.Clock()
    #musique
    """
    pygame.mixer.music.load('musique_mainmenu.wav')
    pygame.mixer.music.play()
    """
    #déplacements du titre
    while position_titre.midbottom != ecran_rect.center:
        clock.tick(40)
        position_titre = position_titre.move((0,10))
        ecran.blit(fond,(0,0))
        ecran.blit(titre,position_titre)
        pygame.display.flip()
        
#placement et déplacements du bouton "jouer", il faudra appuyer sur 'O' pour pouvoir lancer le jeu
    jouer = pygame.image.load('jouer.png')
    jouer.set_colorkey((255,255,255))
    jouer.convert()
    position_jouer = jouer.get_rect()
    position_jouer.midtop = ecran_rect.midbottom
    ecran.blit(jouer,position_jouer)
    pygame.display.flip()
    
    while position_jouer.midtop != position_titre.midbottom:
        clock.tick(30)
        position_jouer = position_jouer.move((0,-10))
        ecran.blit(fond,(0,0))
        ecran.blit(titre,position_titre)
        ecran.blit(jouer,position_jouer)
        pygame.display.flip()
        
        
    #placement du bouton "crédits"
    menu_credits = pygame.image.load('menu_credits.png')
    menu_credits.set_colorkey((255,255,255))
    menu_credits.convert()
    position_credits = menu_credits.get_rect()
    position_credits.midtop = ecran_rect.midbottom
    ecran.blit(menu_credits,position_credits)
    pygame.display.flip()
    
    
    
    while position_credits.top >= 475:
        clock.tick(30)
        position_credits = position_credits.move((0,-10))
        ecran.blit(fond,(0,0))
        ecran.blit(titre,position_titre)
        ecran.blit(jouer,position_jouer)
        ecran.blit(menu_credits,position_credits)
        pygame.display.flip()
    
    
    
    
    
    continuer = 1
    
    pygame.display.flip()
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit() #permet de quitter le jeu en cliquant sur la X .
                pygame.mixer.music.stop()
            elif event.type == KEYDOWN:
                if event.key == K_o:
                    pygame.mixer.music.stop()
                    jeu() #lancement du jeu
                elif event.key == K_n:
                    pygame.display.quit() #permet de quitter le jeu en cliquant sur la X .
                    pygame.mixer.music.stop()
                elif event.key == K_c:
                    credits()  #lancement de la page de crédits
                elif event.key == K_s:
                    tab_score()
            
def jeu():
    
    global score, life
    #création du labyrinthe
    COTE = 40
    COULEURS = { 'bleu' : (0,0,150), 'rouge' : (200,0,0)}
    
     #réinitialisation des variables globales
    life = 3
    score = 0
    
    #Initialisation des sprites
    
   
    
    lesimages = ['pacman.png', 'fantome.png', 'fantome2.png', 'fantome3.png', 'fantome4.png','fromage.png']
    pac, position_pacman = charger_sprite(lesimages[0])
    pacman = [pac]
    #pacman est un tableau contenant les 4 surfaces possibles pour pacman
    for k in range(1, 4):
        pacman.append(pygame.transform.rotate(pac, k*90))
        
    fantomes = []
    for image in lesimages[1:]:
        fantomes.append(charger_sprite(image))
    
        
   
    
    def fichier_to_matrice(fichier):
        """Ouvre un fichier texte de type csv et récupère les données
        pour les stocker dans un tableau à 2 dimensions"""
        f = open(fichier, 'r')
        t = []
        for ligne in f:
            champs_texte = ligne.rstrip().split(',')
            #print(champs_texte) #pour visualiser
            champs_entier = [int(c) for c in champs_texte]
            #print(champs_entier) #pour visualiser
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
                elif matrice[y][x] == 0:
                    laby.blit(PASSAGE, (x*COTE, y*COTE))
                    fromage, position_fromage = charger_sprite(lesimages[5])
                    laby.blit(fromage, (x*COTE, y*COTE))
                else:
                    laby.blit(PASSAGE, (x*COTE, y*COTE))
        return laby
        
    
    #mise en place  de l'environnement graphique du labyrinthe
    matrice = fichier_to_matrice('labyrinthe_pacman.csv')
    largeur, hauteur = len(matrice[0]), len(matrice)
    ecran = pygame.display.set_mode((largeur*COTE, hauteur*COTE))
    pygame.display.set_caption('pac-man') 
    ecran_rect = ecran.get_rect()
    MUR = pygame.surface.Surface((COTE, COTE))
    MUR.fill(COULEURS['rouge'])
    MUR.convert()
    PASSAGE =  pygame.surface.Surface((COTE, COTE))
    PASSAGE.fill(COULEURS['bleu'])
    PASSAGE.convert()
    labyrinthe = matrice_to_laby(matrice)
    
    """
    def fabriquer_fromage():
        for x in range(largeur):
            for y in range(hauteur):
                if matrice[y][x] == 0:
                    fromage, position_fromage= charger_sprite(lesimages[5])
                    ecran.blit(fromage, (x*COTE, y*COTE))
                    
    def manger_fromage(rectpos):
        global score
        i,j = rectpos[0]//COTE , rectpos[1]//COTE
        tabscore = matrice
        if matrice[i][j] == 0 and tabscore[i][j] == 0:
            score += 1
            tabscore[i][j] == 1
    """


    
    
    
    """
    #musique
    pygame.mixer.music.load('pacman.wav')
    pygame.mixer.music.play(-1)
    """
    #Fonte de police de caractère
    font = pygame.font.SysFont('comicsansms',50)
    
    #On lance le chronomètre
    
    clockframe = pygame.time.Clock()
    
    
    #collage du labyrnthe
    ecran.blit(labyrinthe,(0,0)) #blit sur l'écran principal du labyrinthe

    
   #collages initiaux de pacman
    origine_pacman = (4*COTE, COTE)
    position_pacman.topleft = origine_pacman
    choixpacman = 0
    ecran.blit(pacman[choixpacman],position_pacman)  #blit sur l'écran principal de pacman
    
    
    #collages initiaux des fantomes
    origine_fantomes = [(2,11), (20,8), (12,9), (10,1)]
    for k in range(4):
        fantomes[k][1].topleft  = (origine_fantomes[k][0]*COTE, origine_fantomes[k][1]*COTE)
        ecran.blit(fantomes[k][0], fantomes[k][1])
        
    
    def deplacer_sprite(direction, rectpos):
        x, y = rectpos.topleft[0]//COTE, rectpos.topleft[1]//COTE
        if direction == 0: #droite
            x += 1
        elif direction == 1: #haut
            y += -1
        elif direction == 2: #gauche
            x -= 1
        elif direction == 3: #bas
            y += 1
        if  matrice[y][x] <= 0:
            rectpos.topleft = (x*COTE, y*COTE)
    

    def perte_de_vie(position_pacman):
        """fonction qui vérifie quand le joueur perd une vie"""
        global life
        for f in fantomes:
            if position_pacman == f[1]:
                life -= 1
                position_pacman.topleft = origine_pacman
        if life == -1 :
            letableaudesscores.append (score)
            mainmenu()
        
        
    def afficher_vie(font):
        affichage_vies = font.render(str(life),1, (255, 255, 0))
        ecran.blit(affichage_vies,(0,0))

    def afficher_temps(font):
        affichage_score = font.render(str(temps//1000),1,(255,255,0))
        ecran.blit(affichage_score,(1000,0))
    def afficher_score(font):
        affichage_score = font.render(str(score),1,(255,255,0))
        ecran.blit(affichage_score,(0,60))
    def gagner():
        global score
        if score == 176:
            pygame.mixer.stop()
            letableaudesscores.append('felicitation, vous avez gagne')
            mainmenu()


    #Boucles évènement
    continuer = 1
    
    pausefantomes = 0 #temps de pause de fantomes avant qu'ils bougent de nouveau
    temps = 0
    while continuer:
        d = clockframe.tick(60)
        temps += d
        pausefantomes += d
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit() #permet de quitter le jeu en cliquant sur la X .
                pygame.mixer.music.stop()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:#déplacement à droite
                    choixpacman = 0
                    deplacer_sprite(0, position_pacman)
                elif event.key == K_LEFT:#déplacement à gauche
                    deplacer_sprite(2, position_pacman)
                    choixpacman = 2
                elif event.key == K_UP:#déplacement en haut
                    deplacer_sprite(1, position_pacman)
                    choixpacman = 1
                elif event.key == K_DOWN:#déplacement à droite
                    deplacer_sprite(3, position_pacman)
                    choixpacman = 3
                elif event.key == K_PRINT: #appuyer sur "impécran" pour faire une capture d'écran.
                    pygame.image.save(ecran,'screenshot_pacman.png')
            x, y = position_pacman.topleft[0]//COTE, position_pacman.topleft[1]//COTE
            if matrice[y][x] == 0:
                 score += 1
                 matrice[y][x] = -1
        labyrinthe = matrice_to_laby(matrice)
        if pausefantomes >= 120: #on déplace les fantomes toutes les secondes
            pausefantomes = 0
            for f in fantomes:
                    deplacer_sprite(randint(0,3), f[1])
        perte_de_vie(position_pacman)
        gagner()
        
        #print(position_pacman.x, position_pacman.y)
        ecran.blit(labyrinthe,(0,0))
        ecran.blit(pacman[choixpacman],position_pacman)
        for f in fantomes:
            ecran.blit(f[0], f[1])
        afficher_vie(font)
        afficher_score(font)
        afficher_temps(font)
        pygame.display.flip()

            
def credits():
    ecran = pygame. display.set_mode((1200, 800))
    ecran_rect = ecran.get_rect()
    fond = pygame.Surface((1200,800))
    fond.convert()
    credit = pygame.image.load('credits.png')
    credit.set_colorkey((255,255,255))
    credit.convert()
    position_credits = credit.get_rect()
    position_credits.midtop = ecran_rect.midbottom
    ecran.blit(credit,position_credits)
    pygame.display.flip()
    """
    pygame.mixer.music.load('musique_credits.wav')
    pygame.mixer.music.play()
    """
    clock = pygame.time.Clock()
    while position_credits.midbottom != ecran_rect.midtop:
        clock.tick(20)
        position_credits= position_credits.move((0,-10))
        ecran.blit(fond,(0,0))
        ecran.blit(credit, position_credits)
        pygame.display.flip()
    pygame.mixer.music.stop()
    mainmenu()





def tab_scores():
    






#lancement du menu principal et donc du jeu
mainmenu()
    
            

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
