# HUOM! Vastaus olettaa, että kaikki nimet ovat uniikkeja. 
# Lähdin ajattelemaan tätä aluksi dictien kautta kunnes tajusin, että nimet eivät ole uniikkeja. 
# En sitten ruvennut muuttamaan ratkaisua, koska se nyt sattuu toimimaan annetun datan kanssa.
import sys

try:
    with open("data.csv") as f:
        # Lue rivit indeksistä 1 alkaen, poista ympäriltä ylimääräiset whitespacet, jaa jokainen rivi pilkun kohdalta (tästä tulee lista) ja tee näistä listoista lista
        persons_list = [l.strip().split(",") for l in f.readlines()[1:]] 
        # Käydään läpi persons_list ja otetaan jokaisesta listasta ensimmäinen arvo avaimeksi ja toinen arvo arvoksi
        persons = {person[0]: int(person[1]) for person in persons_list}
except FileNotFoundError as e:
    print(f"Tiedostoa {e.filename} ei löydy")
    sys.exit(1)

# Otetaan talteen pienin ja suurin ikä
# .values() palauttaa dictistä kaikki arvot listana
min_age = min(persons.values())
max_age = max(persons.values())

# Tulostetaan henkilö, mikäli ikä on maksimi tai minimi. 
# .items() palauttaa dictistä avain-arvo-parit tuplena. Tuplet voidaan hajoittaa kahteen muuttujaan.
for name, age in persons.items():
    if age == min_age or age == max_age:
        print(f"{name}: {age}")

# Tässä sama vähän villimpänä versiona. List comprehensionia voidaan siis käyttää for looppien sijaan lähes missä tahansa tilanteessa.
# [print(f"{name}: {age}") for name, age in persons.items() if age == min_age or age == max_age]
