import numpy as np
from random import uniform


class Crosser:

    def __init__(self, config):
        self.crossover_probability = config['crossover_probability']

    def crossover(self, target: np.array, donor: np.array):
        trial_vector = []

        for i in range(len(target)):
            random = uniform(0, 1)
            if random <= self.crossover_probability:
                trial_vector.append(donor[i])
            else:
                trial_vector.append(target[i])

        return np.array(trial_vector)
