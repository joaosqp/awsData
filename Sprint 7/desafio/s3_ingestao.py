import boto3

chave_acesso_aws = 'AKIARTMJ3STNRAXPYP6H'
chave_secreta_aws = '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'
bucket_filmes = 'data-lake-do-joaosqp-filmes'
bucket_series = 'data-lake-do-joaosqp-series'
zona_raw = 'Raw'
diretorio_local = 'Local'
formato_dados = 'CSV'
ano_processamento = '2023'
mes_processamento = '10'
dia_processamento = '23'
nomes_arquivos = ['movies.csv', 'series.csv']


s3_filmes = boto3.client('s3', aws_access_key_id=chave_acesso_aws, aws_secret_access_key=chave_secreta_aws)
s3_series = boto3.client('s3', aws_access_key_id=chave_acesso_aws, aws_secret_access_key=chave_secreta_aws)


for nome_arquivo in nomes_arquivos:
    if "movies" in nome_arquivo:
        caminho_s3 = f'{bucket_filmes}/{zona_raw}/{diretorio_local}/{formato_dados}/Movies/{ano_processamento}/{mes_processamento}/{dia_processamento}/{nome_arquivo}'
        caminho_local = f'./movies.csv' 
        s3_filmes.upload_file(caminho_local, bucket_filmes, caminho_s3)
    elif "series" in nome_arquivo:
        caminho_s3 = f'{bucket_series}/{zona_raw}/{diretorio_local}/{formato_dados}/Series/{ano_processamento}/{mes_processamento}/{dia_processamento}/{nome_arquivo}'
        caminho_local = f'./series.csv'  
        s3_series.upload_file(caminho_local, bucket_series, caminho_s3)

print('Ingestão concluída com sucesso.')
