animais = ["Raposa", "Golfinho", "Baleia", "Lobo", "Camelo", "Esquilo", "Tartaruga", "Polvo", "Calango", "Foca", "Capivara", "Canguru", "Coala", "Pardal", "Tigre", "Pinguim Imperador", "Arara", "Gato", "Morsa", "Urso"]

animais_ord = sorted(animais)

print(animais_ord)

with open("animais.csv", "w") as file:
    for animal in animais_ord:
        file.write(f"{animal}\n")