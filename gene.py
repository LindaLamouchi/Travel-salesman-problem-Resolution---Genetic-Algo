import random

from params import NB_GENES
class Gene :
    def __init__(self):
        #Coordonnées (x,y) d'un pays
        self.x = random.randrange(1,NB_GENES) 
        self.y = random.randrange(1,NB_GENES) 
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def  __str__(self):
        return self.x,self.y