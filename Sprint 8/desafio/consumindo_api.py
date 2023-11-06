import pandas as pd
import boto3
import os
import requests
import json

# API e configurações
chave_acesso_aws = 'AKIARTMJ3STNRAXPYP6H'
chave_secreta_aws = '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'
chave_api = "429396332743d52589579ea586d4057a"
bucket = 'data-lake-do-joaosqp-filmes'
caminho_s3 = 'data-lake-do-joaosqp-filmes/Raw/Local/CSV/Movies/2023/10/23/movies.csv'

# Configuração das credenciais da AWS
os.environ['AWS_ACCESS_KEY_ID'] = chave_acesso_aws
os.environ['AWS_SECRET_ACCESS_KEY'] = chave_secreta_aws
base_url = "https://api.themoviedb.org/3"

# Defina as configurações e variáveis globais aqui, como você já fez

def obter_informacoes_adicionais_filme(filme_id):
    orcamento = "Informação não disponível"
    receita = "Informação não disponível"

    url_creditos = f"{base_url}/movie/{filme_id}/credits"
    parametros = {"api_key": chave_api}
    data_creditos = requests.get(url_creditos, params=parametros).json()

    diretores = [membro["name"] for membro in data_creditos["crew"] if membro["job"] == "Director"]
    atores_principais = [ator["name"] for ator in data_creditos["cast"] if ator["order"] in (0, 1, 2)]

    return orcamento, receita, diretores, atores_principais

# LEITURA CSV
s3_client = boto3.client('s3')
objeto = s3_client.get_object(Bucket=bucket, Key=caminho_s3)
df = pd.read_csv(objeto['Body'], sep="|")

# Filtrar filmes de comédia
comedy_movies = df[df['genero'] == 'comedy']

# Iterar sobre os filmes de comédia e obter informações
lista_filmes = []

for _, row in comedy_movies.iterrows():
    movie_id = row['id']
    orcamento, receita, diretores, atores_principais = obter_informacoes_adicionais_filme(movie_id)

    # Adicionar informações do filme à lista de filmes
    lista_filmes.append({
        'ID': movie_id,
        'Orçamento': orcamento,
        'Receita': receita,
        'Diretores': diretores,
        'Atores Principais': atores_principais
    })

# Dividir os dados em lotes de 100 registros
lotes = [lista_filmes[i:i + 100] for i in range(0, len(lista_filmes), 100)]

# Gravar os lotes de dados em arquivos JSON no Amazon S3
for i, lote in enumerate(lotes):
    arquivo_json = f'lote_{i}.json'
    path_s3 = f's3://{bucket}/data-lake-do-joaosqp-filmes/Tmdb/Json/2023/10/01/{arquivo_json}'

    with open(arquivo_json, 'w') as json_file:
        json.dump(lote, json_file)

    # Enviar o arquivo JSON para o Amazon S3
    s3 = boto3.client('s3')
    s3.upload_file(arquivo_json, bucket, path_s3)

# Exibir um print quando a operação for concluída
print("Operação de envio para o Amazon S3 concluída.")
