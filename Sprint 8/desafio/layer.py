import json
import os 
import requests

tmdb_api_chave = '429396332743d52589579ea586d4057a'
conta_id = '20621002'
endpoint = f'https://api.themoviedb.org/3/account/{conta_id}/rated/tv?api_key={tmdb_api_chave}'

resposta = requests.get(endpoint)
dados = resposta.json()

dados = dados.get('results', [])
tamanho_parte = 100

if not os.path.exists('testeJson'):
    os.makedirs('testeJson')

for i in range(0, len(dados), tamanho_parte):
    parte = dados[i:i + tamanho_parte]
    nome_arquivo = f'testeJson/dados_tmdb_{i // tamanho_parte}.json'
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(parte, arquivo_json, ensure_ascii=False, indent=4)

print('Arquivos JSON criados com sucesso!')
