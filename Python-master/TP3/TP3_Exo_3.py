from random import*
from time import*

x = randint(0,100)
compteur = 0
n = -1

print("Bienvenu dans ce jeu du nombre mystère !")
print("Le but est simple, deviner la valeur comprise entre 0 et 100")
print("Bonne chance !")

sleep(1)

while n != x:
    n = int(input("Votre premier choix : "))
    if n>=0 and n<=100:
        compteur += 1
        if n>x:
            print("C'est moin !")
        elif n<x:
            print("C'est plus !")
        elif n == x:
            print("Bien jouer !")
            print(f"Tu as mis {compteur} tour(s) pour trouver, Bravo !")
    else:
        print("Valeur indisponible, recommencez.")
    
    

