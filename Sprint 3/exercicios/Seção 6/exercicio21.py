'''Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
Imprima no console exatamente assim:
Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu'''

class Passaro:
    def voar(self, voar):
        self.voar = voar

class Pato(Passaro):
    def __init__(self, voar, emitir_som):
        super().__init__(voar, emitir_som)
        emitir_som = "Quack Quack"
        

class Pardal(Passaro):
    def __init__(self, voar, emitir_som):
        super().__init__(voar, emitir_som)
        emitir_som = "Piu Piu"
        

voar = "Voando..." 
pato = Passaro(voar)
pato.voar