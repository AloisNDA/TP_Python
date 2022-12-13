while True:
    user = input("Quelle boucle souhaitez-vous utilisez ?(répondez par for ou while) : ")
    if user == 'while':
        print("Nous allons éxécuter le programme avec la boucle while.")
        while True:
            n = int(input("Entrez une valeur supérieur à 0 : "))
            x = n
            f = n-1
            c = 0
            while n != 0:
                n *= f
                f -= 1
                c += 1
                print("Boucle While : ",c,n,f,)
                if f == 1:
                    print(f"La fractionnelle de {x} est {n}")
                    break
            break
    elif user == 'for':
        print("Nous allons éxécuter le programme avec la boucle for.")
        z = int(input("Entrez une valeur supérieur à 0 : "))
        y = z
        a = z-1
        for i in range(1,z):
            z *= a
            a -= 1
            print("Boucle For : ",i,z,a)
            if a == 1:
                print(f"La fractionnelle de {y} est {z}")    
                break
    else:
        print("Valeur introuvable, recommencez")
        
        
        






        