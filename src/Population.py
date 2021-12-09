import numpy as np
import random
import json
from opfunu.cec.cec2013.unconstraint import Model
from .Mutator import Mutator
from .Generator import Generator
from .Crosser import Crosser


class Population:

    def __init__(self, configFile, function, is_on):
        with open(configFile) as configuration:
            config = json.load(configuration)

        self.epochs = config['epochs']
        self.function = function
        self.is_hypermutation_on = is_on
        self.mutator = Mutator(config['mutator'])
        self.generator = Generator(config['generator'])
        self.crosser = Crosser(config['crossoverer'])
        self.population = []
        self.results = []
        self.resultsMin = []
        self.resultsMax = []
        self.resultsAvg = []
        self.current_score = 0
        self.fitness_fun = Model(config['dimension'])

    def run(self):
        self.initialize()

        for epoch in range(self.epochs):
            next_population = []

            for i in range(len(self.population)):
                individual = self.population[i]
                random_1, random_2, random_3 = self.generate(i)

                if self.should_hypermutate():
                    self.mutator.hypermutate()
                donor = self.mutator.mutate(random_1, random_2, random_3)

                trial_vector = self.crosser.crossover(individual, donor)

                if self.evaluate(trial_vector) <= self.evaluate(individual):
                    next_population.append(trial_vector)
                else:
                    next_population.append(individual)

            self.population = next_population
            self.observeEpoch()

    def initialize(self):
        self.population = self.generator.generate_population()

    def random_population_index(self):
        return random.randint(0, len(self.population) - 1)

    def generate(self, omitted):
        generated_indices = []
        for i in range(3):
            new_index = self.random_population_index()
            while generated_indices.count(new_index) or omitted == new_index:
                new_index = self.random_population_index()
            generated_indices.append(new_index)

        x0 = self.population[generated_indices[0]]
        x1 = self.population[generated_indices[1]]
        x2 = self.population[generated_indices[2]]

        return x0, x1, x2

    def should_hypermutate(self):
        if not self.is_hypermutation_on or len(self.results) < 6:
            return False
        first_result_to_consider_index = -6
        previous = self.results[first_result_to_consider_index][1]
        for i in range(first_result_to_consider_index + 1, len(self.results)):
            if self.results[i][1] > previous:
                return False
        return True

    def evaluate(self, x):
        return eval("self.fitness_fun.F" + str(self.function) + "(x)")

    def observeEpoch(self):
        epoch_results = []
        individual_results = []

        for individual in self.population:
            individual_results.append(self.evaluate(individual))

        df = np.array(individual_results)

        self.resultsMin.append(np.min(df))
        self.resultsMax.append(np.max(df))
        self.resultsAvg.append(np.average(df))

        epoch_results.append(np.min(df))
        epoch_results.append(np.max(df))
        epoch_results.append(np.average(df))

        self.results.append(np.array(epoch_results))

    def getSimulationResults(self):
        return self.resultsMin, self.resultsAvg, self.resultsMax
