'''Exercícios Parte 1
Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range().'''



numero = 101

for numero in range(1, 101):
    count = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            count += 1

    if count == 2:
        print(numero)