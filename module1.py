import random
from operator import itemgetter
import pygame
from pygame.locals import*

pygame.init()

fenetre=pygame.display.set_mode((1500,900),RESIZABLE)
bg=pygame.image.load('backg.jpg').convert()
icone = pygame.image.load('cases/3wayupdragon.png')
pygame.display.set_icon(icone)
pygame.display.set_caption('Labyrinthe')


'''YO YO YO
CA CREE UNE GRILLE AVEC DES CASES ALEATOIRES DE TYPE GRILLE=[[ligne1[position_possible_x,position_possible_y,case_x,case_y,tresor,[ah,ab,ag,ad],image],[ligne2]]
'''

def generation_grille():
    """ Grosse fonction qui va retourner la liste grille=[ligne1,ligne2,ligne3,....] avec ligne2=[case1,case2,case3,....] et case1=[pos_x,pos_y,[autoriseLeDeplacementVersLeHaut,bas,gauche,droite],ContientUnJoueur,NomDeLaPiece,CodePourCollage)
    16 pieces sont fixes, avec des x,y et direction fixes mais tous le reste est a une position aléatoire, et regarde dans une direction aléatoire. Toutefois les trésors sont toujours sur le même type de pièce et
    les 'proportions' de piece 2chemin/3chemin/coins sont toujours respectés. La fonction est lancé a chaque lancement de la boucle de jeu
    """
    global grille;global cases; global tresors

    position_possible_cases=[[200,100],[400,100],[600,100],[200,300],[400,300],[600,300],[200,500],[400,500],[600,500],[200,700],[400,700],[600,700],[1300,500]]
    for i in range(7):
        position_possible_cases.append([100+i*100,200])
        position_possible_cases.append([100+i*100,400])
        position_possible_cases.append([100+i*100,600]) # liste de toutes les positions possibles de pieces amovibles
    random.shuffle(position_possible_cases) # mélangé a chaque nouvelle partie pour des positions aléatoires


    # La fonction retourne 3 listes (listedirection2way,3way,corner) contenant des coordonnées de position à des positions aléatoires dans la liste
    direction2way=[[1,1,0,0],[0,0,1,1]] # HAUT BAS GAUCHE DROITE ; 1 AUTORISE, 0 BLOQUE
    listedirection2way=[]
    for x in range (12):
        x=random.choice(direction2way)
        listedirection2way.append(x)

    direction3way=[[1,0,1,1],[1,1,0,1],[0,1,1,1],[1,1,1,0]]
    listedirection3way=[]
    for x in range(6):
        x=random.choice(direction3way)
        listedirection3way.append(x)

    directioncorner=[[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
    listedirectioncorner=[]
    for x in range(16):
        x=random.choice(directioncorner)
        listedirectioncorner.append(x)

    '''Les 150 prochaines lignes créent les 34 pièces et les intègrent a la liste cases ; cases=[positionX,positionY,[autoriseHaut,autoriseBas,autoriseGauche,autoriseDroite],tresor ou pas,imageassocié.png]
         12 2chemins
         6 3chemins avec trésors
         6 coins avec trésors
         10 coins sans trésors
    '''
    cases=[]
    tresors=["fantome1","fantome2","couronne","dragon","epee","coffre","chauvesouris","scarabee","yeux","carte","grimoire","casque","bougeoire","anneau","emeraude","araignee","tetedemort","cles","sorciere","rat","lezard","sac","monstre","bouteille"]
    for x in range(12): # création de 12 pieces 2chemins
        ax=[]
        ax.append(position_possible_cases[x][0])
        ax.append(position_possible_cases[x][1])
        ax.append(listedirection2way[x])
        if listedirection2way[x][0]==1 and listedirection2way[x][1]==1: #equivaut a if listedirection2way=[1,1,0,0]
            ax.append("2wayvertical.png")
        elif listedirection2way[x]==[0,0,1,1]:
            ax.append("2wayhorizontal.png")
        cases.append(ax)

    for x in range(6): # 6 3 chemins
        ay=[]
        ay.append(position_possible_cases[12+x][0])
        ay.append(position_possible_cases[12+x][1])
        ay.append(listedirection3way[x])
        ay.append(tresors[x])
        if tresors[x]=="fantome1":
            if listedirection3way[x]==[1,0,1,1]:
                ay.append("3wayupfantome1.png")
            elif listedirection3way[x]==[0,1,1,1]:
                ay.append("3waydownfantome1.png")
            elif listedirection3way[x]==[1,1,0,1]:
                ay.append("3wayrightfantome1.png")
            else:
                ay.append("3wayleftfantome1.png")
        elif tresors[x]=="fantome2":
            if listedirection3way[x]==[1,0,1,1]:
                ay.append("3wayupfantome2.png")
            elif listedirection3way[x]==[0,1,1,1]:
                ay.append("3waydownfantome2.png")
            elif listedirection3way[x]==[1,1,0,1]:
                ay.append("3wayrightfantome2.png")
            else:
                ay.append("3wayleftfantome2.png")
        elif tresors[x]=="couronne":
            if listedirection3way[x]==[1,0,1,1]:
                ay.append("3wayupcouronne.png")
            elif listedirection3way[x]==[0,1,1,1]:
                ay.append("3waydowncouronne.png")
            elif listedirection3way[x]==[1,1,0,1]:
                ay.append("3wayrightcouronne.png")
            else:
                ay.append("3wayleftcouronne.png")
        elif tresors[x]=="dragon":
            if listedirection3way[x]==[1,0,1,1]:
                ay.append("3wayupdragon.png")
            elif listedirection3way[x]==[0,1,1,1]:
                ay.append("3waydowndragon.png")
            elif listedirection3way[x]==[1,1,0,1]:
                ay.append("3wayrightdragon.png")
            else:
                ay.append("3wayleftdragon.png")
        elif tresors[x]=="epee":
            if listedirection3way[x]==[1,0,1,1]:
                ay.append("3wayupepee.png")
            elif listedirection3way[x]==[0,1,1,1]:
                ay.append("3waydownepee.png")
            elif listedirection3way[x]==[1,1,0,1]:
                ay.append("3wayrightepee.png")
            else:
                ay.append("3wayleftepee.png")
        elif tresors[x]=="coffre":
            if listedirection3way[x]==[1,0,1,1]:
                ay.append("3wayupcoffre.png")
            elif listedirection3way[x]==[0,1,1,1]:
                ay.append("3waydowncoffre.png")
            elif listedirection3way[x]==[1,1,0,1]:
                ay.append("3wayrightcoffre.png")
            else:
                ay.append("3wayleftcoffre.png")
        cases.append(ay)

    for x in range(6): # 6 coins avec tresors
        az=[]
        az.append(position_possible_cases[x+18][0])
        az.append(position_possible_cases[x+18][1])
        az.append(listedirectioncorner[x])
        az.append(tresors[6+x])
        if tresors[6+x]=="chauvesouris":
            if listedirectioncorner[x]==[1,0,1,0]:
                az.append("cornerupleftchauvesouris.png")
            elif listedirectioncorner[x]==[1,0,0,1]:
                az.append("corneruprightchauvesouris.png")
            elif listedirectioncorner[x]==[0,1,1,0]:
                az.append("cornerdownleftchauvesouris.png")
            elif listedirectioncorner[x]==[0,1,0,1]:
                az.append("cornerdownrightchauvesouris.png")
        elif tresors[6+x]=="scarabee":
            if listedirectioncorner[x]==[1,0,1,0]:
                az.append("cornerupleftscarabee.png")
            elif listedirectioncorner[x]==[1,0,0,1]:
                az.append("corneruprightscarabee.png")
            elif listedirectioncorner[x]==[0,1,1,0]:
                az.append("cornerdownleftscarabee.png")
            elif listedirectioncorner[x]==[0,1,0,1]:
                az.append("cornerdownrightscarabee.png")
        elif tresors[6+x]=="yeux":
            if listedirectioncorner[x]==[1,0,1,0]:
                az.append("cornerupleftyeux.png")
            elif listedirectioncorner[x]==[1,0,0,1]:
                az.append("corneruprightyeux.png")
            elif listedirectioncorner[x]==[0,1,1,0]:
                az.append("cornerdownleftyeux.png")
            elif listedirectioncorner[x]==[0,1,0,1]:
                az.append("cornerdownrightyeux.png")
        elif tresors[6+x]=="carte":
            if listedirectioncorner[x]==[1,0,1,0]:
                az.append("cornerupleftcarte.png")
            elif listedirectioncorner[x]==[1,0,0,1]:
                az.append("corneruprightcarte.png")
            elif listedirectioncorner[x]==[0,1,1,0]:
                az.append("cornerdownleftcarte.png")
            elif listedirectioncorner[x]==[0,1,0,1]:
                az.append("cornerdownrightcarte.png")
        elif tresors[6+x]=="grimoire":
            if listedirectioncorner[x]==[1,0,1,0]:
                az.append("cornerupleftgrimoire.png")
            elif listedirectioncorner[x]==[1,0,0,1]:
                az.append("corneruprightgrimoire.png")
            elif listedirectioncorner[x]==[0,1,1,0]:
                az.append("cornerdownleftgrimoire.png")
            elif listedirectioncorner[x]==[0,1,0,1]:
                az.append("cornerdownrightgrimoire.png")
        elif tresors[6+x]=="casque":
            if listedirectioncorner[x]==[1,0,1,0]:
                az.append("cornerupleftcasque.png")
            elif listedirectioncorner[x]==[1,0,0,1]:
                az.append("corneruprightcasque.png")
            elif listedirectioncorner[x]==[0,1,1,0]:
                az.append("cornerdownleftcasque.png")
            elif listedirectioncorner[x]==[0,1,0,1]:
                az.append("cornerdownrightcasque.png")
        cases.append(az)
    for x in range(10): # 10 coins sans trésors
        av=[]
        av.append(position_possible_cases[x+24][0])
        av.append(position_possible_cases[x+24][1])
        av.append(listedirectioncorner[x+6])
        if listedirectioncorner[x+6]==[1,0,1,0]:
            av.append("cornerupleft.png")
        elif listedirectioncorner[x+6]==[1,0,0,1]:
            av.append("cornerupright.png")
        elif listedirectioncorner[x+6]==[0,1,1,0]:
            av.append("cornerdownleft.png")
        elif listedirectioncorner[x+6]==[0,1,0,1]:
            av.append("cornerdownright.png")
        cases.append(av)


    # bougeoire","anneau","emeraude","araignee","tetedemort","cles","sorciere","rat","lezard","sac","monstre","bouteille"

    # implantation des cases fixes

    ligne1=[[100,100,[0,1,0,1],'cornerdownright.png'],[300,100,[0,1,1,1],'bougeoire','3waydownbougeoire.png'],[500,100,[0,1,1,1],'anneau','3waydownanneau.png'],[700,100,[0,1,1,0],'cornerdownleft.png']]
    ligne2=[]
    ligne3=[[100,300,[1,1,0,1],'araignee','3wayrightaraignee.png'],[300,300,[1,1,0,1],'tetedemort','3wayrighttetedemort.png'],[500,300,[0,1,1,1],'cles','3waydowncles.png'],[700,300,[1,1,1,0],'sorciere','3wayleftsorciere.png']]
    ligne4=[]
    ligne5=[[100,500,[1,1,0,1],'rat','3wayrightrat.png'],[300,500,[1,0,1,1],'lezard','3wayuplezard.png'],[500,500,[1,1,1,0],'sac','3wayleftsac.png'],[700,500,[1,1,1,0],'emeraude','3wayleftemeraude.png']]
    ligne6=[]
    ligne7=[[100,700,[1,0,0,1],'cornerupright.png'],[300,700,[1,0,1,1],'monstre','3wayupmonstre.png'],[500,700,[1,0,1,1],'bouteille','3wayupbouteille.png'],[700,700,[1,0,1,0],'cornerupleft.png']]



    for i in range (len(cases)): # on place chaque case dans la ligne correspondante et les trie ensuite dans la ligne par leur position croissante de x grace a itemgetter
        if cases[i][1]==100:      # X=0 Y=1
            ligne1.append(cases[i])
            ligne1=sorted(ligne1, key=itemgetter(0))
        elif cases[i][1]==200:
            ligne2.append(cases[i])
            ligne2=sorted(ligne2, key=itemgetter(0))
        elif cases[i][1]==300:
            ligne3.append(cases[i])
            ligne3=sorted(ligne3, key=itemgetter(0))
        elif cases[i][1]==400:
            ligne4.append(cases[i])
            ligne4=sorted(ligne4, key=itemgetter(0))
        elif cases[i][1]==500:
            ligne5.append(cases[i])
            ligne5=sorted(ligne5, key=itemgetter(0))
        elif cases[i][1]==600:
            ligne6.append(cases[i])
            ligne6=sorted(ligne6, key=itemgetter(0))
        elif cases[i][1]==700:
            ligne7.append(cases[i])
            ligne7=sorted(ligne7, key=itemgetter(0))
        else:
            "j'ai foiré un truc"

    grille=[ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7]
    #cases=sorted(cases)


def collage_grille(grille):
    """Charge les images correspondantes au plateau précédemment aléatoirement généré
    On change aussi la facon dont sont codé les pièces: on rajoute ainsi le nom de la piece (ex:3waydowndragon.png) et le truc qu'on utilisera pour coller qui
    est placé en dernier element. On pourra ainsi facilement faire fenetre.blit(grille[ligne][case][-1],(grille[ligne][case][x],grille[ligne][case][y]))
    """
    global listenomcase # ca mange pas de pain
    listenomcase=[]
    for ligne in grille:
        for case in ligne:
            listenomcase.append(case[-1]) # on ajoute le dernier élément de la liste correspondant au nom de la case (pour chaque case dans chaque ligne)
    wutang=0
    for ligne in grille:
        for case in ligne:
            case.append(listenomcase[wutang]) # on ajoute le nom de la piece pour chaque case, pas indispensable mais ca aide a la lecture de la liste grille
            case[-1]=pygame.image.load('cases/'+str(listenomcase[wutang])) #on charge les images correspondant au nom précédemment ajouté a la case
            case.insert(3,0) # on rajoute aussi au case en 3e position l'attribut 'un perso est sur la case' avec 0=non et 1=oui
            wutang+=1

def affiche2(grille):
    """Juste la partie blit de affichagegrille, qui sera utilisé dans le refresh du plateau, car on ne peut pas load 2 fois la meme image"""
    for ligne in grille:
        for case in ligne:
          fenetre.blit(case[-1],(case[0],case[1]))
    pygame.display.flip()


def deplacergaucheversdroite200():
    """ le déplacement de la 2e ligne du plateau de gauche vers droite"""
    case_out=grille[4][-1] # on redéfinit que la case en dehors est la derniere case de la 5e ligne
    for i in range(20):
        for i in range(6):
            grille[1][i][0]+=5 # on augmente la variable pixel de 5 pour chaque case de la 2e ligne 20 fois, pour simuler un effet d'animation
            fenetre.blit(grille[1][i][-1],(grille[1][i][0],grille[1][i][1])) # on colle aux nouvelle positions
            pygame.display.flip() # toujours la, LE bg quoi
    for joueur in joueurs:
        if joueur.y==200: # si un joueur est sur la ligne au moment du déplacemnt
            if joueur.x==700: # si il est au bout de la ligne (x=700)
                joueur.x=100 # on le renvoie a la premiere case
                joueur.casex=int(joueur.x/100) # on précise bien int car la division par / renvoie un float (toujours update le px et la case)
            else: # si il n'est pas au bout
                joueur.x+=100 # on le pousse de 100px
                joueur.casex=int(joueur.x/100)
    case_out[0]=100 ; case_out[1]=200 # on définit les nouvelles positions de la case out, soit la premiere case de la 2e ligne
    grille[1].insert(0,case_out) #on insere case_out dans la ligne
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop() # on enleve case_out de la ligne5
    new_case_out=grille[1][-1] # la nouvelle case out est la derniere case de la ligne 2
    grille[4].append(new_case_out) # qu'on ajoute donc a la ligne5, ca pose pas de probleme sachant que la ligne5 est fixe
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[1].pop() # reste plus qu'a l'enlever vraiment de la ligne 2
    fenetre.blit(new_case_out[-1],(1300,500))
    pygame.display.flip()

def deplacergaucheversdroite400():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(6):
            grille[3][i][0]+=5 # [ligne2][cases][x]
            fenetre.blit(grille[3][i][-1],(grille[3][i][0],grille[3][i][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.y==400:
            if joueur.x==700:
                joueur.x=100
                joueur.casex=int(joueur.x/100)
            else:
                joueur.x+=100
                joueur.casex=int(joueur.x/100)
    case_out[0]=100
    case_out[1]=400
    grille[3].insert(0,case_out) #on insere case_out dans la ligne
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop() # on enleve case_out de la ligne5
    new_case_out=grille[3][-1] # derniere case de la ligne 2
    grille[4].append(new_case_out)
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[3].pop() # on enleve la derniere case de la ligne2
    fenetre.blit(new_case_out[-1],(1300,500))
    pygame.display.flip()

def deplacergaucheversdroite600():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(6):
            grille[5][i][0]+=5 # [ligne6][cases][x]
            fenetre.blit(grille[5][i][-1],(grille[5][i][0],grille[5][i][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.y==600:
            if joueur.x==700:
                joueur.x=100
                joueur.casex=int(joueur.x/100)
            else:
                joueur.x+=100
                joueur.casex=int(joueur.x/100)
    case_out[0]=100
    case_out[1]=600
    grille[5].insert(0,case_out) #on insere case_out dans la ligne
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop() # on enleve case_out de la ligne5
    new_case_out=grille[5][-1] # derniere case de la ligne6
    grille[4].append(new_case_out)
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[5].pop() # on enleve la derniere case de la ligne6
    fenetre.blit(new_case_out[-1],(1300,500))
    pygame.display.flip()

def deplacerdroiteversgauche200():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(1,7): # On ne prend pas la premiere qui sera new_case_out
            grille[1][i][0]-=5 # [ligne2][cases][x]
            fenetre.blit(grille[1][i][-1],(grille[1][i][0],grille[1][i][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.y==200:
            if joueur.x==100:
                joueur.x=700
                joueur.casex=int(joueur.x/100)
            else:
                joueur.x-=100
                joueur.casex=int(joueur.x/100)
    case_out[0]=700
    case_out[1]=200
    grille[1].append(case_out)
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[1][0]
    grille[4].append(new_case_out)
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[1].pop(0)
    fenetre.blit(new_case_out[-1],(1300,500))
    pygame.display.flip()

def deplacerdroiteversgauche400():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(1,7): # On ne prend pas la premiere qui sera new_case_out
            grille[3][i][0]-=5 # [ligne2][cases][x]
            fenetre.blit(grille[3][i][-1],(grille[3][i][0],grille[3][i][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.y==400:
            if joueur.x==100:
                joueur.x=700
                joueur.casex=int(joueur.x/100)
            else:
                joueur.x-=100
                joueur.casex=int(joueur.x/100)
    case_out[0]=700
    case_out[1]=400
    grille[3].append(case_out)
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[3][0]
    grille[4].append(new_case_out)
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[3].pop(0)
    fenetre.blit(new_case_out[-1],(1300,500))
    pygame.display.flip()

def deplacerdroiteversgauche600():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(1,7): # On ne prend pas la premiere qui sera new_case_out
            grille[5][i][0]-=5 # [ligne2][cases][x]
            fenetre.blit(grille[5][i][-1],(grille[5][i][0],grille[5][i][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.y==600:
            if joueur.x==100:
                joueur.x=700
                joueur.casex=int(joueur.x/100)
            else:
                joueur.x-=100
                joueur.casex=int(joueur.x/100)
    case_out[0]=700
    case_out[1]=600
    grille[5].append(case_out)
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[5][0]
    grille[4].append(new_case_out)
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[5].pop(0)
    fenetre.blit(new_case_out[-1],(1300,500))
    pygame.display.flip()

def deplacerhautversbas200():
    """ bouger les colonnes c'est un peu différent, sachant qu'on a codé la grille dans une logique de lignes ca simplifie pas la chose
    """
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(6):
            grille[i][1][1]+=5 # on augmente de 5 pixels pour la 2e case de chaque ligne (20 fois)
            fenetre.blit(grille[i][1][-1],(grille[i][1][0],grille[i][1][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.x==200:
            if joueur.y==700:
                joueur.y=100
                joueur.casey=int(joueur.y/100)
            else:
                joueur.y+=100
                joueur.casey=int(joueur.y/100)
    listecasetemp=[]
    for ligne in grille:
        listecasetemp.append(ligne[1]) # on crée ici une liste qui permettra de swap les valeurs, celle ci correspond a la 2e colonne
    case_out[0]=200
    case_out[1]=100
    grille[0][1]=case_out
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[6][1]
    new_case_out[0]=1300
    new_case_out[1]=500 # les changements classiques de case_out
    grille[4].append(new_case_out)
    fenetre.blit(new_case_out[-1],(new_case_out[0],new_case_out[1]))
    for i in range(1,7): # soit les 2e cases de la 2e a la 7e ligne, les changements ayant déja été effectués pour la premiere ligne
        grille[i][1]=listecasetemp[i-1] # la 2e case de la ligne1 devient la 2e case de la ligne2, jusqu'a la ligne7
    pygame.display.flip()

def deplacerhautversbas400():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(6):
            grille[i][3][1]+=5 #[lignes][case2][y]
            fenetre.blit(grille[i][3][-1],(grille[i][3][0],grille[i][3][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.x==400:
            if joueur.y==700:
                joueur.y=100
                joueur.casey=int(joueur.y/100)
            else:
                joueur.y+=100
                joueur.casey=int(joueur.y/100)
    listecasetemp=[]
    for ligne in grille:
        listecasetemp.append(ligne[3])
    case_out[0]=400
    case_out[1]=100
    grille[0][3]=case_out
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[6][3]
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[4].append(new_case_out)
    fenetre.blit(new_case_out[-1],(new_case_out[0],new_case_out[1]))
    for i in range(1,7):
        grille[i][3]=listecasetemp[i-1]
    pygame.display.flip()

def deplacerhautversbas600():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(6):
            grille[i][5][1]+=5 #[lignes][case2][y]
            fenetre.blit(grille[i][5][-1],(grille[i][5][0],grille[i][5][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.x==600:
            if joueur.y==700:
                joueur.y=100
                joueur.casey=int(joueur.y/100)
            else:
                joueur.y+=100
                joueur.casey=int(joueur.y/100)
    listecasetemp=[]
    for ligne in grille:
        listecasetemp.append(ligne[5])
    case_out[0]=600
    case_out[1]=100
    grille[0][5]=case_out
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[6][5]
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[4].append(new_case_out)
    fenetre.blit(new_case_out[-1],(new_case_out[0],new_case_out[1]))
    for i in range(1,7):
        grille[i][5]=listecasetemp[i-1]
    pygame.display.flip()

def deplacerbasvershaut200():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(1,7):
            grille[i][1][1]-=5
            fenetre.blit(grille[i][1][-1],(grille[i][1][0],grille[i][1][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.x==200:
            if joueur.y==100:
                joueur.y=700
                joueur.casey=int(joueur.y/100)
            else:
                joueur.y-=100
                joueur.casey=int(joueur.y/100)
    listecasetemp=[]
    for ligne in grille:
        listecasetemp.append(ligne[1])
    case_out[0]=200
    case_out[1]=700
    grille[6][1]=case_out
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[0][1]
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[4].append(new_case_out)
    fenetre.blit(new_case_out[-1],(new_case_out[0],new_case_out[1]))
    for i in range(6):
        grille[i][1]=listecasetemp[i+1]
    pygame.display.flip()

def deplacerbasvershaut400():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(1,7):
            grille[i][3][1]-=5
            fenetre.blit(grille[i][3][-1],(grille[i][3][0],grille[i][3][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.x==400:
            if joueur.y==100:
                joueur.y=700
                joueur.casey=int(joueur.y/100)
            else:
                joueur.y-=100
                joueur.casey=int(joueur.y/100)
    listecasetemp=[]
    for ligne in grille:
        listecasetemp.append(ligne[3])
    case_out[0]=400
    case_out[1]=700
    grille[6][3]=case_out
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[0][3]
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[4].append(new_case_out)
    fenetre.blit(new_case_out[-1],(new_case_out[0],new_case_out[1]))
    for i in range(6):
        grille[i][3]=listecasetemp[i+1]
    pygame.display.flip()

def deplacerbasvershaut600():
    case_out=grille[4][-1]
    for i in range(20):
        for i in range(1,7):
            grille[i][5][1]-=5
            fenetre.blit(grille[i][5][-1],(grille[i][5][0],grille[i][5][1]))
            pygame.display.flip()
    for joueur in joueurs:
        if joueur.x==600:
            if joueur.y==100:
                joueur.y=700
                joueur.casey=int(joueur.y/100)
            else:
                joueur.y-=100
                joueur.casey=int(joueur.x/100)
    listecasetemp=[]
    for ligne in grille:
        listecasetemp.append(ligne[5])
    case_out[0]=600
    case_out[1]=700
    grille[6][5]=case_out
    fenetre.blit(case_out[-1],(case_out[0],case_out[1]))
    pygame.display.flip()
    grille[4].pop()
    new_case_out=grille[0][5]
    new_case_out[0]=1300
    new_case_out[1]=500
    grille[4].append(new_case_out)
    fenetre.blit(new_case_out[-1],(new_case_out[0],new_case_out[1]))
    for i in range(6):
        grille[i][5]=listecasetemp[i+1]
    pygame.display.flip()


def rotationpiece_out():
    """ On change la direction de la piece en dehors du plateau, utilisé par les joueurs pour pousser une ligne/colonne. On doit donc changer le code de la piece et son image
    """
    direction3way=[[1,0,1,1],[1,1,0,1],[0,1,1,1],[1,1,1,0]] # position trié de 4 rotations a 90 degrés horaire
    directioncorner=[[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]] # pareil
    case_out=grille[4][-1] # on reprécise, surement inutile mais bon

    if case_out[-2]=='2wayvertical.png':
        case_out[-2]='2wayhorizontal.png' # on change le nom de la piece, aucun intéret au niveau du code mais une précaution si on a des problemes avec le plateau
        case_out[2]=[0,0,1,1] # correspond  a 2wayhorizontal, soit autorisant les déplacements vers droite et gauche
        case_out[-1]=pygame.transform.rotate(case_out[-1],90) # rotation visuelle de l'image 90deg horaire
    elif case_out[-2]=='2wayhorizontal.png':
        case_out[-2]='2wayvertical.png'
        case_out[2]=[1,1,0,0]
        case_out[-1]=pygame.transform.rotate(case_out[-1],90)

    elif sum(case_out[2])==3:

        if case_out[2]==direction3way[0]: # la liste est au début
            case_out[2]=direction3way[1]
            case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
            case_out[-2]=('3wayright'+str(case_out[4])+'.png') # tous les 3 chemins ont des trésors
        elif case_out[2]==direction3way[1]:
            case_out[2]=direction3way[2]
            case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
            case_out[-2]=('3waydown'+str(case_out[4])+'.png')
        elif case_out[2]==direction3way[2]:
            case_out[2]=direction3way[3]
            case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
            case_out[-2]=('3wayleft'+str(case_out[4])+'.png')
        elif case_out[2]==direction3way[3]:
            case_out[2]=direction3way[0]
            case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
            case_out[-2]=('3wayup'+str(case_out[4])+'.png')



    elif case_out[2]==directioncorner[0]:
        case_out[2]=directioncorner[1]
        case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
        if len(case_out)==7: # soit si la case contient un trésor
            case_out[-2]=('cornerdownright'+str(case_out[4])+'.png')
        else:
            case_out[-2]='cornerdownright.png'
    elif case_out[2]==directioncorner[1]:
        case_out[2]=directioncorner[2]
        case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
        if len(case_out)==7: # soit si la case contient un trésor
            case_out[-2]=('cornerdownleft'+str(case_out[4])+'.png')
        else:
            case_out[-2]='cornerdownleft.png'
    elif case_out[2]==directioncorner[2]:
        case_out[2]=directioncorner[3]
        case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
        if len(case_out)==7: # soit si la case contient un trésor
            case_out[-2]=('cornerupleft'+str(case_out[4])+'.png')
        else:
            case_out[-2]='cornerupleft.png'
    elif case_out[2]==directioncorner[3]:
        case_out[2]=directioncorner[0]
        case_out[-1]=pygame.transform.rotate(case_out[-1],-90)
        if len(case_out)==7: # soit si la case contient un trésor
            case_out[-2]=('cornerupright'+str(case_out[4])+'.png')
        else:
            case_out[-2]='cornerupright.png'



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
            liste_message.pop() # supprime le dernier element
        else: # soit 6, donc on rajoute 2 et pop 2
            liste_message.insert(0,message1) # ajoute le nouvel element en index 0
            liste_message.insert(0,message2)
            liste_message.pop();liste_message.pop() # supprime les 2 derniers éléments
    else:
        if len(liste_message)<6:
            liste_message.insert(0,message)
        else:
            liste_message.insert(0,message) # ajoute le nouvel element en index 0
            liste_message.pop() # supprime le dernier element

    textdisplay=pygame.font.Font('AtlantisInlineGrunge.ttf',20) # on créé l'élément de texte avec nos parametres de font / fontsize
    for message in liste_message: # on render chaque message dans la liste
        textSurface=textdisplay.render(message,True,(255,255,255))
        textRect = textSurface.get_rect(left=(905),y=440-i*25) # (axe y orienté vers le bas) on colle chaque message 25 pixels plus haut que le précédent
        fenetre.blit(textSurface,textRect)
        i+=1
    pygame.display.flip()



def affiche_cartes():
    """ ca colle du dos de carte en fonction du nombre de joueurs"""
    for i in range(nbjoueurs):
        fenetre.blit(dos_carte,(920+i*145,100)) # soit 920,1065,1210,1355 pour 4 joueurs

def bloc_actu(): #Ca correspond aux elements qu'on veut blit a peu pres tout le temps, on réaffiche les dos de carte, le plateau de jeu, les personnages en eux mêmes
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

def conditions_win():
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


def deplacements_plateau():
    global lastmove;global stopdepcartes
    #on a donc plein de petites flèches sur lequelle le joueur peut cliquer pour faire bouger la ligne/colonne qu'il souhaite
    if event.pos[0] < 100 and 200< event.pos[1] < 300 and lastmove!='x-200':
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


generation_grille()
#collage_grille(grille)
imagelog=pygame.image.load('imagelog.png')
liste_message=[]
dos_carte=pygame.image.load("cartes/dos_carte.png") # chargement du dos de carte. Je me sentais mal de faire une fonction pour juste ca


continuer=1
while continuer: # la boucle principale qui regroupera toutes les sous-boucles (menu, aide, crédits, jeu)

    imagemenu=pygame.image.load('imagemenu.jpg').convert()
    fenetre.blit(imagemenu,(0,0))
    pygame.display.flip()
    print(grille)

    continuer_menu = 1
    continuer_jeu = 1
    continuer_aide = 1
    continuer_credits = 1 # les 4 cavaliers de l'apocalypse
    nbjoueurs = 0

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

    images_aide=[0,0,0,0] # la liste des images d'aide qu'on va charger
    for i in range(4):
        images_aide[i]=pygame.image.load('imageaide'+str(i)+'.jpg') # on charge les 4 pages d'aide
    image_active=images_aide[0] # la variable qui contiendra la page sur laquelle le joueur est.
    while continuer_aide: # Le menu d'aide, qui consiste en 4 pages entre lesquelles on peut alterner librement
        fenetre.blit(image_active,(0,0)) # on colle la page sur laquelle le joueur est, cette variable sera modifié dans la boucle
        pygame.display.flip()
        loopbreak=1 # pour casser une boucle
        for event in pygame.event.get(): # toujours permettre au joueur de quitter
            if event.type==QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type==MOUSEBUTTONUP and event.button==1:
                if 1330<event.pos[0]<1400 and 80<event.pos[1]<140: # le joueur peut toujours revenir au menu a partir de n'importe quelle page
                    continuer_aide=0
                    continuer_jeu=0
                    continuer_credits=0

                elif 1225<event.pos[0]<1300 and 740<event.pos[1]<825: # on va vers la page a gauche
                    for x in range(1,4): # on teste les 3 pages possibles sur lequelle peut être le joueur et ou il peut aller vers la page précédente
                        # on ne peut aller a la page précédente que si on est sur la page2,3 ou 4 soit images_aide[1,2 ou 3] soit les valeurs de x.
                        if image_active==images_aide[x]:
                            image_active=images_aide[x-1] # si il est sur la page x, la nouvelle page_active est la page x-1

                elif 1325<event.pos[0]<1390 and 740<event.pos[1]<825: # on va vers la page a droite
                    for x in range(3): # ici on ne peut tourner la page qu'aux pages 1,2 et 3
                        if image_active==images_aide[x] and loopbreak==1: # on doit rajouter loopbreak car sinon a chaque valeur de x il changerait image_active or cela ne doit être fait qu'une seule fois
                            image_active=images_aide[x+1] # ici on augmente le x
                            loopbreak=0 # on arrete d'augmenter le x apres l'avoir fait une fois


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
                pygame.quit()
                pygame.display.quit()

        if run_once==0: # plein de choses qu'on a besoin de lancer qu'une seule fois
            generation_grille() # le plateau est généré quand on lance la boucle de jeu
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

                        deplacements_plateau()

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

            if joueur.compteur_tresor==4:
                conditions_win() # victoire du joueur : sortie du plateau lorsqu'il a trouvé 4 trésors

        bloc_actu()






