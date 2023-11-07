import pandas as pd
import boto3
import os
import requests
import json
from datetime import date

# Função para obter informações do filme da API TMDB
def obter_informacoes_filme(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        data = resposta.json()
        orcamento = data.get('budget')
        receita = data.get('revenue')
        diretores = ', '.join([d['name'] for d in data.get('directors', [])])
        atores_principais = ', '.join([a['name'] for a in data.get('cast', [])])
        
        return {
            'ID': movie_id,
            'Orçamento': orcamento,
            'Receita': receita,
            'Diretores': diretores,
            'Atores Principais': atores_principais
        }
    else:
        return None

def lambda_handler(event, context):
    # Sua chave da API TMDB
    api_key = "429396332743d52589579ea586d4057a"

    # Sua chave de acesso da AWS
    chave_acesso_aws = 'AKIARTMJ3STNRAXPYP6H'
    chave_secreta_aws = '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'

    bucket = 'data-lake-do-joaosqp-filmes'
    caminho_s3 = 'data-lake-do-joaosqp-filmes/Raw/Local/CSV/Movies/2023/10/23/movies.csv'

    s3_client = boto3.client('s3', aws_access_key_id=chave_acesso_aws, aws_secret_access_key=chave_secreta_aws)
    objeto = s3_client.get_object(Bucket=bucket, Key=caminho_s3)
    df = pd.read_csv(objeto['Body'], sep="|")

    # Filtrar filmes de comédia
    comedy_movies = df['genero'].str.contains("Comedy")

    lista_filmes = []

    for movie_id in comedy_movies['id']:
        info_filme = obter_informacoes_filme(movie_id, api_key)
        if info_filme:
            lista_filmes.append(info_filme)

    base_path = 'data-lake-do-joaosqp-filmes/'
    minha_camada = 'RAW'
    minha_origem = 'TMDB'
    meu_formato = 'JSON'

    data_de_processamento = date.today().strftime('%Y/%m/%d')
    
    # Dividir os dados em lotes de 100 registros
    lotes = [lista_filmes[i:i + 100] for i in range(0, len(lista_filmes), 100)]

    # Gravar os lotes de dados em arquivos JSON no Amazon S3
    for i, lote in enumerate(lotes):
        arquivo_json = f'lote_{i}.json'
        path_s3 = f"{base_path}{minha_camada}/{minha_origem}/{meu_formato}/{data_de_processamento}/{arquivo_json}"
        
        with open(arquivo_json, 'w') as json_file:
            json.dump(lote, json_file)

        # Enviar o arquivo JSON para o Amazon S3
        s3 = boto3.client('s3', aws_access_key_id=chave_acesso_aws, aws_secret_access_key=chave_secreta_aws)
        s3.upload_file(arquivo_json, bucket, path_s3)

    return {
        'status code': 200,
        'body': json.dumps(f"Funcionou")
    }