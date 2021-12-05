from src.Population import Population
from src.Observer import Observer
import numpy as np
import pandas as pd
import os


def main():
    runs = 12
    directory = os.getcwd()
    conf_dir = directory + "/conf"
    for r, d, f in os.walk(conf_dir):
        f.sort()
        for file in f:
            resultsMin = []
            resultsMax = []
            resultsAvg = []
            results = []
            print(file)
            observer = Observer(conf_dir + "/" + file)
            for i in range(runs):
                population = Population(conf_dir + "/" + file)
                population.run()
                minimal, avg, maximal = population.getSimulationResults()
                resultsMax.append(maximal)
                resultsMin.append(minimal)
                resultsAvg.append(avg)

            dfAvg = pd.DataFrame(data=np.array(resultsAvg))
            dfMax = pd.DataFrame(data=np.array(resultsMax))
            dfMin = pd.DataFrame(data=np.array(resultsMin))
            _, columns = dfAvg.shape
            for j in range(columns):
                epoch_results = [np.min(dfMin[j]), np.max(dfMax[j]), np.average(dfAvg[j])]
                results.append(epoch_results)
            df = pd.DataFrame(data=np.array(results), columns=["min", "max", "average"])
            print(df.shape)
            observer.plot_chart(df)


if __name__ == '__main__':
    main()
