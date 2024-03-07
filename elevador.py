
class Elevador:
    def __init__(self, origem): 
        self.origem = origem  # Added the origin variable


    def porta(self, porta = 0):
         '''
        Método que se receber valor 0 fecha aa porta, se receber 
        valor 1 abre a porta e se receber qualquer outro valor emite um alerta.
        '''
         if porta == 0:
             print("Fechando a porta") 
         elif porta == 1:
             print("Abrindo a porta")
         else:
             print("Perigo saia do elevador")
    @property
    def origem2(self):
         '''
        Método que guarda o andar que o elevador vai parar.
        '''
         return self.origem
            

        
        




 

    
