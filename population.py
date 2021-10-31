from chromosome import Chromosome
from params import *

class Population:
    def __init__(self) :
        self.chromosomes = []
        i = 0
        while i < POPULATION_SIZE :
            self.chromosomes.append( Chromosome() )
            i += 1
        self.chromosomes.sort(key=lambda x: x.get_fitness(), reverse=False)

    '''Get All Population Chromosomes'''
    def get_chromosomes(self):
        return self.chromosomes

    def print_population(self, gen_number):
        print("\n-----------------------Generation Summary---------------------------")
        print("--------------------------------------------------------------------")
        print("Generation #", gen_number, "| Fittest chromosome fitness:", self.get_chromosomes()[0].get_fitness())
        # print("Target chromosome", TARGET_CHROMOSOME)
        print("--------------------------------------------------------------------")
        i = 0
        for x in self.get_chromosomes():
            for y in range(NB_GENES-1) : 
             print("Chromosome #",i," : (",x.get_genes()[y]. __str__(),") | Fitness", x.get_fitness())
            
            print("Chromosome #",i," : Fitness", x.get_fitness())
            i += 1

p = Population()
p.print_population(1)