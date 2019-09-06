def croupier():
    if pioche >= 20:
        mise = "100" #le croupier rentre en mode gambleur du seigneur, il all in

elif 0 < pioche <= 8: 
        proba1 = random.randint(0,100) 
        if proba1 >= 70:
            fct_mise()
            mise = 0.2 * argent_joueurs("croupier")  #on mise 20% du bag au croupier
        elif proba1 >= 35:
            fct_mise()
            mise = 0.1 * argent_joueurs("croupier")  #sinon on mise 10% du bag
        elif proba1 >= 17:
            fct_mise()
            mise = 0.05 * argent_joueurs("croupier")  #sinon on mise 5% du bag

    elif 8 < pioche <= 13: 
        proba2 = random.randint(0,100) 
        if proba2 >= 50:
            fct_mise()
            mise = 0.4 * argent_joueurs("croupier")  #on mise 50% du bag au croupier
        elif proba2 >= 25:
            fct_mise()
            mise = 0.25 * argent_joueurs("croupier")  #sinon on mise 25% du bag
        elif proba2 >= 12:
            fct_mise()
            mise = 0.12 * argent_joueurs("croupier")  #sinon on mise 12% du bag
        
    
    elif 13 < pioche <= 15:
        proba3 = random.randint(0,100)
        if proba3 >= 30:
            fct_mise()
            mise = 0.6 * argent_joueurs("croupier") #60% du bag
        elif proba3 >= 15:
            fct_mise()
            mise = 0.3 * argent_joueurs("croupier")  #sinon on mise 30% du bag
        elif proba3 >= 7:
            fct_mise()
            mise = 0.15 * argent_joueurs("croupier")  #15%
    
    
    elif 15 < pioche <= 17:
        proba4 = random.randint(0,100)
        if proba4 >= 15:
            fct_mise()
            mise = 0.85 * argent_joueurs("croupier")  #on mise 85% du bag au croupier
        elif proba4 >= 8:
            fct_mise()
            mise = 0.42 * argent_joueurs("croupier")  #sinon on mise 42% du bag
        elif proba4 >= 4:
            fct_mise()
            mise = 0.21 * argent_joueurs("croupier")  #sinon on mise 21% du bag
            
    
    elif 17 < pioche <= 19:
        proba5 = random.randint(0,100)
        if proba5 >= 10:
            fct_mise()
            mise = 0.9 * argent_joueurs("croupier")  #on mise 90% du bag au croupier
        elif proba5 >= 5:
            fct_mise()
            mise = 0.45 * argent_joueurs("croupier")  #sinon on mise 45% du bag
        elif proba5 >= 2:
            fct_mise()
            mise = 0.22 * argent_joueurs("croupier")  #sinon on mise 22% du bag
