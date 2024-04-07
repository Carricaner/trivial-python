import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    air_quality = pd.read_csv("../../data/air_quality_no2_long.csv")

    air_quality = air_quality.rename(columns={"date.utc": "datetime"})
    print(air_quality.head())
    #     city country                   datetime location parameter  value   unit
    # 0  Paris      FR  2019-06-21 00:00:00+00:00  FR04014       no2   20.0  µg/m³
    # 1  Paris      FR  2019-06-20 23:00:00+00:00  FR04014       no2   21.8  µg/m³
    # 2  Paris      FR  2019-06-20 22:00:00+00:00  FR04014       no2   26.5  µg/m³
    # 3  Paris      FR  2019-06-20 21:00:00+00:00  FR04014       no2   24.9  µg/m³
    # 4  Paris      FR  2019-06-20 20:00:00+00:00  FR04014       no2   21.4  µg/m³

    print(type(air_quality.city))
    #  <class 'pandas.core.series.Series'>
    print(air_quality.city)
    # 0        Paris
    # 1        Paris
    # 2        Paris
    # 3        Paris
    # 4        Paris
    #          ...
    # 2063    London
    # 2064    London
    # 2065    London
    # 2066    London
    # 2067    London
    # Name: city, Length: 2068, dtype: object

    print(air_quality.city.unique())
    # ['Paris' 'Antwerpen' 'London']

    # I want to work with the dates in the column datetime as datetime objects instead of plain text
    air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
    print(air_quality["datetime"])
    # 0      2019-06-21 00:00:00+00:00
    # 1      2019-06-20 23:00:00+00:00
    # 2      2019-06-20 22:00:00+00:00
    # 3      2019-06-20 21:00:00+00:00
    # 4      2019-06-20 20:00:00+00:00
    #                   ...
    # 2063   2019-05-07 06:00:00+00:00
    # 2064   2019-05-07 04:00:00+00:00
    # 2065   2019-05-07 03:00:00+00:00
    # 2066   2019-05-07 02:00:00+00:00
    # 2067   2019-05-07 01:00:00+00:00
    # Name: datetime, Length: 2068, dtype: datetime64[ns, UTC]

    # We can use this to directly parse the datetime column
    # pd.read_csv("../data/air_quality_no2_long.csv", parse_dates=["datetime"])

    min_and_max = air_quality["datetime"].min(), air_quality["datetime"].max()
    print(min_and_max)
    # (Timestamp('2019-05-07 01:00:00+0000', tz='UTC'), Timestamp('2019-06-21 00:00:00+0000', tz='UTC'))

    time_diff = air_quality["datetime"].max() - air_quality["datetime"].min()
    print(type(time_diff))
    # <class 'pandas._libs.tslibs.timedeltas.Timedelta'>
    # pandas.Timestamp is similar with datetime.timedelta
    print(time_diff)
    # 44 days 23:00:00

    air_quality["month"] = air_quality["datetime"].dt.month
    #     city country                  datetime  ... value   unit  month
    # 0  Paris      FR 2019-06-21 00:00:00+00:00  ...  20.0  µg/m³      6
    # 1  Paris      FR 2019-06-20 23:00:00+00:00  ...  21.8  µg/m³      6
    # 2  Paris      FR 2019-06-20 22:00:00+00:00  ...  26.5  µg/m³      6
    # 3  Paris      FR 2019-06-20 21:00:00+00:00  ...  24.9  µg/m³      6
    # 4  Paris      FR 2019-06-20 20:00:00+00:00  ...  21.4  µg/m³      6
    #
    # [5 rows x 8 columns]

    print(air_quality.groupby(
        [air_quality["datetime"].dt.weekday, "location"])["value"].mean())
    # datetime  location
    # 0         BETR801               27.875000
    #           FR04014               24.856250
    #           London Westminster    23.969697
    # 1         BETR801               22.214286
    #           FR04014               30.999359
    #           London Westminster    24.885714
    # 2         BETR801               21.125000
    #           FR04014               29.165753
    #           London Westminster    23.460432
    # 3         BETR801               27.500000
    #           FR04014               28.600690
    #           London Westminster    24.780142
    # 4         BETR801               28.400000
    #           FR04014               31.617986
    #           London Westminster    26.446809
    # 5         BETR801               33.500000
    #           FR04014               25.266154
    #           London Westminster    24.977612
    # 6         BETR801               21.896552
    #           FR04014               23.274306
    #           London Westminster    24.859155
    # Name: value, dtype: float64

    fig, axs = plt.subplots(figsize=(12, 4))
    air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
        kind='bar', rot=0, ax=axs
    )
    plt.xlabel("Hour of the day")
    plt.ylabel("$NO_2 (µg/m^3)$")
    plt.show()

    no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
    print(no_2.head())
    # location                   BETR801  FR04014  London Westminster
    # datetime
    # 2019-05-07 01:00:00+00:00     50.5     25.0                23.0
    # 2019-05-07 02:00:00+00:00     45.0     27.7                19.0
    # 2019-05-07 03:00:00+00:00      NaN     50.4                19.0
    # 2019-05-07 04:00:00+00:00      NaN     61.9                16.0
    # 2019-05-07 05:00:00+00:00      NaN     72.4
    print(no_2.index.year)
    # Index([2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
    #        ...
    #        2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019],
    #       dtype='int32', name='datetime', length=1033)
    print(no_2.index.weekday)
    # Index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #        ...
    #        3, 3, 3, 3, 3, 3, 3, 3, 3, 4],
    #       dtype='int32', name='datetime', length=1033)

    no_2["2019-05-20":"2019-05-21"].plot()
    plt.show()

    # Aggregate the current hourly time series values to the monthly maximum value in each of the stations.
    monthly_max = no_2.resample("ME").max()
    print(monthly_max)
    # location                   BETR801  FR04014  London Westminster
    # datetime
    # 2019-05-31 00:00:00+00:00     74.5     97.0                97.0
    # 2019-06-30 00:00:00+00:00     52.5     84.7

    print(monthly_max.index.freq)
    # <MonthEnd>

    no_2.resample("D").mean().plot(style="-o", figsize=(10, 5));
    plt.show()
