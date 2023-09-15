# Klassinen numeronarvauspeli

# Arvataan numeroa 1-100 väliltä. Peli laskee arvausten määrän. 
# Arvauksen jälkeen peli ilmoittaa, että oliko arvaus liian suuri 
# vai liian pieni. Jos arvaa 75 ja arvaus on liian suuri peli estää
# suuremman luvun arvaamisen ja sama liian pienelle. Peli estää 
# myös 1-100 ulkopuolelta arvaamisen sekä kirjaimet (string.isnumeric()). 
# Peli juhlii (päätä miten), kun arvaat oikein. 

import random

if __name__ == "__main__":
    arvattava_luku = random.randint(1,100)
    arvaus_min = 1
    arvaus_max = 100
    arvaus_maara = 0

    # pelilooppi
    while True:
        print(f"Luku on väliltä {arvaus_min}-{arvaus_max}")
        
        # käyttäjän syöte
        luku = input("Anna luku: ")

        # SYÖTTEEN TARKISTUSTA
        # Lopeta
        if luku == "q":
            break

        # Onko numeroita
        if luku.isnumeric() == False:
            print("Et antanut kokonaislukua!", end="\n\n")
            continue
        
        # Muutetaan kokonaisluvuksi
        luku = int(luku)

        # Onko 1-100
        if luku < 1 or luku > 100:
            print("Antamasi Luku ei ole väliltä 1-100!", end="\n\n")
            continue
        
        # ARVAUSTEN TARKISTUSTA
        # Estä arvattua suuremman tai pienemmän luvun syöttö
        if luku <= arvaus_min:
            print("Ei kannata arvata pienempää tai samaa kuin jo kerran arvattu!")
        elif luku >= arvaus_max:
            print("Ei kannata arvata suurempaa tai samaa kuin jo kerran arvattu!")
        else:
            # Onko liian suuri tai pieni
            if luku < arvattava_luku:
                print("Haetaan suurempaa lukua")
                arvaus_min = luku
            elif luku > arvattava_luku:
                print("Haetaan pienempää lukua")
                arvaus_max = luku
            else:
                print("Oikein! Jihuu!")
                print(f"Arvasit {arvaus_maara} kertaa väärin.")
                break

        # Laske arvausten määrää 
        arvaus_maara += 1
        print()