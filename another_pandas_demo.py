import pandas as pd

if __name__ == '__main__':
    air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

    air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
    print(air_quality.head())
    #                      station_antwerp  ...  london_mg_per_cubic
    # datetime                              ...
    # 2019-05-07 02:00:00              NaN  ...               43.286
    # 2019-05-07 03:00:00             50.5  ...               35.758
    # 2019-05-07 04:00:00             45.0  ...               35.758
    # 2019-05-07 05:00:00              NaN  ...               30.112
    # 2019-05-07 06:00:00              NaN  ...                  NaN
    #
    # [5 rows x 4 columns]

    air_quality["ratio_paris_antwerp"] = (
            air_quality["station_paris"] / air_quality["station_antwerp"]
    )
    print(air_quality.head())
    #                      station_antwerp  ...  ratio_paris_antwerp
    # datetime                              ...
    # 2019-05-07 02:00:00              NaN  ...                  NaN
    # 2019-05-07 03:00:00             50.5  ...             0.495050
    # 2019-05-07 04:00:00             45.0  ...             0.615556
    # 2019-05-07 05:00:00              NaN  ...                  NaN
    # 2019-05-07 06:00:00              NaN  ...                  NaN
    #
    # [5 rows x 5 columns]

    air_quality_renamed = air_quality.rename(
        columns={
            "station_antwerp": "BETR801",
            "station_paris": "FR04014",
            "station_london": "London Westminster",
        }
    )
    print(air_quality_renamed.head())
    #                      BETR801  FR04014  ...  london_mg_per_cubic  ratio_paris_antwerp
    # datetime                               ...
    # 2019-05-07 02:00:00      NaN      NaN  ...               43.286                  NaN
    # 2019-05-07 03:00:00     50.5     25.0  ...               35.758             0.495050
    # 2019-05-07 04:00:00     45.0     27.7  ...               35.758             0.615556
    # 2019-05-07 05:00:00      NaN     50.4  ...               30.112                  NaN
    # 2019-05-07 06:00:00      NaN     61.9  ...                  NaN                  NaN
    #
    # [5 rows x 5 columns]

    air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
    print(air_quality_renamed.head())
    #                      betr801  fr04014  ...  london_mg_per_cubic  ratio_paris_antwerp
    # datetime                               ...
    # 2019-05-07 02:00:00      NaN      NaN  ...               43.286                  NaN
    # 2019-05-07 03:00:00     50.5     25.0  ...               35.758             0.495050
    # 2019-05-07 04:00:00     45.0     27.7  ...               35.758             0.615556
    # 2019-05-07 05:00:00      NaN     50.4  ...               30.112                  NaN
    # 2019-05-07 06:00:00      NaN     61.9  ...                  NaN                  NaN
    #
    # [5 rows x 5 columns]
