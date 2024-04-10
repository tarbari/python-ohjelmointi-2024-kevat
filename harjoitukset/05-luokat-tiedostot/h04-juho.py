import random


def generate_lotto():
    # luodaan sallitut numerot
    nums = list(range(1, 41))

    # sekoitetaan luodut numerot
    random.shuffle(nums)

    # valitaan lottoriviin 7 ensimmäistä
    line = nums[:7]

    return line


def check_lotto(line):
    # pituus 7 ja uniikkeja lukuja
    if len(set(line)) != 7:
        return False

    if min(line) < 1 or max(line) > 40:
        return False

    return True


line = generate_lotto()
print(line)
print(f"laillinen rivi: {check_lotto(line)}")

# testejä riveille

# laillinen
line = [1, 2, 3, 4, 5, 6, 7]
print(f"pitäisi olla true: {check_lotto(line)}")

# lyhyt
line = [1, 2, 3, 4, 5, 6]
print(f"pitäisi olla false: {check_lotto(line)}")

# pitkä
line = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"pitäisi olla false: {check_lotto(line)}")

# liian pieni arvo
line = [0, 2, 3, 4, 5, 6, 7]
print(f"pitäisi olla false: {check_lotto(line)}")

# liian suuri arvo
line = [1, 2, 3, 4, 5, 6, 41]
print(f"pitäisi olla false: {check_lotto(line)}")
