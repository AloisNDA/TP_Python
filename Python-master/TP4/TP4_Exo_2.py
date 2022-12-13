from ast import literal_eval
from decimal import*
étudiant = int(input("Veuillez indiquez le nombre d'étudiants : "))
r = 0
notes = 0
liste_notes = []
liste_notesBis = []
rang = []
écart = 0
écart_liste = []
somme = 0
moyenne = 0

for i in range(1,étudiant+1):
    notes = literal_eval(input(f"Note de l'étudiant_{r+1} :"))
    if 0<=notes<=20: 
        r +=1
        rang.append(r)
        liste_notes.append(notes)
        liste_notesBis.append(notes)
    else:
        print("Note invalide...")
somme = sum(liste_notes)
moyenne = float(somme/étudiant)
print(f"La moyenne de classe est de {moyenne}/20")

for a in range(1,étudiant+1):
    écart = liste_notes[0]-moyenne
    écart_liste.append(écart)
    del(liste_notes[0])

print("Rang | Notes | écart à la moyenne de classe")
for z in range(1,étudiant+1):
    print(f"{rang[0]}    | {liste_notesBis[0]}    | {écart_liste[0]}")
    del(rang[0],liste_notesBis[0],écart_liste[0])