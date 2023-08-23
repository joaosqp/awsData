"""Leia o arquivo person.json, faça o parsing e imprima seu conteúdo."""

import json

arquivo = "person.json"

try:
    with open(arquivo, "r") as arquivo_lido:
        conteudo = arquivo_lido.read()
        data = json.loads(conteudo)
        print(data)
except IndexError:
    pass
