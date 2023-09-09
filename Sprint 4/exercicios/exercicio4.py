def calcular_valor_maximo(operadores, operandos) -> float:
    pares = zip(operadores, operandos)
    
    def aplicar_operacao(pares):
        operador, (a, b) = pares
        a = float(a)
        b = float(b)
        
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            return a / b
        else:
            return 0 
    
    resultados = list(map(aplicar_operacao, pares))
    max_valor = max(resultados)
    
    return max_valor

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

maximo = calcular_valor_maximo(operadores, operandos)

print(maximo)
