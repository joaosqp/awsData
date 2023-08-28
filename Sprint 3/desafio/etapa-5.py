'''Apresente a lista dos atores ordenada pela receita bruta
 de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.
Ao escrever no arquivo, considere o padrão de saída
<nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.'''

caminho = 'C:\\Users\\joao_\\Desktop\\Compass UOL\\awsData\\Sprint 3\\desafio\\actors.csv'

# Cria um dicionário para armazenar a receita total bruta de cada ator
receita_ator = {}

with open(caminho, 'r') as arquivo:
    cabecalho = arquivo.readline().strip().split(",")
    indice_ator = cabecalho.index("Actor")
    indice_gross = cabecalho.index("Total Gross")
    
    for linha in arquivo:
        colunas = linha.strip().split(",")
        nome = colunas[indice_ator]
        gross_str = colunas[indice_gross].replace(",", "").strip()
        
        if gross_str.replace(".", "").isdigit():
            gross = float(gross_str)

            if nome in receita_ator:
                receita_ator[nome] += gross
            else:
                receita_ator[nome] = gross
        elif '"' in nome:
            nome = nome.replace('"', '')
            if nome in receita_ator:
                receita_ator[nome] += gross
            else:
                receita_ator[nome] = gross

atores_ordenados = sorted(receita_ator.items(), key=lambda x: x[1], reverse=True)

for ator, receita in atores_ordenados:
    print(f"{ator} - R${receita:.2f}")
