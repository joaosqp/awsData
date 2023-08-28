'''Apresente o ator/atriz com maior número de filmes
 e a respectiva quantidade. 
 A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.'''


caminho = 'C:\\Users\\joao_\\Desktop\\Compass UOL\\awsData\\Sprint 3\\desafio\\actors.csv'

ator_maior = ""
mais_filmes = 0

with open(caminho, 'r') as arquivo:
    cabecalho = arquivo.readline().strip().split(",")
    indice_ator = cabecalho.index("Actor")
    indice_filme = cabecalho.index("Number of Movies")
    
    for linha in arquivo:
        colunas = linha.strip().split(",")
        nome = colunas[indice_ator]
        
        qtd_filmes_str = colunas[indice_filme].replace(" ", "").strip()
        
        # Verifica se a string qtd_filmes_str contém apenas dígitos numéricos
        if qtd_filmes_str.isdigit():
            # Converte a string para um número inteiro
            qtd_filmes = int(qtd_filmes_str)

            if qtd_filmes > mais_filmes: 
                ator_maior = nome  
                mais_filmes = qtd_filmes

print(f'{ator_maior}: {mais_filmes} filmes.')
