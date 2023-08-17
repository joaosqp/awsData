'''
Exercícios Parte 1
Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
'''

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

ano_hoje = 2023
centenario = ano_hoje + (100 - idade)

print(nome + ", Você completará 100 anos de idade em:", centenario)