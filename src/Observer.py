import matplotlib.pyplot as plt
import json


class Observer:

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

    def plot_chart(self, df):
        ax = plt.gca()

        df.plot(kind='line', y='min', color='green', ax=ax)
        df.plot(kind='line', y='average', color='red', ax=ax)
        df.plot(kind='line', y='max', color='blue', ax=ax)

        plt.xlabel("epochs")
        plt.ylabel("fitness value")
        plt.title("Function:" + str(self.fun) + " Dimension:" + str(self.dim) + " Hyper: " + self.isOn)

        name = ("e" + str(self.epochs) + "-p" + str(self.populationSize) + "-f" + str(self.fun) + "-d" + str(self.dim) +
                "-o" + self.isOn + "-m" + str(self.mutationF) + "-h" + str(self.hyper) + ".png")
        plt.savefig(name)
        plt.clf()
        plt.cla()
        plt.close()
