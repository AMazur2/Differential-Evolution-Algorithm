import numpy as np
from random import uniform

class Generator:
    
    def __init__(self, config):
        self.pop_size = config['size']
        self.dimension = config['dimension']
        self.min_val = config['min']
        self.max_val = config['max']
        
    def generate_population(self):
        population = []
        
        for i in range(self.pop_size):
            individual = []
            for j in range(self.dimension):
                individual.append(uniform(self.min_val, self.max_val))
            
            population.append(np.array(individual))
        
        return population
    