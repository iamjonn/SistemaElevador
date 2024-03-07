from elevador import Elevador
from time import sleep



class Painel:
    def __init__(self, destino: int, origem = 0):
        self.origem = origem
        self.destino = destino if 0 < destino <= 13 else self.origem  # Corrected the assignment
        

    def __str__(self) -> str:
     if self.destino == self.origem:
        return f"Já estamos no andar {self.destino}º"
     elif self.destino > self.origem:
        for i in range(self.origem, self.destino + 1):  # Ajustado o range
            print(f"🔺{i}º")
            sleep(1)
        return f"Chegamos ao andar {self.destino}º"
     else:
        for i in range(self.origem, self.destino - 1, -1):  # Ajustado o range
            print(f"🔻{i}º")
            sleep(1)
        return f"Chegamos ao andar {self.destino}º"

    def run(self):
       origem = 0
       while True:
           self.destino = int(input("Digite o andar desejado: "))
           if self.destino == 0:
               print("Elevador desligado")
               break
           elevar = Elevador(self.destino)
           elevar.porta(0)
           play = Painel(self.destino, origem)
           print(play)
           elevar.porta(1)
           origem = elevar.origem2         

          
       

           




      




