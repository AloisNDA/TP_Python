while True:
    n = int(input("Entrez un nombre entier :"))

    positif = 1
    negatif = 1

    if n == 0:
        print("Le nombre",n,"et pair")
    elif n > 0:
        positif = n
        if positif % 2 ==0:
            print("Le nombre",n,"est positif et pair")
        else:
            print("Le nombre",n,"est positif et impair")
    elif n < 0:
        negatif = n
        if negatif % 2 ==0:
            print("Le nombre",n,"est negatif et pair")
        else:
            print("Le nombre",n,"est negatif et impair")