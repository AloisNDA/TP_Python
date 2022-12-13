nMax = 3
v1 = []
v2 = []
produit = 0

while True:
    n = int(input("Tailles de vos vecteurs : "))
    if 0<n<=nMax:
        print("Saisie du premier vecteur :")
        v1.append(int(input("v1 [0] = ")))
        v1.append(int(input("v1 [1] = ")))
        v1.append(int(input("v1 [2] = ")))
        print("Saisie du deuxième vecteur :")
        v2.append(int(input("v1 [0] = ")))
        v2.append(int(input("v1 [1] = ")))
        v2.append(int(input("v1 [2] = ")))

        produit = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
        break
    else:
        print("Valeur invalide...")
print(produit)

