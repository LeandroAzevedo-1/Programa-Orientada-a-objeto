class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False ):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    #criando metedo 

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo ')
            return
            

        if self.falando:
            print(f'{self.nome} já está comendo ')
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo ')


    
    #criando metedo, está comendo
    #trabalhando com funções 
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
    
    #criando outro metedo se for false para de coemr 

    def para_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo ')
            return

        print(f'{self.nome} parou de comer ')
        self.comendo = False

