import matplotlib.pyplot as plt


class Observer:

    def __init__(self):
        pass

    def plot_chart(self, df):
        ax = plt.gca()

        df.plot(kind='line', x='index', y='min', color='green', ax=ax)
        df.plot(kind='line', x='index', y='average', color='red', ax=ax)
        df.plot(kind='line', x='index', y='max', color='blue', ax=ax)

        plt.show()