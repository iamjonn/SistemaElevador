
class Elevador:
    def __init__(self, destino, origem =0):
        self.destino = destino 
        self.origem = self.destino  # Added the origin variable


    def porta(self, porta = 0):
        if porta == 0:
            print("Fechando a porta") 
        elif porta == 1:
            print("Abrindo a porta")
        else:
            print("Perigo saia do elevador")

              






 

    
