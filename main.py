import os

from src.ObserverECDF import ObserverECDF
from src.Population import Population


def main():
    runs = 10
    directory = os.getcwd()
    conf_dir = directory + "/conf"
    hypermutation_on = [True, False]
    for r, d, f in os.walk(conf_dir):
        f.sort()
        for file in f:
            observerECDF = ObserverECDF(conf_dir + "/" + file)
            minimal = []
            for option in hypermutation_on:
                min_values = []
                for function_nr in range(1, 2):
                    population = Population(conf_dir + "/" + file, function_nr, option)
                    for run in range(runs):
                        print(file + "\t" + str(option) + "\t" + str(function_nr) + "\t" + str(run))
                        population.run()
                        mins, _, _ = population.getSimulationResults()
                        min_values.append(mins)
                minimal.append(min_values)
            observerECDF.plot_chart(minimal)


if __name__ == '__main__':
    main()
