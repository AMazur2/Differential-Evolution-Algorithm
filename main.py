from src.Population import Population
import numpy as np
import pandas as pd

def main():
    population = Population("config.json")
    population.run()
    results = population.getSimulationResults()
    print(results)
    #df = pd.DataFrame(data=np.array(results), )

if __name__ == '__main__':
    main()
