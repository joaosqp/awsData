'''Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e 
retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:
x = 4 
y = 5
imprima:
Somando: 4+5 = 9
Subtraindo: 4-5 = -1'''

class Calculo:
    def soma(self, x, y):
        soma_f = x + y
        return f'Somando: {x}+{y} = {soma_f}'
    

    def subtracao(self, x, y):
        sub = x - y
        return f'Subtraindo: {x}+{y} = {sub}'
    

x = 4
y = 5

teste_soma = Calculo()
resultado_soma = teste_soma.soma(x, y)
print(resultado_soma)

teste_sub = Calculo()
resultado_sub = teste_sub.subtracao(x, y)
print(resultado_sub)

