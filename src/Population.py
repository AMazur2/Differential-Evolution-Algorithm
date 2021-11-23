import numpy as np
import pandas as pd
import json
from opfunu.cec.cec2013.unconstraint import Model
from Mutator import Mutator
from Generator import Generator

class Population:
    
    def __init__(self, configFile):
        config = {}
        
        with open(configFile) as configuration:
            config = json.load(configuration)
            
        self.epochs = config['epochs']
        self.function = config['fun_number']
        self.mutator = Mutator(config['mutator'])
        self.generator = Generator(config['generator'])
        self.population = []
        self.results = []
      
    
    def initialize(self):
        self.population = self.generator.generate_population()
        
        
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