from src.Population import Population
from src.Observer import Observer
from src.ObserverECDF import ObserverECDF
import numpy as np
import pandas as pd
import os
from datetime import datetime


#def main():
#    now = datetime.now()
#    current_time = now.strftime("%H:%M:%S")
#    print("Current Time =", current_time)
#
#    runs = 10
#    directory = os.getcwd()
#    conf_dir = directory + "/conf"
#    for r, d, f in os.walk(conf_dir):
#        f.sort()
#        for file in f:
#            resultsMin = []
#            resultsMax = []
#            resultsAvg = []
#            results = []
#            print(file)
#            observer = Observer(conf_dir + "/" + file)
#            observerECDF = ObserverECDF(conf_dir + "/" + file)
#            for i in range(runs):
#                population = Population(conf_dir + "/" + file)
#                population.run()
#                minimal, avg, maximal = population.getSimulationResults()
#                resultsMax.append(maximal)
#                resultsMin.append(minimal)
#                resultsAvg.append(avg)
#
#            dfAvg = pd.DataFrame(data=np.array(resultsAvg))
#            dfMax = pd.DataFrame(data=np.array(resultsMax))
#            dfMin = pd.DataFrame(data=np.array(resultsMin))
#
#            _, columns = dfAvg.shape
#            for j in range(columns):
#                epoch_results = [np.min(dfMin[j]), np.max(dfMax[j]), np.average(dfAvg[j])]
#                results.append(epoch_results)
#            df = pd.DataFrame(data=np.array(results), columns=["min", "max", "average"])
#            observer.plot_chart(df)
#
#            observerECDF.plot_chart(resultsMin)
#
#    now = datetime.now()
#    current_time = now.strftime("%H:%M:%S")
#    print("Current Time =", current_time)


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
                for function_nr in range(1, 29):
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
