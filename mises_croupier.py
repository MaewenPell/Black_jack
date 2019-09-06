def croupier():
    if pioche >= 20:
        mise = "100" #le croupier rentre en mode gambleur du seigneur, il all in

    elif 8 < pioche <= 13: 
        proba6 = random.randint(0,100) 
        if proba6 >= 38:
            fct_mise()
            mise = "10"
        else:
            mise = "0"
    
    elif 13 < pioche <= 15:
        proba4 = random.randint(0,100)
        if proba4 >= 30:
            fct_mise()
            mise = "30"
        else:
            mise = "0"
    
    elif 15 < pioche <= 17:
        proba4 = random.randint(0,100)
        if proba4 >= 15:
            fct_mise()
            mise = "60"
        else:
            mise = "0"
    
    elif 17 < pioche <= 19:
        proba4 = random.randint(0,100)
        if proba4 >= 10:
            fct_mise()
            mise = "80"
        else:
            mise = "0"
