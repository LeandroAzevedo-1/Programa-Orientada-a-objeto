#Classe televisao simples 
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
tv = Televisao()
tv.ligada
tv.canal
print(tv.canal,tv.ligada)    
    
class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv = Televisão()
tv.ligada
tv.canal

#criei outro TV da classe Televião 
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4

#aqui imprimi as duas tvs que crie 
print(tv.ligada, tv.canal, tv_sala.ligada,tv_sala.canal)
 
