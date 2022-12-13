import time

while True:
    n = int(input("Entrez un nombre n positif : "))
    time.sleep(0.5)
    print(n)
    time.sleep(0.5)
    while n>1:
        n -= 1
        print(n)
        time.sleep(0.5)
        if n == 1:
            print(0)
            time.sleep(0.5)
            print("Fin")
            break
    while n<1: 
        print("Valeur invalide, recommencez.")
        break
    break

x = int(input("Entrez un nombre n positif : "))
for _ in range(x):
    if x >0:
        print(x)
        x -= 1
        time.sleep(0.5)
        if x == 0:
            print(0)
            print("Fin")
            break
    else:
        print("valeur non-valide, réessayer")