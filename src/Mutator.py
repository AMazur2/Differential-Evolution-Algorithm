
import numpy

class Mutator:

    def __init__(self, config):
        self.mutation_factor = config['mutation_factor']
        self.hypermutation_factor = config['hypermutation_factor']
        self.hypermutated = False

    def mutate(self, individual_1: numpy.array, individual_2: numpy.array, individual_3: numpy.array):

        factor: int
        if self.hypermutated:
            self.hypermutated = False
            factor = self.mutation_factor * self.hypermutation_factor
        else:
            factor = self.mutation_factor

        return individual_1 + factor * (individual_2 - individual_3)

    def hypermutate(self):
        self.hypermutated = True
