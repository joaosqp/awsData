import random
import names

# Passo 3: Definir os parâmetros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar a lista de nomes únicos
aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = []

# Gerar a lista de nomes aleatórios com base nos nomes únicos
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Passo 5: Gerar um arquivo de texto
with open("nomes_aleatorios.txt", "w") as file:
    for nome in dados:
        file.write(f"{nome}\n")


