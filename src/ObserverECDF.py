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

            x = np.arange(0.0, 1.0, 1.0 / self.epochs)
            y = np.zeros(len(x))

            ECDFs = []
            for i in range(0, len(hypermutation_option_results)):
                current_ECDF = ECDF(hypermutation_option_results[i])
                ECDFs.append(current_ECDF)

                span = current_ECDF.x[-1]

                for j in range(0, self.epochs):
                    y[j] += current_ECDF(float(j) / self.epochs * span)

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
