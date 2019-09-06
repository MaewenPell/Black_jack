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
    """Genere le nom des joueurs et du Croupier et les ajoutent à la liste joueur """

    print("\t **** Interface de création des joueurs \t ****")
    print()
    print("\t Le Croupier sera créé automatiquement après les joueurs")
    print()

    for i in range (n): #On à une place en moins car il y a le Croupier
        print("\t **** Création du joueur numéro ", i+1, "\t****")
        print()
        nom = input("\t Entrez le nom du joueur : ")
        print()
        joueurs.append(nom)
        i+=1
    print("\t **** Fin de création des joueurs\t **** \n")

    nom = "Croupier"
    joueurs.append(nom)
    print("\t **** Note : le Croupier a bien été créé \t **** \n")

    print("****************************************************")
    print()

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
                print(players, " vous avez actuellement :", somme, "point(s) et vous avez piocher un as ! \n Suivant votre stratégie, vous voulez qu'il vaille 1 ou 11 points ?")
            somme = valeurCarte(carte) + somme
        scores[players] = somme
        somme = 0

        print(players, "a les cartes : \t", carte_en_main[players])

    return scores
    
def gagnant(scores,pot):
    """ """
    win = ""
    mini = 21
    for keys in scores: #On decompose chaque entrée dans scores
        valeur_main = scores[keys] #On recupere la valeur de la main dans le dico
        difference = 21 - valeur_main
        if difference < mini and difference >= 0:
            win = keys
            mini = difference
            score_partie = 21 - mini

    print("\tFin de cette partie ! \n\t Le gagnant est", win, "avec", score_partie,"points, vous remportez", pot, "et vous possédez maintenant", argent[win] + pot, "kopeks")
    
    print("\tChaque joueur possède : ")
    for j in argent:
        print("\t",j, ":", argent[j], "kopeks")
    return win, score_partie
   
def piocher():

    """On demande au joueur si il veut piocher, et on return True or False suivant la réponse"""

    choix = input("\tSouhaitez vous repiocher ? (o/n) ")
    print()
    
    while choix != "o" and choix != "n":
        print("Erreur, veuillez répondre par (o/n)")
        choix = input("souhaitez-vous repiocher ? (o/n) ")
    if choix == 'o' :
        return True
    elif choix == 'n':
        return False

def tourJoueur(j, pot = 0):

    print()
    print("\t **** Etat du joueur", j, " **** ")
    print()
    print("\t Score actuel de", j, ":", scores[j], "\n\t Argent actuel : ", argent[j], "Kopeks") #Etat

################################# MISE ############################################

    if j == "Croupier" : #ICi l'IA decide de se coucher ou de continuer à jouer

        choix_croupier = Croupier_PlusOuMoinsIntelligent() #True or False

        if choix_croupier: #Si l'algo à return True
            choix_miser = "miser"
        else:
            choix_miser = "coucher"

    else: #Partie non IA
        choix_miser = input("\t"+j+" souhaitez-vous miser ou vous coucher ? (miser/coucher) : ")

        while choix_miser != "miser" and choix_miser != "coucher":
            choix_miser = input("reponse incorrecte, souhaitez-vous miser ? (miser/coucher) : ")
    
    if choix_miser == 'miser':

        if j == "Croupier" : #Ici partie IA 
            print("\tLe croupier joue --> ") 
            mise_j = misecroupier() #Il decide automatiquement combien miser
            print("Il mise : ", mise_j)
        
        else : 
            mise_j = fct_mise(j) #On appel la fct_mise(j)
            print("\tVous avez choisi de miser", mise_j , "kopeks")

        argent[j] -= mise_j
        print("\tIl vous reste :",argent[j], "kopeks")
        pot += mise_j
        
    else:
        print("Vous vous couchez, au revoir")
        mise_j = 0
        joueurs.remove(j)

##################################### Partie PIOCHE ################################################

    if j in joueurs: #Si le j n'a pas été remove

        ###################### Partie Croupier ######################################################
    
        if j == "Croupier" : ####Est-ce que le croupier pioche ou pas #######

            if Croupier_PlusOuMoinsIntelligent():
                rep = True
            else :
                rep = False

        #############################################################################################
        
        else : 
            rep = piocher() #1- Appel pioche()

        if rep == True : #Si il veut repiocher
            new = piocheCarte(p)
            carte = new[0] 

            print("\t Vous avez pioché :", carte)
            if carte == "1 de pique" or carte == '1 de trefle' or carte == '1 de carreau' or carte == '1 de coeur':
                newval = None
                while newval != 1 and newval != 11 :
                    newval = int(input("\t Vous avez pioché un as ! \n\tSuivant votre stratégie, voulez-vous qu'il vaille 1 ou 11 points ?"))
            else :
                newval = valeurCarte(carte)

            scores[j] += newval #On calcule la nouvelle valeur de sa main 

            if scores[j] > 21 : #Il pioche et il depasse 21
                print("\t Après la pioche, votre nouveau score est de :", scores[j]," points")
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
    print("\t Actuellement le pot vaut ", pot, "Kopeks")
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


    mise = int(input("\t"+j+" combien souhaitez-vous miser ? "))

    while mise > argent[j]:
        print("Vous n'avez pas assez d'argent pour vous permettre cette mise, misez moins")
        mise = int(input("Combien souhaitez-vous miser ? "))
    while mise <= 0 :
                print("Vous devez obligatoirement miser plus de 0, n'essayez pas de tricher ;) ")
                mise = int(input("Combien souhaitez-vous miser ? "))

    return mise

def return_1_0():
    tirage = random.randint(0,1)
    if tirage == "0": #le Croupier décide de ne pas piocher 
        return False
    else:
        return True

#########################################
########### Partie Croupier #############
#########################################  

# def Croupier_aleatoire():
#     valchoix = random.randint(0,1)
#     if valchoix == "0": #le Croupier décide de ne pas piocher 
#         print("*******************************************")
#         print("Le ",valchoix, "est sorti donc il se couche")
#         print("*******************************************")
#         return False
#     else :
#         print("*******************************************")
#         print("Le ",valchoix, "est sorti donc il pioche")
#         print("*******************************************")
#         return True

# def Croupier_param(niveau = 0.8):
#     if niveau == "1": #le Croupier pioche tout le temps, ce grand fou
#         return True
#     elif niveau == "0": #le Croupier ne pioche jamais, ce froussard 
#         return False
#     elif niveau == 0.5 :
#         return return_1_0()
#     else:
#         n = random.uniform(0,1)
#         if n <= niveau : #Si le nombre généré est compris entre 0 et niveau
#             print("*******************************************")
#             print(n, "est sorti donc il pioche")
#             print("*******************************************")
#             return True 
        
def Croupier_PlusOuMoinsIntelligent():
    if scores['Croupier'] <= 10: #si le Croupier à une pioche inférieur ou égale à 10 il doit piocher car peu importe la carte qu'il va piocher il ne dépassera pas 21
        return True
    
    elif 10 < scores['Croupier'] <= 15: #si le Croupier à une pioche comprise entre 10 et 15, il doit piocher une carte d'une valeur maximal de 6, on cherche donc la proba d'avoir une carte > 6
        proba6 = random.randint(0,100) #on a 52 carte au total, 5 cartes par couleur on une valeur inférieur ou égale à 6, on à 4 couleur donc 4x5= 20, grossièrement on a 20/52 (environ 38%) de chance d'avoir une carte inférieur ou égale à 6 en piochant
        if proba6 >= 38:
            return True
        else:
            return False

    elif 15 < scores['Croupier'] <= 17:
        proba4 = random.randint(0,100) #on procéde de la même manière que pour la condition précédente, sauf qu'ici on doit avoir une carte de valeur max 4, donc 16/52 (30%)
        if proba4 >= 30:
            return True
        else:
            return False

    elif 17 < scores['Croupier'] <= 19:
        prob2 = random.randint(0,100) #on ne doit pas dépasser la valeur de 2, on a 8/52 (15%)
        if prob2 >= 15:
            return True
        else:
            return False
    
    elif 19 < scores['Croupier'] <= 20:
        proba1 = random.randint(0,100) #ici on a uniquement 4 cartes sur 52, 4/52 (7%)
        if proba1 >= 7:
            return True
        else:
            return False
    else: #Si il est à 21
        return False

def misecroupier():
    if scores['Croupier'] >= 20:
        mise = 100 #le croupier rentre en mode gambleur du seigneur, il all in

    elif 8 < scores['Croupier'] <= 13: 
        proba6 = random.randint(0,100) 
        if proba6 >= 38:
            mise = 10
        else:
            mise = 1
    
    elif 13 < scores['Croupier'] <= 15:
        proba4 = random.randint(0,100)
        if proba4 >= 30:
            mise = 30
        else:
            mise = 1
    
    elif 15 < scores['Croupier'] <= 17:
        proba4 = random.randint(0,100)
        if proba4 >= 15:
            mise = 60
        else:
            mise = 0
    
    elif 17 < scores['Croupier'] <= 19:
        proba4 = random.randint(0,100)
        if proba4 >= 10:
            mise = 80
        else:
            mise = 0
    
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
    n = int(input("Combien de joueurs vont affronter notre Croupier maison pour cette partie ? "))
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
