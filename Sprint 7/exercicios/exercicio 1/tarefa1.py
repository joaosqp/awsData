import pandas as pd


df = pd.read_csv('actors.csv')


Ator_num_filmes = df[df['Number of Movies'] == df['Number of Movies'].max()]['Actor'].values[0]
num_filmes = df['Number of Movies'].max()


media_filmes = df['Number of Movies'].mean()


ator_maior_media_filme = df[df['Average per Movie'] == df['Average per Movie'].max()]['Actor'].values[0]


filme_mais_frequente = df[df['Gross'] == df['Gross'].max()]['#1 Movie'].values[0]
frequencia_mais_alta = df['Gross'].max()


print("Ator com maior número de filmes:", Ator_num_filmes)
print("Número de filmes:", num_filmes)
print("Média da coluna:", media_filmes)
print("Ator com a maior média por filme:", ator_maior_media_filme)
print("Filme mais frequente:", filme_mais_frequente)
print("Frequência mais alta:", frequencia_mais_alta)
