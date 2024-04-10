count = 0

with open("user_lines.txt", "w") as f:
    while True:
        line = input("sana: ")
        if line == "lopeta":
            break
        f.write(line + "\n")
        count += 1

print(f"{count} riviä kirjoitettu tiedostoon!")
