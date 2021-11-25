from src.Population import Population
from src.Observer import Observer
import numpy as np
import pandas as pd


def main():
    population = Population("config.json")
    observer = Observer()
    population.run()
    results = population.getSimulationResults()
    df = pd.DataFrame(data=np.array(results), columns=["min", "max", "average"])
    observer.plot_chart(df)


if __name__ == '__main__':
    main()
