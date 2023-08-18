'''
Exercícios Parte 1
Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
'''

import datetime

nome = input()
idade = input()

idade = int(idade)

ano_hoje = datetime.datetime.now().year
centenario = ano_hoje + (100 - idade)

print(centenario)

