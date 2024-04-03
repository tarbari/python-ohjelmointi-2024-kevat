from pprint import pprint
from models import Fruit, Apple, Orange

data = []


def parse_line(line):
    parts = line.split(",")
    match parts[1]:
        case "Apple":
            return Apple(int(parts[0]), parts[1], int(parts[2]))
        case "Orange":
            return Orange(int(parts[0]), parts[1], int(parts[2]))

    return Fruit(int(parts[0]), parts[1], int(parts[2]))


def count_total():
    return sum([f.count for f in data])


def start():
    filepath = "data.csv"

    try:
        header_skipped = False
        with open(filepath, "r") as file:
            for line in file:
                if not header_skipped:
                    header_skipped = True
                    continue
                print(line.strip())
                data.append(parse_line(line.strip()))
    except FileNotFoundError:
        print("tiedostoa ei löytynyt")

    pprint(data)

    print(f"total: {count_total()}")

    # f = Fruit(1, "nimi", 123)
    f = Apple(1, "nimi", 123)
    print(f)


if __name__ == "__main__":
    start()
