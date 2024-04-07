import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    air_quality = pd.read_csv("../../data/air_quality_no2.csv", index_col=0, parse_dates=True)
    print(air_quality.head())
    air_quality.plot()
    plt.show()
    air_quality["station_paris"].plot()
    plt.show()
    air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
    plt.show()

    air_quality.plot.box()
    plt.show()

    axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
    plt.show()