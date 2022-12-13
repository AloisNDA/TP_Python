base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
convives = int(input("Nombres d'inviter :"))

Nfromage = convives*fromage / base
Neau = convives*eau / base
Nail = convives*ail / base
Npain = convives*pain /base

print("La quantité d'ingrédient pour",convives,"convives est :","\n","-", Nfromage,"gr de fromage","\n","-", Neau,"dl d'eau","\n","-", Nail,"gousse(s) d'ail","\n","-", Npain,"gr de pain")