# Kirjasto:

# Luodaan Kirjasto. 
# Meillä on Book ja Library luokat. 
# Book sisältää numeraalisen id:n, kirjan nimen, kirjailijan nimen, sivumäärän, genren ja onko kirja lainassa. 
# Aluksi Libraryyn tehdään __init__ funktiossa lista, johon lisätään vähintään viisi kirjaa. 
# Lisätään funktiot kirjan lainaamiselle ja palauttamiselle id:n avulla. 
# Lisäksi funktiot listaamaan kirjat erotellen lainassa olevat muista kirjoista.

# Mainissa pyöritetään while loopissa kyselyä, että mitä käyttäjä haluaa tehdä kunnes q eli quit.

# Bonus: Lisää kirjojen lisääminen Libraryyn. 

# Kirjasto luokka
class Library():
    def __init__(self) -> None:
        # Luodaan kirjat kirjaston __init__ sisällä
        self.books = [] 
        self.books.append(Book(1, "kirja_1", "Lasse", 123, "Tiede", False))
        self.books.append(Book(2, "kirja_2", "Erkki", 456, "Kauhu", False))
        self.books.append(Book(3, "kirja_3", "Mika", 789, "Fantasia", True))
        self.books.append(Book(4, "kirja_4", "Mari", 234, "Oppikirja", True))
        self.books.append(Book(5, "kirja_5", "Hannele", 345, "Draama", False))
    
    # Lainaus
    def loan_book(self, id):
        for book in self.books:
            if book.id == id:
                book.loaned = True
                print(f"Kirja nimeltä {book.name} lainattu...")

    # Palautus
    def return_book(self, id):
        for book in self.books:
            if book.id == id:
                book.loaned = False
                print(f"Kirja nimeltä {book.name} palautettu...")

    # Kirjojen listaus
    def book_list(self):
        print("Vapaat kirjat:")
        for book in self.books:
            if book.loaned == False:
                print(book)
        print("Lainatut kirjat:")
        for book in self.books:
            if book.loaned == True:
                print(book)
    
    def add_new_book(self, id, book_name, writer_name, page_amount, genre):
        self.books.append(Book(id, book_name, writer_name, page_amount, genre, False))
        print("Kirja lisätty...")

# Kirja luokka
class Book():

    # Kirjan tiedot
    def __init__(self, id, name, writer_name, page_amount, genre, loaned) -> None:
        self.id = id
        self.name = name
        self.writer_name = writer_name
        self.page_amount = page_amount
        self.genre = genre
        self.loaned = loaned
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.writer_name} {self.page_amount}"

if __name__ == "__main__":
    library = Library()
    user_input = ""
    while user_input != "q":
        print("q = Lopeta, 1 = Lainaa, 2 = Palauta, 3 = Kirjalista, 4 = Lisää uusi kirja")
        print("")
        user_input = input("")
        if user_input == "1":
            library.loan_book(int(input("Anna lainattavan kirjan id: ")))
        if user_input == "2":
            library.return_book(int(input("Anna palautettavan  kirjan id: ")))
        if user_input == "3":
            library.book_list()
        if user_input == "4":
            library.add_new_book(
                int(input("Kirjan id: ")),
                input("Kirjan nimi: "),
                input("Kirjalijan nimi: "),
                int(input("Sivujen määrä: ")),
                input("Genre: "), 
            )
        print("")
    print("Kiitos käynnistä...")
        