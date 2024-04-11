import random
import sys

def lotto_gen() -> set[int]:
    # Samplelle annetaan populaatio, josta arvot otetaan ja kuinka monta arvoa sieltä otetaan. Tehdään tästä set.
    return set(random.sample(range(1,41), 7))

def test_lotto_gen(line: set[int]) -> bool:
    # Koska kyseessä on set, niin ei ole tarvetta testata arvojen uniikkiutta
    if len(line) == 7 and max(line) < 41 and min(line) > 0:
        return True
    return False

if __name__ == "__main__":
    # Testataan tämä useampaan kertaan, koska mukana on satunnaisuutta
    for i in range(100000):
        line = lotto_gen()
        if not test_lotto_gen(line):
            print(f"Testi {i} epäonnistui!")
            print(line)
            sys.exit(1)
    print("Kaikki testit onnistuivat")
