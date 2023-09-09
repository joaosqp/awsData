'''E3
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 
Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools)
map'''

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    def calcular_cartao(saldo, cartao):
        valor, tipo = cartao
        if tipo == 'C':
            return saldo + valor
        else:
            return saldo - valor

    resultados = map(lambda cartao: calcular_cartao(0, cartao), lancamentos)
    saldo_final = reduce(lambda x, y: x + y, resultados)
    
    return saldo_final

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

saldo = calcula_saldo(lancamentos)
print(saldo)
