
class Elevador:
    def __init__(self, origem): 
        self.origem = origem  # Added the origin variable


    def porta(self, porta = 0):
        if porta == 0:
            print("Fechando a porta") 
        elif porta == 1:
            print("Abrindo a porta")
        else:
            print("Perigo saia do elevador")
    @property
    def origem2(self):
        return self.origem
            

        
        




 

    
