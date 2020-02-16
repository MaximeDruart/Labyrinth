import pygame
from pygame.locals import*

import random
from operator import itemgetter

from fonctionsgrille import*

pygame.init()

fenetre=pygame.display.set_mode((1500,900),RESIZABLE)
bg=pygame.image.load('backg.jpg').convert()
icone = pygame.image.load('cases/3wayupdragon.png')
pygame.display.set_icon(icone)
pygame.display.set_caption('Labyrinthe')

imagelog=pygame.image.load('imagelog.png')
liste_message=[]
dos_carte=pygame.image.load("cartes/dos_carte.png") # chargement du dos de carte. Je me sentais mal de faire une fonction pour juste ca




grille=generation_grille()
collage_grille(grille)


continuer=1
while continuer: # la boucle principale qui regroupera toutes les sous-boucles (menu, aide, crédits, jeu)

    imagemenu=pygame.image.load('imagemenu.jpg').convert()
    fenetre.blit(imagemenu,(0,0))
    pygame.display.flip()

    continuer_menu = 1
    continuer_jeu = 1
    continuer_aide = 1
    continuer_credits = 1 # les 4 cavaliers de l'apocalypse


    while continuer_menu:
        pygame.time.Clock().tick(30) # bloque le refresh rate a 30 par seconde

        for event in pygame.event.get():
            if event.type==pygame.VIDEORESIZE: # permet de resize la fenetre de menu, j'aurais aimé le faire pour la fenetre de jeu mais il y a trop d'images.
                fenetre=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                fenetre.blit(pygame.transform.scale(imagemenu,event.dict['size']),(0,0))
                pygame.display.flip()

            if event.type == QUIT: # les conditions de sortie classique
                continuer_menu = 0
                continuer_jeu = 0
                continuer = 0
                nbjoueurs=0

                pygame.quit()

            if event.type==KEYDOWN:

                if event.key==K_F2: # F2 : Lancement du mode 2 joueurs
                    continuer_menu=0
                    continuer_aide=0
                    continuer_credits=0
                    nbjoueurs=2

                if event.key==K_F3: # F3 : Lancement du mode 3 joueurs
                    continuer_menu=0
                    continuer_aide=0
                    continuer_credits=0
                    nbjoueurs=3

                if event.key==K_F4: # F4 : Lancement du mode 4 joueurs
                    continuer_menu=0
                    continuer_aide=0
                    continuer_credits=0
                    nbjoueurs=4

            if event.type==MOUSEBUTTONUP and event.button==1: # 2 boutons qui mène vers aide et crédits
                if 126<event.pos[1]<230 and 75<event.pos[0]<250 or (event.type==KEYDOWN and event.key==K_F1):
                    continuer_menu=0
                    nbjoueurs=0

                if 126<event.pos[1]<230 and 1300<event.pos[0]<1500 or (event.type==KEYDOWN and event.key==K_F5):
                    continuer_menu=0
                    continuer_aide=0

    if nbjoueurs!=0: # histoire que ca se lance pas si le joueur quitte.
        creationperso(nbjoueurs) # on créé n joueurs (joueur1,joueur2,...)
        choixcartes(nbjoueurs) # constitution d'un deck de cartes trésors pour chaque joueur

    page_actuelle=2 # on veut commencer avec la page1 (lire la suite pour comprendre)
    while continuer_aide: # Le menu d'aide, qui consiste en 2 pages entre lesquelles on peut alterner librement
        imageaide1=pygame.image.load('imageaide1.jpg')
        imageaide2=pygame.image.load("imageaide2.jpg")
        if page_actuelle==2: # logique pas evidente ici mais ca marche
            fenetre.blit(imageaide1,(0,0))
        if page_actuelle==1:
            fenetre.blit(imageaide2,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type==MOUSEBUTTONUP and event.button==1:
                if 0<event.pos[0]<300 and 0<event.pos[1]<300: # A COMPLETER : BOUTON RETOUR MENU
                    continuer_aide=0
                    continuer_jeu=0
                    continuer_credits=0

                elif 0<event.pos[0]<1500 and 600<event.pos[1]<900: # A COMPLETER : OUVERTURE DE LA PAGE 2
                # on swap entre les pages, si on est sur la page1, on colle la 2 et viceversa
                    if page_actuelle== 2:
                        fenetre.blit(imageaide1,(0,0))
                        pygame.display.flip()
                        page_actuelle=1
                    elif page_actuelle==1:
                        fenetre.blit(imageaide2,(0,0))
                        pygame.display.flip()
                        page_actuelle=2

    while continuer_credits: # une boucle tres simple avec un blit d'image et un petit bouton de sortie
        imagecredits=pygame.image.load("imagecredits.jpg")
        fenetre.blit(imagecredits,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
                continuer_jeu=0
                continuer_credits=0
                pygame.display.quit()
                pygame.quit()
            if event.type==MOUSEBUTTONUP and event.button==1:
                if 0<event.pos[0]<300 and 0<event.pos[1]<300: # A COMPLETER : BOUTON RETOUR MENU
                    continuer_aide=0
                    continuer_jeu=0
                    continuer_credits=0

    run_once=0;run_once2=0;run_once3=0
    while continuer_jeu==1: # la boucle de jeu, accrochez vous
        global lastmove

        for event in pygame.event.get():
            if event.type==pygame.VIDEORESIZE:
                fenetre=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                fenetre.blit(pygame.transform.scale(bg,event.dict['size']),(0,0))
            if event.type==QUIT:
                continuer=0
                continuer_menu = 0
                continuer_jeu = 0
                print('oui')
                pygame.quit()
                pygame.display.quit()

        if run_once==0: # plein de choses qu'on a besoin de lancer qu'une seule fois
            grille=generation_grille() # le plateau est généré quand on lance la boucle de jeu
            collage_grille(grille)
            load_compteurtresor()
            fenetre.blit(bg,(0,0))
            affichage_compteurtresor4()
            fenetre.blit(imagelog,(900,300))
            bloc_actu()
            affichage_message("Bienvenue dans Labyrinthe !")
            affichage_message("Si vous prenez plus de 25 secondes pour jouer l'ordinateur s'autodetruira") # pietre tentative d'humour
            lastmove='0'# j'essaie d'implanter la regle qui fait que lorsqu'on joue a un endroit le joueur suivant ne peut pas refaire le meme coup dans l'autre sens
            run_once=1





        pygame.time.Clock().tick(30)


        for joueur in joueurs:
            """ce qui nous permet d'avoir des tours de jeu, c'est pratique ca loop les n joueurs a la suite. ca nous permet surtout de pouvoir appeler joueur.x ou y et que le joueur
            actuellement en train de joueur soit affecté
            """
            stopdepcartes = 1
            stopdepjoueur = 1
            affichage_compteurtresor()

            """ Il faut toutefois limiter ces petits chenapans de joueur, pour ne pas qu'il bouge plusieurs lignes. On a ainsi redivisé la boucle de jeu en 2 sous boucles pour chaque phase de jeu:
            la premiere boucle permettra au joueur de retourner la piece autant qu'il le souhaite et de bouger une ligne/colonne. Apres ca commence la 2e phase:
            2nde boucle, ou le joueur peut se déplacer a volonté, il validera sa position avec entrée et marquera ainsi la fin de son tour.
            """
            TEXTEVENT=USEREVENT+1 # c'est surement pas la meilleure méthode mais ca marche
            pygame.time.set_timer(TEXTEVENT,5000) # tout le texte que je veux mettre ne rentre pas au début. Du coup on fait qu'une partie ne s'affiche qu'apres 5sec
            while stopdepcartes==1:


                for event in pygame.event.get():
                    if event.type==TEXTEVENT and run_once3==0: # s'affiche au bout de 5sec mais seulement la premiere fois
                        affichage_message(' ') # saut de lignes
                        affichage_message('Regardez votre objectif en passant votre souris sur le dos de carte correspondant')
                        affichage_message(' ') # saut de lignes
                        affichage_message('Commencez par tourner votre piece en cliquant dessus puis deplacez une ligne ou colonne')
                        affichage_message('pour creer votre chemin')
                        run_once3=1

                    if event.type == QUIT:
                        stopdepcartes=0
                        continuer_jeu=0
                        continuer_menu = 0
                        continuer = 0
                        pygame.quit()
                        pygame.display.quit()

                    if event.type==MOUSEBUTTONUP and event.button==1:
                        if 1300<event.pos[0]<1400 and 500<event.pos[1]<600: # cliquer sur la piece provoque ainsi sa rotation
                            rotationpiece_out()

                        #on a donc plein de petites flèches sur lequelle le joueur peut cliquer pour faire bouger la ligne/colonne qu'il souhaite
                        elif event.pos[0] < 100 and 200< event.pos[1] < 300 and lastmove!='x-200':
                            deplacergaucheversdroite200()
                            stopdepcartes=0 # on arrete la boucle de deplacement de cartes pour entrer dans la phase de deplacement de pion
                            lastmove='x+200' # variable qui tient compte du dernier move joué, ainsi on teste a chaque fois si le coup précédent n'a pas été joué avant
                            # si celui-ci vient d'être joué, le coup contraire n'est pas autorisé

                        elif event.pos[0] < 100 and 400 < event.pos[1] < 500 and lastmove!='x-400':
                            deplacergaucheversdroite400()
                            stopdepcartes=0
                            lastmove='x+400'
                        elif event.pos[0] < 100 and 600 < event.pos[1] < 700 and lastmove!='x-600':
                            deplacergaucheversdroite600()
                            stopdepcartes=0
                            lastmove='x+600'
                        elif 800 < event.pos[0] < 900 and 200 < event.pos[1] < 300 and lastmove!='x+200':
                            deplacerdroiteversgauche200()
                            stopdepcartes=0
                            lastmove='x-200'
                        elif 800 < event.pos[0] < 900 and 400 < event.pos[1] < 500 and lastmove!='x+400':
                            deplacerdroiteversgauche400()
                            stopdepcartes=0
                            lastmove='x-400'
                        elif 800 < event.pos[0] < 900 and 600 < event.pos[1] < 700 and lastmove!='x+600':
                            deplacerdroiteversgauche600()
                            stopdepcartes=0
                            lastmove='x-600'
                        elif 200 < event.pos[0] < 300 and event.pos[1] < 100 and lastmove!='y-200':
                            deplacerhautversbas200()
                            lastmove='y+200'
                            stopdepcartes=0
                        elif 400 < event.pos[0] < 500 and event.pos[1] < 100 and lastmove!='y-400':
                            deplacerhautversbas400()
                            lastmove='y+400'
                            stopdepcartes=0
                        elif 600 < event.pos[0] < 700 and event.pos[1] < 100 and lastmove!='y-600':
                            deplacerhautversbas600()
                            lastmove='y+600'
                            stopdepcartes=0
                        elif 200 < event.pos[0] < 300 and event.pos[1] > 800 and lastmove!='y+200':
                            deplacerbasvershaut200()
                            lastmove='y-200'
                            stopdepcartes=0

                        elif 400 < event.pos[0] < 500 and event.pos[1] > 800 and lastmove!='y+400':
                            deplacerbasvershaut400()
                            lastmove='y-400'
                            stopdepcartes=0
                        elif 600 < event.pos[0] < 700 and event.pos[1] > 800 and lastmove!='y+600':
                            deplacerbasvershaut600()
                            lastmove='y-600'
                            stopdepcartes=0

                        bloc_actu()

                    if event.type==MOUSEMOTION:
                    #Le joueur doit toutefois voir quel est son objectif, mais dans une certaine intimité. Ainsi son trésor n'est révélé que si il passe sa souris dessus, autrement
                    #seul les dos de cartes sont affichés
                        overlap_cartes()
                    if event.type==KEYDOWN and event.key==K_ESCAPE:
                        continuer_jeu=0
                        stopdepcartes=0
                        stopdepjoueur=0
                        del liste_message[:] # on vide le log


            if run_once2==0:
                affichage_message('Deplacez maintenant votre personnage et finissez votre tour avec entree')
                run_once2=1

            while stopdepjoueur==1:

                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer=0
                        continuer_menu = 0
                        continuer_jeu = 0
                        pygame.quit()
                    if event.type==MOUSEMOTION:
                        overlap_cartes()
                    if event.type == KEYDOWN:
                        if event.key==K_ESCAPE:
                            continuer_jeu=0
                            stopdepjoueur=0
                            stopdepcartes=0
                            del liste_message[:] # on vide le log
                        if event.key == K_LEFT:
                            joueur.deplacer("gauche")
                        if event.key == K_RIGHT:
                            joueur.deplacer("droite")
                        if event.key == K_UP:
                            joueur.deplacer('haut')
                        if event.key == K_DOWN:
                            joueur.deplacer("bas")
                        if event.key == K_RETURN: # le joueur valide sa position et marque la fin de son tour
                            stopdepjoueur=0 # on met alors cette variable a 0
                            affichage_compteurtresor() # refresh du compteur instantané, dans le cas ou il viendrait d'obtenir un trésor


                            """S'en suit la manière d'acquisition d'un trésor et ce qu'elle entraîne
                            """
                            if  grille[(joueur.casey)-1][(joueur.casex)-1][4]==joueur.tresor_actif[0]: # si le trésor de la case sur laquelle se trouve correspond a son tresor actif

                                joueur.compteur_tresor+=1 # on incrémente le compteur
                                affichage_message(('{} a trouve le tresor {}').format(joueur.nomjoueur,joueur.tresor_actif[0])) # on envoie un message sur le log

                                if joueur.compteur_tresor<4: # list index out of range aka le demon
                                    joueur.tresor_actif[0]=joueur.tresors[joueur.compteur_tresor] # le trésor actif correspondant a l'élément d'index compteur tresor de la liste trésor
                                    joueur.tresor_actif[1]=pygame.image.load('cartes/'+str(joueur.tresors[joueur.compteur_tresor])+'.png') # on charge la nouvelle image
                                    joueur.tresor_actif[1]=pygame.transform.scale(joueur.tresor_actif[1],(125,192)) # on la rescale a la bonne dimension

                                else:
                                    affichage_message("vous avez trouve tous vos tresors, sortez du labyrinthe !")
                                    joueur.tresor_actif[0]=False
                                    joueur.tresor_actif[1]=dos_carte
                        bloc_actu()
                        affichage_compteurtresor()

            if joueur.compteur_tresor==4: # victoire du joueur : sortie du plateau lorsqu'il a trouvé 4 trésors
                if grille[(joueur.casey)-1][(joueur.casex)-1][0]==100: # si sa pos_y=100
                    if grille[(joueur.casey)-1][(joueur.casex)-1][1]==200 or 400 or 600: #si sa pos_x=200 ou 400 ou 600
                        if grille[(joueur.casey)-1][(joueur.casex)-1][2][0]==1: # si elle autorise le dep vers le haut
                            affichage_message(('{} est sorti du plateau avec ses tresors ! La partie est finie.').format(joueur.nomjoueur))
                            affichage_message('Appuyez sur echap pour revenir au menu')
                            for event in pygame.event.get():
                                if event.type==KEYDOWN and event.key==K_ESCAPE:
                                    continuer_jeu=0
                                    stopdepcartes=0
                                    stopdepjoueur=0
                                    del liste_message[:] # on vide le log

                elif grille[(joueur.casey)-1][(joueur.casex)-1][0]==200: # si sa pos_y=200
                    if (grille[(joueur.casey)-1][(joueur.casex)-1][1]==100 and grille[(joueur.casey)-1][(joueur.casex)-1][2][2]==1) or (grille[(joueur.casey)-1][(joueur.casex)-1][1]==700 and grille[(joueur.casey)-1][(joueur.casex)-1][2][3]==1): #=100 ou 700
                        affichage_message(('{} est sorti du plateau avec ses tresors ! La partie est finie.').format(joueur.nomjoueur))
                        affichage_message('Appuyez sur echap pour revenir au menu')
                        for event in pygame.event.get():
                            if event.type==KEYDOWN and event.key==K_ESCAPE:
                                continuer_jeu=0
                                stopdepcartes=0
                                stopdepjoueur=0
                                del liste_message[:] # on vide le log

                elif grille[(joueur.casey)-1][(joueur.casex)-1][0]==400:
                    if (grille[(joueur.casey)-1][(joueur.casex)-1][1]==100 and grille[(joueur.casey)-1][(joueur.casex)-1][2][2]==1) or (grille[(joueur.casey)-1][(joueur.casex)-1][1]==700 and grille[(joueur.casey)-1][(joueur.casex)-1][2][3]==1):
                        affichage_message(('{} est sorti du plateau avec ses tresors ! La partie est finie.').format(joueur.nomjoueur))
                        affichage_message('Appuyez sur echap pour revenir au menu')
                        for event in pygame.event.get():
                            if event.type==KEYDOWN and event.key==K_ESCAPE:
                                continuer_jeu=0
                                stopdepcartes=0
                                stopdepjoueur=0
                                del liste_message[:] # on vide le log

                elif grille[(joueur.casey)-1][(joueur.casex)-1][0]==600:
                    if (grille[(joueur.casey)-1][(joueur.casex)-1][1]==100 and grille[(joueur.casey)-1][(joueur.casex)-1][2][2]==1) or (grille[(joueur.casey)-1][(joueur.casex)-1][1]==700 and grille[(joueur.casey)-1][(joueur.casex)-1][2][3]==1):
                        affichage_message(('{} est sorti du plateau avec ses tresors ! La partie est finie.').format(joueur.nomjoueur))
                        affichage_message('Appuyez sur echap pour revenir au menu')
                        for event in pygame.event.get():
                            if event.type==KEYDOWN and event.key==K_ESCAPE:
                                continuer_jeu=0
                                stopdepcartes=0
                                stopdepjoueur=0
                                del liste_message[:] # on vide le log

                elif grille[(joueur.casey)-1][(joueur.casex)-1][0]==700: # si sa pos_y=700
                    if grille[(joueur.casey)-1][(joueur.casex)-1][1]==200 or 400 or 600: #si sa pos_x=200 ou 400 ou 600
                        if grille[(joueur.casey)-1][(joueur.casex)-1][2][1]==1: # si elle autorise le dep vers le bas
                            affichage_message(('{} est sorti du plateau avec ses tresors ! La partie est finie.').format(joueur.nomjoueur))
                            affichage_message('Appuyez sur echap pour revenir au menu')
                            for event in pygame.event.get():
                                if event.type==KEYDOWN and event.key==K_ESCAPE:
                                    continuer_jeu=0
                                    stopdepcartes=0
                                    stopdepjoueur=0
                                    del liste_message[:] # on vide le log
        bloc_actu()
