'''A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. 
Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. 
Considere a ordem decrescente e, em segundo nível, o nome do  filme.
Ao escrever no arquivo, considere o padrão de saída 
<sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset, adicionando um resultado a cada linha.'''

def contar_aparicoes(filme, linhas):
    if filme:
        if filme in linhas:
            linhas[filme] += 1
        else:
            linhas[filme] = 1

def ordenar_filmes(dic):
    ordenacao = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    return ordenacao


caminho = 'C:\\Users\\joao_\\Desktop\\Compass UOL\\awsData\\Sprint 3\\desafio\\actors.csv'

filmes_mais_aparicoes = {}

with open(caminho, 'r') as arquivo:
    cabecalho = arquivo.readline().strip().split(",")
    indice_ator = cabecalho.index("Actor")
    indice_filme = cabecalho.index("#1 Movie")
    
    for linha in arquivo:
        colunas = linha.strip().split(",")
        nome = colunas[indice_ator]
        filme = colunas[indice_filme]
        contar_aparicoes(filme, filmes_mais_aparicoes)


filmes_ordenados = ordenar_filmes(filmes_mais_aparicoes)

sequencia = 0
while sequencia < len(filmes_ordenados):
    filme, quantidade = filmes_ordenados[sequencia]
    print(f"{sequencia} - O filme '{filme}' aparece {quantidade} vez(es) no dataset")
    sequencia += 1

