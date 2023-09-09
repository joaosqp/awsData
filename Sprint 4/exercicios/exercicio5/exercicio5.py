import csv

def calcular_maiores(notas):
    tres_maiores = sorted(notas, reverse=True)[:3]
    return tres_maiores

with open('estudantes.csv', 'r') as arquivo:
    reader = csv.reader(arquivo)

    resultados = []
    for linha in reader:
        nome = linha[0]
        notas = list(map(int, linha[1:]))
        maiores_notas = calcular_maiores(notas)
        media_maiores = round(sum(maiores_notas) / 3, 2)

        resultado = (nome, maiores_notas, media_maiores)
        resultados.append(resultado)

resultados = sorted(resultados, key=lambda x: x[0])

for resultado in resultados:
    nome, maiores_notas, media_maiores = resultado
    print(f"Nome: {nome} Notas: {maiores_notas} Média: {media_maiores}")
