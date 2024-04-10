import sys


peeps = []

try:
    with open("data.csv", "r") as f:
        # luetaan data sisään ja otetaan newlinet pois
        data = [l.strip() for l in f.readlines()]

        # tiputetaan otsikkorivit
        data = data[1:]

        # hajotaan luettu data tupleiksi (ja muutetaan age kokonaisluvuksi)
        peeps = [(l.split(",")[0], int(l.split(",")[1])) for l in data]
except FileNotFoundError as e:
    print(f"Tiedostoa {e.filename} ei löytynyt")
    sys.exit(1)

# print(peeps)

# etsitään pienin ja suurin datasta löytyvät iät
smallest_age = min([p[1] for p in peeps])
biggest_age = max([p[1] for p in peeps])

# print(smallest_age, biggest_age)

# kerätään nuorimmat
youngest = [p for p in peeps if p[1] == smallest_age]
print("nuorimmat: ")
print(youngest)

# kerätään vanhimmat
oldest = [p for p in peeps if p[1] == biggest_age]
print("vanhimmat: ")
print(oldest)

# Matt
matt_sum = sum([p[1] for p in peeps if p[0].split()[0] == "Matt"])
print(f"Mattien ikäsumma: {matt_sum}")
