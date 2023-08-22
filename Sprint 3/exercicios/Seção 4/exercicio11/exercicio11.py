'''Exercícios Parte 2
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e 
imprime o seu conteúdo.'''

# -*- coding: utf-8 -*-
 
arquivo = "arquivo_texto.txt"

try:
    with open(arquivo, "r") as arquivo_lido:
        conteudo = arquivo_lido.read()
        print(conteudo, end="")
except IndexError:
    pass
