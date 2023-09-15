# Laskukone:

# Tehdään laskukone. Aluksi käyttäjä laittaa ensimmäisen numeron.
# Tämän jälkeen loopissa kysellään matemaattinen operaatio ja numero.
# Looppi loppuu ja lopullinen vastaus annetaan, kun käyttäjä vastaa "bye".
# Muista välitulos jokaisen loopin kerroksen välillä. Tee varsinainen 
# laskeminen erillisissä funktioissa. Vähintään lisääminen, vähentäminen,
# kertolasku ja jakolasku. Muitakin saa tehdä.


def plus(nykyinen_summa):
    luku = 0
    summa = nykyinen_summa
    try:
        luku = float(input(f"{nykyinen_summa} + "))
        summa += luku
    except:
        print("Virheellinen luku!")
    return summa

def miinus(nykyinen_summa):
    luku = 0
    summa = nykyinen_summa
    try:
        luku = float(input(f"{nykyinen_summa} - "))
        summa -= luku
    except:
        print("Virheellinen luku!")
    return summa
    
def kerto(nykyinen_summa):
    luku = 0
    summa = nykyinen_summa
    try:
        luku = float(input(f"{nykyinen_summa} * "))
        summa *= luku
    except:
        print("Virheellinen luku!")
    return summa

def jako(nykyinen_summa):
    luku = 0
    summa = nykyinen_summa
    try:
        luku = float(input(f"{nykyinen_summa} / "))
        summa /= luku
    except:
        print("Virheellinen luku!")
    return summa

def potenssi(nykyinen_summa):
    luku = 0
    summa = nykyinen_summa
    try:
        luku = float(input(f"{nykyinen_summa} ** "))
        summa **= luku
    except:
        print("Virheellinen luku!")
    return summa

if __name__ == "__main__":
    summa = 0
    # Käyttäjä syöttää numeron
    print("Tervetuloa laskimeen!")
    summa = input("Syötä ensimmäinen luku: ")

    try:
        summa = float(summa)
    except:
        summa = 0

    # Loop    
    while True:
       
        # Välitulos
        print()
        print(f"{summa}")
        print()
        print("Valitse operaatio:")
        print("+ = plus, - = vähennys, * = kerto, / = jako, bye tai q = lopeta")
        
        # Kysy matemaattinen operaatio ja numero
        syote = input()  
        match syote:
            case "+":
                summa = plus(summa)
            case "-":
                summa = miinus(summa)
            case "*":
                summa = kerto(summa)
            case "/":
                summa = jako(summa)
            case "**":
                summa = potenssi(summa)
            #case vastaus if syote == "bye" or syote == "q":
            case vastaus if syote in ["bye","q"]:
                # Lopeta loop
                print()
                print(f"Lopullinen tulos: {summa}")
                break
            case _:
                print(f"komentoa {syote} ei löydy!")