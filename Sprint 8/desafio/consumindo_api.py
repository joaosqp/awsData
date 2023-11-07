import pandas as pd
import boto3
import requests
import json
from datetime import date

# Aqui você vai colocar sua chave da API

def lambda_handler(event, context):
    
    api_key = '429396332743d52589579ea586d4057a'

    bucket = 'data-lake-do-joaosqp-filmes'
    caminho_s3 = 'data-lake-do-joaosqp-filmes/Raw/Local/CSV/Movies/2023/10/23/movies.csv'

    s3_client = boto3.client('s3')
    objeto = s3_client.get_object(Bucket=bucket, Key=caminho_s3)

    # Ler o arquivo do S3 diretamente em um DataFrame do Pandas
    df = pd.read_csv(objeto['Body'], sep="|", low_memory=False)

    # Continuação do seu código...
    # Filtrar por filmes de Comédia lançados após 2000
    data = df[(df['genero'].str.contains("Comedy")) & (df['anoLancamento'] > 2000)][['id', 'genero']].drop_duplicates()
    dataC = data.count()
    print(dataC)

    filmes = []

    for index, row in data.iterrows():
        id = row['id']
        url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
        resposta = requests.get(url)
        data = resposta.json()

        orcamento = data.get('budget')
        receita = data.get('revenue')

        if orcamento is not None and orcamento > 0 and receita is not None and receita > 0:
            filmes.append({'id': id, 'orcamento': orcamento, 'receita': receita})

        # Dividir os dados em lotes de 100 registros
        lotes = [filmes[i:i + 100] for i in range(0, len(filmes), 100)]

        # Destino no Amazon S3
        pasta_origem = 'data-lake-do-joaosqp-filmes'
        minha_camada = 'Raw'
        minha_origem = 'TMDB'
        meu_formato = 'JSON'
        today = date.today()
        data_de_processamento = today.strftime("%Y/%m/%d")

        s3 = boto3.client('s3')

        # Gravar os lotes de dados em arquivos JSON no Amazon S3
        for i, lote in enumerate(lotes):
            arquivo_json = f'lote_{i}.json'
            path_s3 = f"{pasta_origem}/{minha_camada}/{minha_origem}/{meu_formato}/{data_de_processamento}/{arquivo_json}"
            
            with open(arquivo_json, 'w') as json_file:
                json.dump(lote, json_file)

            # Enviar o arquivo JSON para o Amazon S3
            s3.upload_file(arquivo_json, bucket, path_s3)

        #Aqui é coisa do lambda, n mexe só apaga o comentario depois
        return {
            'status code': 200,
            'body': json.dumps(f"Funcionou")
        }
