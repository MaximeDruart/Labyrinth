import pygame
from pygame.locals import*

import random
from operator import itemgetter

imagelog=pygame.image.load('imagelog.png')
dos_carte=pygame.image.load("cartes/dos_carte.png") # chargement du dos de carte. Je me sentais mal de faire une fonction pour juste ca
liste_message=[]



class perso:
    def __init__(self,x,y,nomjoueur,imagehaut,imagebas,imagegauche,imagedroite):
        self.x=x # sa position horizontale en pixel
        self.y=y # sa position verticale en pixel
        self.casex=int(self.x/100) # les cases font 100*100
        self.casey=int(self.y/100)
        self.haut=pygame.image.load(imagehaut).convert_alpha() # on charge les images correspondant aux joueurs, une pour chaque côté
        self.bas=pygame.image.load(imagebas).convert_alpha()
        self.gauche=pygame.image.load(imagegauche).convert_alpha()
        self.droite=pygame.image.load(imagedroite).convert_alpha()
        self.direction=self.bas # le joueur commence en regardant vers le bas
        self.tresors=0 # liste des trésors qu'il doit atteindre
        self.tresor_actif=[0,0] # liste correspondant au trésor actif, le premier élément correspond au nom et le second au blit de la carte correspondante
        self.compteur_tresor=0 # le nombre de trésor que le joueur a amassé
        self.nomjoueur=str(nomjoueur[3:-1]+' '+nomjoueur[-1]) # j'ai appelé les joueurs (nomjoueur1,nomjoueur2), du coup de je le raccourcis et change en joueur 1, joueur 2

    def deplacer(self,direction):
        """ la seule fonction de notre classe, on teste si la case du perso et celle vers laquelle il tente d'aller ne sont pas des murs, puis change le joueur.y/x et casex/y
        on change aussi le statut possession de perso de l'ancienne et nouvelle case. Finalement on change la direction dans laquelle regarde le perso
        """
        if direction == "haut":
            if self.y>=200: #Eviter que le joueur sorte de la grille
                if grille[self.casey-1][self.casex-1][2][0]==1 and grille[self.casey-2][self.casex-1][2][1]==1: # on teste si le déplacement est autorisé : sur la case du joueur et la case au dessus pour le déplacement vers le haut
                    grille[self.casey-1][self.casex-1][3]=0 #on enleve perso=1 de la case sur laquelle etait le perso
                    self.casey-=1
                    self.y=self.casey*100
                    grille[self.casey-1][self.casex-1][3]=1 # perso=1 pour la case sur laquelle le perso passe
            self.direction=self.haut

        if direction == "bas":
            if self.y<=600: #Eviter que le joueur sorte de la grille
                if grille[self.casey-1][self.casex-1][2][1]==1 and grille[self.casey][self.casex-1][2][0]==1: # on teste si le déplacement est autorisé : sur la case du joueur et la case en dessous
                    grille[self.casey-1][self.casex-1][3]=0
                    self.casey+=1
                    self.y=self.casey*100
                    grille[self.casey-1][self.casex-1][3]=1
            self.direction=self.bas

        if direction == "gauche":
            if self.x>=200: #Eviter que le joueur sorte de la grille
                if grille[self.casey-1][self.casex-1][2][2]==1 and grille[self.casey-1][self.casex-2][2][3]==1: # on teste si le déplacement est autorisé : sur la case du joueur et la case a gauche pour le déplacement vers la gauche
                    grille[self.casey-1][self.casex-1][3]=0
                    self.casex-=1
                    self.x=self.casex*100
                    grille[self.casey-1][self.casex-1][3]=1
            self.direction=self.gauche

        if direction == "droite":
            if self.x<=600: #Eviter que le joueur sorte de la grille
                if grille[self.casey-1][self.casex-1][2][3]==1 and grille[self.casey-1][self.casex][2][2]==1: # on teste si le déplacement est autorisé : sur la case du joueur et la case a droite pour le déplacement vers la droite
                    grille[self.casey-1][self.casex-1][3]=0
                    self.casex+=1
                    self.x=self.casex*100
                    grille[self.casey-1][self.casex-1][3]=1
            self.direction=self.droite



def choixcartes(nbjoueurs): #
    """ on créé les decks de trésors des joueurs en fonction de leur nombre, on sort avec leurs objectifs dans joueur.tresor, joueur.tresor_actif
    C'est tout simplement un mélange de cartes qu'on distribue aux joueurs, mais toujours 4 cartes peu importe le nombre de joueurs, c'est des parties courtes
     """
    cartesj1=[];cartesj2=[];cartesj3=[];cartesj4=[]
    tresors2=tresors[:]
    if nbjoueurs==2:
        random.shuffle(tresors2)
        for i in range(4):
            cartesj1.append(tresors2[i])
            cartesj2.append(tresors2[i+4])
        cartesjoueurs=[cartesj1,cartesj2,cartesj3]
        j1.tresors=cartesj1[:] ; j1.tresor_actif[0]=cartesj1[0] ; # le trésor actif constitue l'objectif actuel du joueur, qu'on initialise a la premiere carte de joueur.tresors
        j1.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj1[0])+'.png') # on charge l'image au nom du trésor dans le dossier cartes
        j1.tresor_actif[1]=pygame.transform.scale(j1.tresor_actif[1],(125,192)) # on rescale les images a une taille acceptable pour notre fenetre de 1500*900
        j2.tresors=cartesj2[:] ; j2.tresor_actif[0]=cartesj2[0]
        j2.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj2[0])+'.png')
        j2.tresor_actif[1]=pygame.transform.scale(j2.tresor_actif[1],(125,192))
        for j in joueurs:
            print(j.tresor_actif) # du troubleshoot
    if nbjoueurs==3:
        random.shuffle(tresors2)
        for i in range(4):
            cartesj1.append(tresors2[i])
            cartesj2.append(tresors2[i+4])
            cartesj3.append(tresors2[i+8])
        cartesjoueurs=[cartesj1,cartesj2,cartesj3]
        j1.tresors=cartesj1[:] ; j1.tresor_actif[0]=cartesj1[0]
        j1.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj1[0])+'.png')
        j1.tresor_actif[1]=pygame.transform.scale(j1.tresor_actif[1],(125,192))
        j2.tresors=cartesj2[:] ; j2.tresor_actif[0]=cartesj2[0]
        j2.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj2[0])+'.png')
        j2.tresor_actif[1]=pygame.transform.scale(j2.tresor_actif[1],(125,192))
        j3.tresors=cartesj3[:] ; j3.tresor_actif[0]=cartesj3[0]
        j3.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj3[0])+'.png')
        j3.tresor_actif[1]=pygame.transform.scale(j3.tresor_actif[1],(125,192))
        for j in joueurs:
            print(j.tresor_actif)
    if nbjoueurs==4:
        random.shuffle(tresors2)
        for i in range(4):
            cartesj1.append(tresors2[i])
            cartesj2.append(tresors2[i+4])
            cartesj3.append(tresors2[i+8])
            cartesj4.append(tresors2[i+12])
        cartesjoueurs=[cartesj1,cartesj2,cartesj3,cartesj4]
        j1.tresors=cartesj1[:] ; j1.tresor_actif[0]=cartesj1[0]
        j1.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj1[0])+'.png')
        j1.tresor_actif[1]=pygame.transform.scale(j1.tresor_actif[1],(125,192))
        j2.tresors=cartesj2[:] ; j2.tresor_actif[0]=cartesj2[0]
        j2.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj2[0])+'.png')
        j2.tresor_actif[1]=pygame.transform.scale(j2.tresor_actif[1],(125,192))
        j3.tresors=cartesj3[:] ; j3.tresor_actif[0]=cartesj3[0]
        j3.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj3[0])+'.png')
        j3.tresor_actif[1]=pygame.transform.scale(j3.tresor_actif[1],(125,192))
        j4.tresors=cartesj4[:] ; j4.tresor_actif[0]=cartesj4[0]
        j4.tresor_actif[1]=pygame.image.load('cartes/'+str(cartesj4[0])+'.png')
        j4.tresor_actif[1]=pygame.transform.scale(j4.tresor_actif[1],(125,192))
        for j in joueurs:
            print(j.tresor_actif)

def creationperso(nbjoueurs):
    """ plutot explicite, ca prend le nombre de joueurs et créé n joueurs a partir de la classe perso """
    global j1;global j2;global j3;global j4;global joueurs
    if nbjoueurs==2:
        j1=perso(100,100,'nomjoueur1','personnages/personnage1haut.png','personnages/personnage1bas.png','personnages/personnage1gauche.png','personnages/personnage1droite.png')
        j2=perso(700,700,'nomjoueur2','personnages/personnage2haut.png','personnages/personnage2bas.png','personnages/personnage2gauche.png','personnages/personnage2droite.png')
        joueurs=[j1,j2] # liste plus tard utilisé pour boucler les tours de jeu
        grille[0][0][3]=1 # statut 'contient un perso' pour les cases de leur spawn
        grille[0][-1][3]=1
        return joueurs

    if nbjoueurs==3:
        j1=perso(100,100,'nomjoueur1','personnages/personnage1haut.png','personnages/personnage1bas.png','personnages/personnage1gauche.png','personnages/personnage1droite.png')
        j2=perso(700,700,'nomjoueur2','personnages/personnage2haut.png','personnages/personnage2bas.png','personnages/personnage2gauche.png','personnages/personnage2droite.png')
        j3=perso(100,700,'nomjoueur3','personnages/personnage3haut.png','personnages/personnage3bas.png','personnages/personnage3gauche.png','personnages/personnage3droite.png')
        joueurs=[j1,j2,j3]
        grille[0][0][3]=1
        grille[0][-1][3]=1
        grille[-1][0][3]=1
        return joueurs

    if nbjoueurs==4:
        j1=perso(100,100,'nomjoueur1','personnages/personnage1haut.png','personnages/personnage1bas.png','personnages/personnage1gauche.png','personnages/personnage1droite.png')
        j2=perso(700,700,'nomjoueur2','personnages/personnage2haut.png','personnages/personnage2bas.png','personnages/personnage2gauche.png','personnages/personnage2droite.png')
        j3=perso(100,700,'nomjoueur3','personnages/personnage3haut.png','personnages/personnage3bas.png','personnages/personnage3gauche.png','personnages/personnage3droite.png')
        j4=perso(700,100,'nomjoueur4','personnages/personnage4haut.png','personnages/personnage4bas.png','personnages/personnage4gauche.png','personnages/personnage4droite.png')
        joueurs=[j1,j2,j3,j4]
        grille[0][0][3]=1
        grille[0][-1][3]=1
        grille[-1][0][3]=1
        grille[-1][-1][3]=1
        return joueurs



def affichage_message(message):
    """
Une petite fonction qui permettra d'envoyer du texte sur l'interface de jeu sur une zone a droite du plateau. On donne affichage_message('string') et ca l'affiche dans la zone prevu pour.
Ca gere les exceptions comme si la zone est pleine (elle se remplit par le bas et supprime lorsqu'elle a plus de 6 messages d'un coup) ou que le message fait plus de 43 caractères
(max 86 caractères, mais bon sinon suffit de faire 2 affichage_message() )

    """

    fenetre.blit(imagelog,(900,300))
    pygame.display.flip()
    i=0
    global compteur_message;global message1;global message2
    if len(message)>43:
        message1=message[:43]
        message2=message[43:]
        if len(liste_message)<=4: # 4 ou moins, il y a donc de la place pour 2 messages
            liste_message.insert(0,message1)
            liste_message.insert(0,message2)
        elif len(liste_message)==5: # de la place pour 1 msg en plus, on en rajoute 2 et en pop 1
            liste_message.insert(0,message1)
            liste_message.insert(0,message2)
            liste_message.pop()
        else: # soit 6, donc on rajoute 2 et pop 2
            liste_message.insert(0,message1) # ajoute le nouvel element en index 0
            liste_message.insert(0,message2)
            liste_message.pop();liste_message.pop() # supprime le dernier element
    else:
        if len(liste_message)<6:
            liste_message.insert(0,message)
        else:
            liste_message.insert(0,message) # ajoute le nouvel element en index 0
            liste_message.pop() # supprime le dernier element

    textdisplay=pygame.font.Font('AtlantisInlineGrunge.ttf',20)
    for message in liste_message:
        textSurface=textdisplay.render(message,True,(255,255,255))
        textRect = textSurface.get_rect(left=(905),y=440-i*25)
        fenetre.blit(textSurface,textRect)
        i+=1
    pygame.display.flip()



def affiche_cartes():
    """ ca colle du dos de carte en fonction du nombre de joueurs"""
    if nbjoueurs==2:
        fenetre.blit(dos_carte,(920,100))
        fenetre.blit(dos_carte,(1065,100))
    if nbjoueurs==3:
        fenetre.blit(dos_carte,(920,100))
        fenetre.blit(dos_carte,(1065,100))
        fenetre.blit(dos_carte,(1210,100))
    if nbjoueurs==4:
        fenetre.blit(dos_carte,(920,100))
        fenetre.blit(dos_carte,(1065,100))
        fenetre.blit(dos_carte,(1210,100))
        fenetre.blit(dos_carte,(1355,100))


def bloc_actu(): #Ca correspond aux elements qu'on veut blit a peu pres tout le temps, on réaffiche les dos de carte, le plateau de jeu, les personnages en eux mêmes'''
    affiche_cartes() # dos de carte
    affiche2(grille) # plateau de jeu
    for j in joueurs: # joueurs
        fenetre.blit(j.direction, (j.x, j.y))
    pygame.display.update() # le fameux


def load_compteurtresor(): # On load les compteurs qui afficheront le nombre de trésors restants a chaque joueur pour gagner
    global imgtresors4;global imgtresors3;global imgtresors2;global imgtresors1;global imgtresors0
    imgtresors4=pygame.image.load('tresors4.png')
    imgtresors3=pygame.image.load('tresors3.png')
    imgtresors2=pygame.image.load('tresors2.png')
    imgtresors1=pygame.image.load('tresors1.png')
    imgtresors0=pygame.image.load('tresors0.png')


def affichage_compteurtresor4(): # ca sera utilisé seulement utilisé, quand tous les joueurs ont 4 trésors a atteindre (toujours effectué en fn du nombre de joueurs)
    for i in range(nbjoueurs):
        fenetre.blit(imgtresors4,(920+i*145,0))
        pygame.display.update()

def affichage_compteurtresor():
    """ L'affichage des compteurs lorsqu'il est différent de 4. On fait des petits tests avec la variable joueur.compteur_tresor qui est incrémenté lors de l'acquisition d'un trésor
    La position change en fonction du joueur
    """
    if joueur==j1:
        if 4-(joueur.compteur_tresor)==3:
            fenetre.blit(imgtresors3,(920,000))
        elif 4-(joueur.compteur_tresor)==2:
            fenetre.blit(imgtresors2,(920,000))
        elif 4-(joueur.compteur_tresor)==1:
            fenetre.blit(imgtresors1,(920,000))
        elif 4-(joueur.compteur_tresor)==0:
            fenetre.blit(imgtresors0,(920,000))
        else:
            fenetre.blit(imgtresors4,(920,0))
    pygame.display.update()
    if joueur==j2:
        if 4-(joueur.compteur_tresor)==3:
            fenetre.blit(imgtresors3,(1065,000))
        elif 4-(joueur.compteur_tresor)==2:
            fenetre.blit(imgtresors2,(1065,000))
        elif 4-(joueur.compteur_tresor)==1:
            fenetre.blit(imgtresors1,(1065,000))
        elif 4-(joueur.compteur_tresor)==0:
            fenetre.blit(imgtresors0,(1065,000))
        else:
            fenetre.blit(imgtresors4,(1065,0))
    pygame.display.flip()
    if nbjoueurs>=3:
        if joueur==j3:
            if 4-(joueur.compteur_tresor)==3:
                fenetre.blit(imgtresors3,(1210,000))
            elif 4-(joueur.compteur_tresor)==2:
                fenetre.blit(imgtresors2,(1210,000))
            elif 4-(joueur.compteur_tresor)==1:
                fenetre.blit(imgtresors1,(1210,000))
            elif 4-(joueur.compteur_tresor)==0:
                fenetre.blit(imgtresors0,(1210,000))
            else:
                fenetre.blit(imgtresors4,(1210,0))

        pygame.display.flip()
    if nbjoueurs>=4:
        if joueur==j3:
            if 4-(joueur.compteur_tresor)==3:
                fenetre.blit(imgtresors3,(1210,000))
            elif 4-(joueur.compteur_tresor)==2:
                fenetre.blit(imgtresors2,(1210,000))
            elif 4-(joueur.compteur_tresor)==1:
                fenetre.blit(imgtresors1,(1210,000))
            elif 4-(joueur.compteur_tresor)==0:
                fenetre.blit(imgtresors0,(1210,000))
            else:
                fenetre.blit(imgtresors4,(1210,0))
        pygame.display.flip()
        if joueur==j4:
            if 4-(joueur.compteur_tresor)==3:
                fenetre.blit(imgtresors3,(1355,000))
            elif 4-(joueur.compteur_tresor)==2:
                fenetre.blit(imgtresors2,(1355,000))
            elif 4-(joueur.compteur_tresor)==1:
                fenetre.blit(imgtresors1,(1355,000))
            elif 4-(joueur.compteur_tresor)==0:
                fenetre.blit(imgtresors0,(1355,000))
            else:
                fenetre.blit(imgtresors4,(1355,0))
        pygame.display.flip()

def overlap_cartes():
    if joueur==j1:
        if 920<event.pos[0]<1045 and 100<event.pos[1]<292: # position du dos de carte du joueur 1
            fenetre.blit(joueur.tresor_actif[1],(920,100)) # on colle alors la carte correspondant a son tresor actif précédemment chargé
            pygame.display.flip()
        else:
            fenetre.blit(dos_carte,(920,100)) # lorsqu'il n'est pas dessus, le dos est affiché
            bloc_actu()
    if joueur==j2:
        if 1065<event.pos[0]<1190 and 100<event.pos[1]<292:
            fenetre.blit(joueur.tresor_actif[1],(1065,100))
            pygame.display.flip()
        else:
            fenetre.blit(dos_carte,(1065,100))
            bloc_actu()
    if nbjoueurs>=3:
        if joueur==j3:
            if 1210<event.pos[0]<1335 and 100<event.pos[1]<292:
                fenetre.blit(joueur.tresor_actif[1],(1210,100))
                pygame.display.flip()
            else:
                fenetre.blit(dos_carte,(1210,100))
                bloc_actu()
    if nbjoueurs>=4:
        if joueur==j3:
            if 1210<event.pos[0]<1335 and 100<event.pos[1]<292:
                fenetre.blit(joueur.tresor_actif[1],(1210,100))
                pygame.display.flip()
            else:
                fenetre.blit(dos_carte,(1210,100))
                bloc_actu()
        if joueur==j4:
            if 1355<event.pos[0]<1480 and 100<event.pos[1]<292:
                fenetre.blit(joueur.tresor_actif[1],(1355,100))
                pygame.display.flip()
            else:
                fenetre.blit(dos_carte,(1355,100))


from main import grille