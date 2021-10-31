from math import sqrt
import random
from gene import Gene
from params import *

class Chromosome:
    '''Init Chromosome'''
    def __init__(self):
        self.genes = []
        i = 0
        while i < NB_GENES:
            self.genes.append(Gene()) 
            # au lieu de random.randint(0,1)) ;  ajouter des genes;;;; genes = [(x1,y1), (x2,y2), (x3,y3), ...., (xg,yg)]
            i += 1

    '''Chromosome Fitness'''
    def get_fitness(self):
        fitness = 0
        for i in range(NB_GENES-1):   
              # if(self.genes[i] != TARGET_CHROMOSOME[i]):
               fitness  += sqrt(pow(self.get_genes()[i].get_x()-self.get_genes()[i+1].get_x(),2) + pow(self.get_genes()[i].get_y()-self.get_genes()[i+1].get_y(),2))
              #  self.get_genes()[i].get_x() # sqrt((x1-x2)^2 + (y1-y2)^2)
        return fitness

    '''def get_fitness_si(self):
        fitness = 0
        for i in range(NB_GENES):
            if(self.genes[i] == TARGET_CHROMOSOME[i]):
                fitness += 1
        return fitness'''

    '''Chromosome Get Value'''
    def get_genes(self):
        return self.genes

    def __str__(self):
        return self.genes.__str__()

