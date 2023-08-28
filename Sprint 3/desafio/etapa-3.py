'''Apresente o ator/atriz com a maior média de receita de bilheteria 
bruta por filme do conjunto de dados. 
Considere a coluna Avarage per Movie para fins de cálculo.'''

caminho = 'C:\\Users\\joao_\\Desktop\\Compass UOL\\awsData\\Sprint 3\\desafio\\actors.csv'

ator_bem_pago = ""
maior_media = 0

with open(caminho, 'r') as arquivo:
    cabecalho = arquivo.readline().strip().split(",")
    indice_ator = cabecalho.index("Actor")
    indice_media = cabecalho.index("Average per Movie")
    
    for linha in arquivo:
        colunas = linha.strip().split(",")
        nome = colunas[indice_ator]
        
        media_str = colunas[indice_media].replace(",", "").strip()
        
        if media_str.replace(".", "").isdigit():
            media = float(media_str)

            if media > maior_media:
                ator_bem_pago = nome
                maior_media = media

print(f'{ator_bem_pago}: R${maior_media:.2f}')
