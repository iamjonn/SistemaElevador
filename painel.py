from elevador import Elevador


origem = Elevador.origem()

class Painel:
    def __init__(self, destino: int):
        self.origem = origem
        self.destino = destino if 0 < destino < 13 else self.origem  # Corrected the assignment
        Elevador(self.destino)

    def __str__(self) -> str:
         if self.destino == self.origem:
             return f"ja Estamos no andar {self.destino}º"
         if self.destino > self.origem:
             return f"Estamos subindo para o {self.destino}º andar"
         if self.destino < self.origem:
             return f"Estamos descendo para o {self.destino}º andar"
