try:
    number = int(input("Anna kokonaisluku: "))
except ValueError as e:
    print("Syötetty arvo ei ollut kokonaisluku")
    print(e)
