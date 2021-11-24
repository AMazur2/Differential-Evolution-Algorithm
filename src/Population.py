import numpy as np
import random
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
        self.is_hypermutation_on = config['is_hypermutation_on']
        self.mutator = Mutator(config['mutator'])
        self.generator = Generator(config['generator'])
        self.crossoverer = Crossoverer(config['crossoverer'])
        self.population = []
        self.results = []
        self.current_score = 0

    def initialize(self):
        self.population = self.generator.generate_population()

    def run(self):
        for epoch in range(self.epochs):
            next_population = []

            for i in range(len(self.population)):
                individual = self.population[i]
                random_1, random_2, random_3 = self.generate(i)

                if self.should_hypermutate():
                    self.mutator.hypermutate()
                donor = self.mutator.mutate(random_1, random_2, random_3)

                trial_vector = self.crossoverer.crossover(individual, donor)

                if self.evaluate(trial_vector) <= self.evaluate(individual):
                    next_population.append(trial_vector)
                else:
                    next_population.append(individual)

            self.population = next_population
            self.observeEpoch()

    def random_population_index(self):
        return random.randint(0, len(self.population) - 1)

    def generate(self, omitted):
        generated_indices = []
        for i in range(3):
            new_index = self.random_population_index()
            while (generated_indices + omitted).count(new_index):
                new_index = self.random_population_index()
            generated_indices.append(new_index)

        x0 = self.population[generated_indices[0]]
        x1 = self.population[generated_indices[1]]
        x2 = self.population[generated_indices[2]]

        return x0, x1, x2

    def should_hypermutate(self):
        if not self.is_hypermutation_on:
            return False
        first_result_to_consider_index = -6 if len(self.results) >= 6 else 0
        previous = self.results[first_result_to_consider_index][1]
        for i in range(first_result_to_consider_index + 1, len(self.results)):
            if self.results[i][1] > previous:
                return False
        return True

    def evaluate(self, x):
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

