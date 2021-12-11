import matplotlib.pyplot as plt
import json
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF


class ObserverECDF:

    def __init__(self, conf):
        with open(conf) as configuration:
            config = json.load(configuration)
            self.epochs = config['epochs']
            self.dim = config['dimension']
            self.resolution = config['output_resolution']
            mutationConfig = config['mutator']
            self.mutationF = mutationConfig['mutation_factor']
            self.hyper = mutationConfig['hypermutation_factor']
            generatorConfig = config['generator']
            self.populationSize = generatorConfig['size']

    def plot_chart(self, all_min_results):

        option_counter = 0
        for hypermutation_option_results in all_min_results:
            x_min = float('inf')
            x_max = float('-inf')
            ECDFs = []
            for i in range(1, len(hypermutation_option_results)):
                current_ECDF = ECDF(hypermutation_option_results[i])
                current_x = current_ECDF.x

                first_x = current_x[1]
                if first_x < x_min and first_x != float('-inf'):
                    x_min = first_x

                last_x = current_x[len(current_x) - 1]
                if last_x > x_max and last_x != float('inf'):
                    x_max = last_x
                ECDFs.append(current_ECDF)

            x = np.arange(x_min, x_max, (x_max - x_min)/self.resolution)
            y = np.zeros(self.resolution)

            for current_ECDF in ECDFs:
                i = 0
                for current_x in x:
                    y[i] += current_ECDF(current_x)
                    i += 1

            y /= len(hypermutation_option_results)

            plt.step(x, y, label=("Hypermutation on" if option_counter == 0 else "Hypermutation off")) #
            option_counter += 1

        plt.xlabel("results")
        plt.ylabel("proportion of function-target pairs")
        plt.title("Dimension:" + str(self.dim) + " Hypermutation factor:" + str(self.hyper) + " Mutation factor:" + str(self.mutationF))
        plt.legend()

        name = ("e" + str(self.epochs) + "-p" + str(self.populationSize) + "-d" + str(self.dim) +
                "-m" + str(self.mutationF) + "-h" + str(self.hyper) + "ECDF.png")
        plt.savefig(name)
        plt.clf()
        plt.cla()
        plt.close()
