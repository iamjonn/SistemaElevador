
class Elevador:
    def __init__(self, destino, origem =0):
        self.destino = destino 
        self.origem = self.destino  # Added the origin variable


    def run(self):
        if self.destino == self.origem:
            return f"ja Estamos no andar {self.destino}º"
        elif self.destino > self.origem:
            return f"Estamos subindo para o {self.destino}º andar"
        else:
            return f"Estamos descendo para o {self.destino}º andar"  






 

    
