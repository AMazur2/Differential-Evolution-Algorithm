import matplotlib.pyplot as plt
import json
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF


class ObserverECDF:

    def __init__(self, conf):
        with open(conf) as configuration:
            config = json.load(configuration)
            self.epochs = config['epochs']
            self.fun = config['fun_number']
            self.dim = config['dimension']
            mutationConfig = config['mutator']
            self.mutationF = mutationConfig['mutation_factor']
            self.hyper = mutationConfig['hypermutation_factor']
            generatorConfig = config['generator']
            self.populationSize = generatorConfig['size']
            self.isOn = config['is_hypermutation_on']

    def plot_chart(self, all_min_results):
        firstECDF = ECDF(all_min_results[0])
        x = np.array(firstECDF.x)
        y = np.array(firstECDF.y)

        for i in range(1, len(all_min_results)):
            y += ECDF(all_min_results[i]).y

        y /= len(all_min_results)

        plt.plot(x, y)

        plt.xlabel("results")
        plt.ylabel("proportion of function-target pairs")
        plt.title("Function:" + str(self.fun) + " Dimension:" + str(self.dim) + " Hyper: " + self.isOn)

        name = ("e" + str(self.epochs) + "-p" + str(self.populationSize) + "-f" + str(self.fun) + "-d" + str(self.dim) +
                "-o" + self.isOn + "-m" + str(self.mutationF) + "-h" + str(self.hyper) + "ECDF.png")
        plt.savefig(name)
        plt.clf()
        plt.cla()
        plt.close()
