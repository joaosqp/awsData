'''Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
import random 
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática:
mediana
media
valor_minimo 
valor_maximo 

Importante: Esperamos que você utilize as funções abaixo em seu código:
random
max
min
sum'''

import random
random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = min(random_list)
valor_maximo = max(random_list)

random_list.sort() 
tamanho = len(random_list)

if tamanho % 2 == 1:
    mediana = random_list[tamanho // 2]
else:
    mediana = (random_list[tamanho // 2 - 1] + random_list[tamanho // 2]) / 2

media = sum(random_list) / tamanho

print(f"Media: {media:.2f}, Mediana: {mediana:.1f}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
