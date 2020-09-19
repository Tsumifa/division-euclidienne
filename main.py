'''
Attention ! ce script ne marche que pour les entiers naturels. Je ne l'ai pas adapté pour les nombres négatifs et les nombres décimaux.
'''


'''
Initialisation des variables
'''

dividende_initial = int(input("Entrer un dividende : "))
dividende = dividende_initial # Je double les variables pour garder en mémoire la valeur initiale
diviseur_initial = int(input("Entrer un diviseur : "))
diviseur = 1 # Je double les variables pour garder en mémoire la valeur initiale ( = 1 parce que 0 * 10 = 0)
quotient = 0
rest = 0
loop = 1 # loop va déterminer la valeur à ajouter au quotient à chaque boucle

'''
Partie logique
'''

if diviseur_initial < 0 or dividende_initial < 0:
    print("Le script ne fonctionne que pour les entiers naturels")

elif dividende_initial < diviseur_initial: # Renvois un résultat évident
    print(dividende_initial, ' = 0 * ', diviseur_initial, " + ", dividende_initial)

elif dividende_initial == diviseur_initial: # Renvois un résultat évident
    print(dividende_initial, ' = 1 * ', diviseur_initial, " + 0")

elif diviseur_initial == 0:
    print("Is that a joke ?")

else:

    while dividende >= diviseur_initial:
        diviseur = diviseur_initial
        loop = 1

        if diviseur * 100 <= dividende: # Pour réduire rapidement le dividende

            while diviseur * 10 <= dividende:
                diviseur *= 10
                loop *= 10

        else: # Un peu plus lent mais c'est négligeable

            while diviseur <= dividende:
                dividende -= diviseur
                diviseur += diviseur
                loop += 1

        quotient += loop # je mets à jour la valeur du quotient avec le résultat de la boucle
        rest = dividende_initial - (diviseur_initial * quotient)
        dividende = rest # j'injecte la valeur ressortie après le passage dans la boucle

    print(dividende_initial, ' = ', quotient, ' * ', diviseur_initial, ' + ', rest)
