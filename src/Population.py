import numpy as np
import pandas as pd
import json
from opfunu.cec.cec2013.unconstraint import Model
from Mutator import Mutator
from Generator import Generator
from Crossoverer import Crossoverer

class Population:
    
    def __init__(self, configFile):
        config = {}
        
        with open(configFile) as configuration:
            config = json.load(configuration)
            
        self.epochs = config['epochs']
        self.function = config['fun_number']
        self.mutator = Mutator(config['mutator'])
        self.generator = Generator(config['generator'])
        #TODO: find a better name
        self.crossoverer = Crossoverer(config['crossoverer'])
        self.population = []
        self.results = []
      
    
    def initialize(self):
        self.population = self.generator.generate_population()

    def run(self):
        for epoch in range(self.epochs):
            for i in range(len(self.population)):
                individual = self.population[i]
                random_1, random_2, random_3 = self.generate()
                donor = self.mutator.mutate(random_1, random_2, random_3)
                trial_vector = self.crossoverer.crossover(individual, donor)
                if self.evaluate(trial_vector) <= self.evaluate(individual):
                    self.population[i] = trial_vector
            self.observeEpoch()


# TODO: not implemented
    def generate(self):
        x1 = [1, 2, 3, 4, 5]
        x2 = [1, 2, 3, 4, 5]
        x3 = [1, 2, 3, 4, 5]
        return x1, x2, x3
        
    def evaluate(self,x):
        return 1
    
    
    def observeEpoch(self):
        epoch_results = []
        individual_results = []
        
        for individual in self.population:
            individual_results.append(self.evaluate(individual))
            
        df = np.array(individual_results)
        
        epoch_results.append(np.min(df))
        epoch_results.append(np.max(df))
        epoch_results.append(np.average(df))
        
        self.results.append(np.array(epoch_results))
        
    def getSimulationResults(self):
        return self.results