import random
#A GERER SI LE JOUEUR A 21 POINTS IL GAGNE 1.5 FOIS SA MISE DES LE DEBUT

def paquet():
    """Genere un paquet de 52 cartes"""
    couleur = ["pique","carreau","trefle","coeur"]
    figures = ["valet","dame","roi"]
    valeur= [1,2,3,4,5,6,7,8,9,10]
    deck = []
    for i in couleur :
        for j in valeur : 
            deck.append(str(j) + " de " +  str(i)) #valeur convertie en str + couleur(2 de pique)
        for k in figures:
            deck.append(k + " de " + i) #cas speciaux pour valet/dame.. 
    return deck

def initJoueurs(n):
    """Genere le nom des joueurs et les ajoutent à une liste"""

    print("\t **** Interface de création des joueurs\t ****")

    for i in range (n):
        print("\t **** Création du joueur numéro ", i+1, "\t ****")
        nom = input("\t Nom du joueur : ")
        print()
        joueurs.append(nom)
        i+=1
    print("\t **** Fin de création des joueurs\t **** \n")

    return joueurs

def valeurCarte(carte):
    """ Associe le nom de la carte "nom" avec la valeur associée dans la liste "valeur """

    nom = ['1 de pique', '2 de pique', '3 de pique', '4 de pique', '5 de pique', '6 de pique', '7 de pique', '8 de pique', '9 de pique', '10 de pique', 'valet de pique', 'dame de pique', 'roi de pique', '1 de carreau', '2 de carreau', '3 de carreau', '4 de carreau', '5 de carreau', '6 de carreau', '7 de carreau', '8 de carreau', '9 de carreau', '10 de carreau', 'valet de carreau', 'dame de carreau', 'roi de carreau', '1 de trefle', '2 de trefle', '3 de trefle', '4 de trefle', '5 de trefle', '6 de trefle', '7 de trefle','8 de trefle', '9 de trefle', '10 de trefle', 'valet de trefle', 'dame de trefle', 'roi de trefle', '1 de coeur', '2 de coeur', '3 de coeur', '4 de coeur', '5 de coeur', '6 de coeur', '7 de coeur', '8 de coeur', '9 de coeur', '10 de coeur', 'valet de coeur', 'dame de coeur', 'roi de coeur']

    valeur = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]

    for elem in nom:
        if elem == carte:
            if elem == "1 de pique" or elem == '1 de trefle' or elem == '1 de carreau' or elem == '1 de coeur':
                valeur_num = None
                while valeur_num != 1 and valeur_num != 11 :
                    valeur_num = int(input(""))
            else:
                index = nom.index(elem)
                valeur_num = valeur[index]
    return valeur_num

def initPioche(n): 
    """Cette fonction génère une pioche constituée de n paquets. On ajoute ces paquets dans notre liste "pioche" qu'on mélange ensuite avec suffle"""
    p = []
    i = 0
    while i < n:
        p = paquet() + p
        i+=1
    random.shuffle(p)
    return p

def initStatut(joueurs):
    """"On crée à partir de la liste de joueur un statut pour ceux ci qui vaut "o" par defaut si il veut repiocher sinon on le change en "n" """
    statut = {}
    rej = "o"
    for nom in joueurs:
        statut[nom] = rej
    return statut

def piocheCarte(p, x = 1):
    """On recupère les carte des indices[0 jusqu'a x], on les insère dans la liste cartePiochee et on les enlève de la liste initiale "p", on peut préciser combien de carte retirer de p avec le parametre x."""
    cartePiochees = p[0:x]
    del p[0:x]
    return cartePiochees

def initScore(joueurs, v = 0 ):
    """On créer un dictionnaire avec tout les nom qu'on à entré dans la fonction initJoueurs et on initialise leur score avec la valeur de v""" 
    scores = {}
    for nom in joueurs:
        scores[nom] = v 
    return scores

def premier_tour(joueurs):
    """ Génère le nombre de joueurs, et on genere un dictionnaire{joueurs : 0} , pour chaque joueur, on pioche deux cartes provenant de la pioche, on calcule la valeur de chaque carte de chaque joueurs, et on retourne le dico associé.   """
    

    carte_en_main = {}
    somme = 0
    initJoueurs(n)
    initPioche(n)
    init_Argent(joueurs)

    for players in joueurs :
        carte_en_main[players] = piocheCarte(p,2) #On pioche deux cartes

        for carte in carte_en_main[players] : #pour chaque carte dans la main du joueur
            if carte == "1 de pique" or carte == '1 de trefle' or carte == '1 de carreau' or carte == '1 de coeur':
                print(players, " vous avez actuellement :", somme, "point(s) et vous avez pioché un as ! \n Suivant votre stratégie, vous voulez qu'il vaille 1 ou 11 points ?")
            somme = valeurCarte(carte) + somme
        scores[players] = somme
        somme = 0

        print("Les joueurs possèdent les cartes suivantes : ")
        print(players, "a les cartes : \t", carte_en_main[players])

    return scores
    
def gagnant(scores,pot):
    """  """
    win = ""
    mini = 21
    for keys in scores: #On decompose chaque entrée dans scores
        valeur_main = scores[keys] #On recupere la valeur de la main dans le dico
        difference = 21 - valeur_main
        if difference < mini and difference >= 0:
            win = keys
            mini = difference
            score_partie = 21 - mini

    print("\tFin de cette partie ! \n\t Le gagnant est", win, "avec", score_partie," points, vous remportez", pot, "et vous possédez maintenant", argent[win] + pot, "kopeks")
    
    print("Les scores sont : ")
    for j in argent:
        print("Le joueur", j, "possède", argent[j], "kopeks")
    return win, score_partie


    

def piocher():

    """On demande au joueur s'il veut piocher, et on return True or False suivant la réponse"""

    choix = input("\tSouhaitez vous repiocher ? (o/n) ")
    print()
    while choix != "o" and choix != "n":
        print("Erreur, veuillez répondre par (o/n)")
        choix = input("souhaitez-vous repiocher ? (o/n) ")
    if choix == 'o': #Le joueur pioche
        return True
    elif choix == 'n':
        return False

def tourJoueur(j, pot = 0):

    print()
    print("\t **** Etat du joueur ", j, " **** ")
    print()
    print("\t Score actuel de", j, ":", scores[j], "\n\t Argent actuel : ", argent[j], "Kopeks") #Etat

    choix_miser = input(j + " souhaitez-vous miser ou vous coucher ? (miser/coucher) : ")

    while choix_miser != "miser" and choix_miser != "coucher":
        choix_miser = input("reponse incorrecte, souhaitez-vous miser ? (miser/coucher) : ")
    
    if choix_miser == 'miser':

        mise_j = fct_mise(j) #On appel la fct_mise(j)

        print("\t\nVous avez choisi de miser ", mise_j , "kopeks")

        argent[j] -= mise_j

        print("\tIl vous reste : ",argent[j], "kopeks")

        pot += mise_j
        
    else:
        print("Vous vous couchez, au revoir")
        mise_j = 0
        joueurs.remove(j)

    if j in joueurs:

        rep = piocher() #1- Appel pioche()

        if rep == True : #Si il veut repiocher
            new = piocheCarte(p)
            carte = new[0] 
            print("\t Vous avez pioché : ", carte)
            if carte == "1 de pique" or carte == '1 de trefle' or carte == '1 de carreau' or carte == '1 de coeur':
                newval = None
                while newval != 1 and newval != 11 :
                    newval = int(input("Vous avez pioché un as ! \n Suivant votre stratégie, vous voulez qu'il vaille 1 ou 11 points ?"))
            else :
                newval = valeurCarte(carte)
            scores[j] += newval #On calcule la nouvelle valeur de sa main 

            if scores[j] > 21 : #Il pioche et il depasse 21
                print("\t Après la pioche, votre nouveau score est de :", scores[j])
                print()
                print("\t Vous avez dépassé 21 points, vous avez donc perdu... \n\t Au revoir ! ;) ")
                joueurs.remove(j)
            
            elif scores[j] == 21:
                print("Vous êtes arrivé à 21, vous aurez gagné à la fin du tour ! ")
                
            else:
                print("\t Après la pioche, votre nouveau score est de :", scores[j])
                print()
        
        else: #Si il ne repioche pas
            print("\t Vous ne piochez pas, vous gardez votre main pour le tour suivant ! \n")
            print()
            statut[j] = 'n' #Ici le statut change de "o" pour repiocher à "n"
            #print("Debug : le statut acutel des joueurs est : ", statut)
    
    return mise_j #On return la mise pour incrementer le pot dans tour complet

def tourComplet(joueurs):
    pot = 0

    for j in joueurs:
        pot += tourJoueur(j)
    print("Le pot vaut", pot)
    print()

    return pot

def partieFinie(joueurs, scores): #Si partie finie return true 
    
    arret = 0

    for indiv in joueurs: #Si un joueur à un score de 21 
        if scores[indiv] == 21:
            print('Le joueur, ', indiv, 'a gagné avec 21 points')
            return True

    if len(joueurs) == 1 and scores[indiv] != 21: 
        # print("\tFélicitation ",joueurs[0], "Tu es le dernier en jeu tu as gagné")

        # print("Fin de la partie !")
        return True
    
    for player in joueurs:
        if statut[player] == "n":
            arret += 1 
    
    if arret == len(joueurs): 
        return True

def init_Argent(joueurs, kopeks = 100):

    """On crée 100 kopeks d'argent pour chaque joueurs"""
    argent_joueurs = {}
    for j in joueurs:
        argent_joueurs[j] = kopeks
    return argent_joueurs

def fct_mise(j):

    mise = int(input( j  + " combien souhaitez-vous miser ? "))

    while mise > argent[j]:
        print("Vous n'avez pas assez d'argent pour vous permettre cette mise, misez moins")
        mise = int(input("Combien souhaitez-vous miser ? "))
    while mise <= 0 :
                print("Vous devez obligatoirement miser plus de 0, n'essayez pas de tricher ;) ")
                mise = int(input("Combien souhaitez-vous miser ? "))
    
    return mise


#########################################
########### Initialisation ##############
#########################################   

joueurs = []
scores = {}
argent_joueurs = {}

########################################    
########Programme principal#############
########################################

print("\t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("\t ||||||                                                ||||||")
print("\t ||||||        Bienvenue dans Blackjack 2.0            ||||||")
print("\t ||||||                 But du jeu :                   ||||||")
print("\t ||||||  Etre le plus proche de 21 sans le dépasser    ||||||")
print("\t ||||||                                                ||||||")
print("\t ||||||             7 joueurs maximum !                ||||||")
print("\t ||||||                                                ||||||")
print("\t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print()

n = -1
while n > 7 or n < 1 :
    n = int(input("\t Combien de joueurs pour cette partie ? "))
    print()

newGame = True 

while newGame : 

    p = initPioche(n)
    premier_tour(joueurs)
    argent = init_Argent(joueurs)
    statut = initStatut(joueurs)
    pot = tourComplet(joueurs)


    while partieFinie(joueurs,scores) != True : #Deroulé d'une seule partie 
        tourComplet(joueurs)
        partieFinie(joueurs,scores)
    
    gagnant(scores,pot)

    rejouer = input("\tSouhaitez vous rejouer ? (oui/non)")
    if rejouer not in ("o", "O", "oui", "y", "Oui"):
        newGame = False

#Problème du rejouer ...

print()
print("\t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("\t ||||||                                                ||||||")
print("\t ||||||           Fin du jeu Blackjack 2.0             ||||||")
print("\t ||||||             Merci d'avoir joué !               ||||||")
print("\t ||||||                                                ||||||")
print("\t ||||||                 Credits :                      ||||||")
print("\t ||||||             Maewen et Nicolas                  ||||||")
print("\t ||||||                                                ||||||")
print("\t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
