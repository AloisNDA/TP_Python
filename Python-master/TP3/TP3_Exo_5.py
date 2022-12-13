d = int(input("Donnez l’heure de début de la location (un entier) : "))
f = int(input("Donnez l’heure de fin de la location (un entier) : "))
temp_total = f-d
prix = 0
t1 = 0
t2 = 0
a = 0<=d<7 
b = 7<=d<17 or 7<=f<17
c = 17<=f<24

while True:
    if 0<=d<7 and 0<=f<7 or 17<=d<24 and 17<=f<24:
        prix = 1*temp_total
        print(f"Vous avez passer {temp_total} heure(s) au tarif horraire de 1.0 euro")
        
    elif 7<=d<17 and 7<=f<17:
        prix = 2*temp_total
        print(f"Vous avez passer {temp_total} heure(s) au tarif horraire de 2.0 euro")
        
    while a and b :
        t1 = 7-d
        t2 = f-7
        prix = (t1*1)+(t2*2)
        print(f"Vous avez passer {t1} heure(s) au tarif horraire de 1.0 euro")
        print(f"Vous avez passer {t2} heure(s) au tarif horraire de 2.0 euro")
        print(f"Le montant total à payer est de {prix} euro(s).")
        break
    while b and c :
        t1 = 17-d
        t2 = f-17
        prix = (t1*2)+(t2*1)
        print(f"Vous avez passer {t2} heure(s) au tarif horraire de 1.0 euro")
        print(f"Vous avez passer {t1} heure(s) au tarif horraire de 2.0 euro")
        print(f"Le montant total à payer est de {prix} euro(s).")
        break
    while a and c :
        t1 = 7-d
        t2 = f-17
        prix = (t1*1)+(t2*1)+(9*2)
        print(f"Vous avez passer {t1+t2} heure(s) au tarif horraire de 1.0 euro")
        print("Vous avez passer 9 heures au tarif horraire de 2.0 euro")                   
        print(f"Le montant total à payer est de {prix} euro(s).")
        break
    break