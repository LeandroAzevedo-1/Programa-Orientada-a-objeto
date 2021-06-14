
# Criando um getter obtem um valor 

class Produto:
    def __init__(self, nome, preco ):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    
    #setter nome propery nome 
    @property
    def nome(self):
        return self._nome

    @nome.setter 
    def nome(self, valor):
        self._nome = valor.title()

    #se colocar(title) vem a primeira letra Maiúscula )
    #se colocar (lower) vem tudo minúscula)
    #se colocar (replace('A', '@'troca os a para @ ))
    #Getter
    @property
    def preco(self):
        return self._preco
    
    #Setter vai configurar o preco 
    @preco.setter
    def preco(self, valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

# se usar "R$15"str tem que fazer o Getter e o Setter para rodar o programa 

p2 = Produto('CANECA', 'R$15')    
p2.desconto(10)
print(p2.nome, p2.preco)