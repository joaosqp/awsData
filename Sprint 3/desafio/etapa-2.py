'''Apresente a média de receita de bilheteria bruta dos principais filmes, 
considerando todos os atores. Estamos falando aqui da média da coluna Gross.'''

caminho = 'C:\\Users\\joao_\\Desktop\\Compass UOL\\awsData\\Sprint 3\\desafio\\actors.csv'

with open(caminho, 'r') as arquivo:
    cabecalho = arquivo.readline().strip().split(',')
    indice_gross = cabecalho.index("Gross")

    soma = 0
    count = 0

    for linha in arquivo:
        colunas = linha.strip().split(",")
        
        # Verifica se a coluna "Gross" está presente e contém um valor numérico
        gross_str = colunas[indice_gross]
        if gross_str.replace(".", "").isdigit():
            gross = float(gross_str)
            soma += gross
            count += 1

if count > 0:
    media = soma / count
    print(f"Media: R${media:.2f}")


