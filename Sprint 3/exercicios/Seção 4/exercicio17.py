'''Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'''


def dividirLista(listas):
    tamanho = len(listas) // 3

    parte1 = listas[:tamanho]
    parte2 = listas[tamanho:2*tamanho]
    parte3 = listas[2*tamanho:]

    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

p1, p2, p3 = dividirLista(lista)

print(p1, end="")
print(p2, end="")
print(p3)

