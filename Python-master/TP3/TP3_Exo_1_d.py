n = int(input("Entrez une valeur >1: "))
a = 0
b = 0

while n<=1:
    n = int(input("Ce n'est pas une valeur supérieur à 1, réessayer :"))

while b <= n:
    a += 1
    b += a
    print(a,b)
print("La valeur N max est : ",a-1)