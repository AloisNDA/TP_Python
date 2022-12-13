compteur = 0
a = 0
b = 0
c = 0

while True:
    n = int(input("Entrez une valeur comprise entre 0 et 20 : "))
    if 0<=n<=20:
        compteur += 1
        print(f"Vous êtes à {compteur}/10 chances")
        if n <10:
            a += 1
        if 9<n<15:
            b += 1
        if n > 14:
            c += 1
        if compteur == 10:
            print("Vous avez utilisez toutes vos chances.")
            print(f"Il y à {a} valeurs inférieur à 10, {b} entre 10 et 14 et {c} supérieur à 14")
            break
    else:
        print("Valeur incorect, recommencez.")

    

    

