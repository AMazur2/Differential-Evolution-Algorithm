from src.Population import Population
from src.Observer import Observer
import numpy as np
import pandas as pd
import os


def main():
    directory = os.getcwd()
    for r, d, f in os.walk(directory + "/conf"):
        f.sort()
        for file in f:
            print(file)
            population = Population(directory + "/conf/" + file)
            observer = Observer()
            population.run()
            results = population.getSimulationResults()
            df = pd.DataFrame(data=np.array(results), columns=["min", "max", "average"])
            observer.plot_chart(df)


if __name__ == '__main__':
    main()
