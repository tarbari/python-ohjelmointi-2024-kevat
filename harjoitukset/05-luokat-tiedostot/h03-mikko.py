sanat = []

while True:
    # Lisään rivivaihdon syötteeseen jo tässä vaiheessa. Se voitaisiin lisätä myös writelines metodissa.
    sanat.append(input("Syötä sana ('lopeta' lopettaa): ") + "\n") 

    # Muistetaan ottaa rivivaihto mukaan tarkistukseen.
    if sanat[-1] == "lopeta\n":
        sanat.pop() # .pop() ilman argumenttia palauttaa ja poistaa viimeisen elementin listassa.
        with open("tiedosto.txt", "w") as f:
            f.writelines(sanat)
        print(f"{len(sanat)} riviä kirjoitettu")
        break

