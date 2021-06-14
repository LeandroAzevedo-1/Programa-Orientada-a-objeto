#classe simples Computador 

class Computador:
    def __init__(self):
        self.marca = 'Asus'
        self.memoria_ran = '8gb'
        self.placa_de_video = 'Nvivia'



computador1 = Computador()
print(computador1.marca,computador1.memoria_ran,computador1.placa_de_video)
