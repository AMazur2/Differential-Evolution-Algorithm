from src.Population import Population
from src.Observer import Observer
import numpy as np
import pandas as pd
import os


def main():
    runs = 12
    directory = os.getcwd()
    resultsMin = []
    resultsMax = []
    resultsAvg = []
    file = directory + "/conf/config2.json"
    observer = Observer(file)
    for i in range(runs):
        population = Population(file)
        population.run()
        minimal, avg, maximal = population.getSimulationResults()
        resultsMax.append(maximal)
        resultsMin.append(minimal)
        resultsAvg.append(avg)
    df = pd.DataFrame(data=np.array(resultsAvg))
    _, columns = df.shape
    results = []
    for j in range(columns):
        epoch_results = [np.min(df[j]), np.max(df[j]), np.average(df[j])]
        results.append(epoch_results)
    df = pd.DataFrame(data=np.array(results), columns=["min", "max", "average"])
    observer.plot_chart(df)


if __name__ == '__main__':
    main()
