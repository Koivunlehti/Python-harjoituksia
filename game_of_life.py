# Haaste:

# Tehdään Conwayn Game of Life Pythonilla.

# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import random
import time

def tulosta(elinalue:list) -> None: # Tulosteaan elinalue terminaaliin
    for rivi in elinalue:
        for solu in rivi:
            print(solu, end=" ")
        print()

def alusta(koko:int) -> list:   # Alustetaan elinalue
    elinalue = []
    for i in range(koko):
        solut = []
        for j in range(koko):
            if random.randint(0,1):
                solut.append("O")
            else:
                solut.append(" ")
        elinalue.append(solut)
    return elinalue

def tarkista_naapurit(elinalue:list, y:int, x:int) -> int: # Tarkistetaan miten solujen naapurit voivat
    elavat = 0

    # Naapurit käydään läpi solun ympäriltä
    for i in range(y - 1, y + 2, 1):
        for j in range(x - 1, x + 2, 1):
            # Rajan tarkistuksia
            if j < 0 or j > len(elinalue) - 1:
                continue
            if i < 0 or i > len(elinalue) - 1:
                continue
            # Solu itse ei voi olla oma naapurinsa joten se ohitetaan.
            if i == y and j == x:
                continue
            # Jos naapuri on elossa, lisätään eläviä
            if elinalue[i][j] == "O":
                elavat += 1
    
    return elavat

def ela(elinalue:list) -> list: # Edetään solujen elämässä
    uusi_elinalue = []

    # rivit
    for i in range(len(elinalue)):
        # rivin solut
        solut = []
        for j in range(len(elinalue)): 
            elavat_naapurit = 0
            x = j
            y = i      

            elavat_naapurit = tarkista_naapurit(elinalue, y, x)

            # Säännöt
            if elinalue[i][j] == "O":
                # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                if elavat_naapurit < 2:
                    solut.append(" ")
                # Any live cell with two or three live neighbours lives on to the next generation.
                if elavat_naapurit == 2 or elavat_naapurit == 3:
                    solut.append("O")
                # Any live cell with more than three live neighbours dies, as if by overpopulation.
                if elavat_naapurit > 3:
                    solut.append(" ")
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            else:
                if elavat_naapurit == 3:
                    solut.append("O")
                else:
                    solut.append(" ")

        uusi_elinalue.append(solut)

    return uusi_elinalue

def vertaa_elinalueita(edellinen:list, nykyinen:list) -> bool:    # Verrataan, onko elinalue muuttunut viime kerrasta
    sama = False
    for i in range(len(edellinen)):
        for j in range(len(edellinen)):
            if edellinen[i][j] == nykyinen[i][j]:
                sama = True
            else:
                return False
            
    return sama

if __name__ == "__main__":
    # Käyttäjän syötteet
    koko = int(input("Anna alueen koko: "))
    kierros_maara = int(input("Anna kierrosten määrä: "))

    # Alustetaan elinalue
    elinalue = alusta(koko)
    edellinen_elinalue = []

    # Aloitetaan elämän kierto
    for i in range(kierros_maara):
        tulosta(elinalue)

        elinalue = ela(elinalue)
        print(f"{koko * '--'} Kierros: {i + 1}")

        time.sleep(0.2)

        # Katkaistaan silmukka kun / jos elinalue ei enää muutu
        if vertaa_elinalueita(edellinen_elinalue,elinalue):
            print()
            print("Elinalueen solut eivät muutu enää.")
            break
        else:
            edellinen_elinalue = elinalue