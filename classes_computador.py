class Computador:
    def __init__(self, marca, memoria_ran, placa_de_video):
        self.marca = marca
        self.memoria_ran = memoria_ran
        self.placa_de_video = placa_de_video

    #metedo
    def Ligar(self):
        print('estou ligando')
    
    def Desligar(self):
        print('estou desligando')

    #metdo usando parametro
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ran, self.placa_de_video)
    
    #rodando o codigo
computador1 = Computador('Asus', '8gb', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()



