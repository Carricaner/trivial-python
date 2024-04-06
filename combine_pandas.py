import pandas as pd
from pandas import json_normalize
import openaq


if __name__ == '__main__':
    air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv",
                                  parse_dates=True)

    air_quality_no2 = air_quality_no2[["date.utc", "location",
                                       "parameter", "value"]]

    air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",
                                   parse_dates=True)

    air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                         "parameter", "value"]]

    air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
    print(air_quality.head())
    #                     date.utc location parameter  value
    # 0  2019-06-18 06:00:00+00:00  BETR801      pm25   18.0
    # 1  2019-06-17 08:00:00+00:00  BETR801      pm25    6.5
    # 2  2019-06-17 07:00:00+00:00  BETR801      pm25   18.5
    # 3  2019-06-17 06:00:00+00:00  BETR801      pm25   16.0
    # 4  2019-06-17 05:00:00+00:00  BETR801      pm25    7.5

    air_quality = air_quality.sort_values("date.utc")
    print(air_quality.head())
    #                        date.utc            location parameter  value
    # 2067  2019-05-07 01:00:00+00:00  London Westminster       no2   23.0
    # 1003  2019-05-07 01:00:00+00:00             FR04014       no2   25.0
    # 100   2019-05-07 01:00:00+00:00             BETR801      pm25   12.5
    # 1098  2019-05-07 01:00:00+00:00             BETR801       no2   50.5
    # 1109  2019-05-07 01:00:00+00:00  London Westminster      pm25    8.0

    air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
    print(air_quality_.head())
    #                          date.utc location parameter  value
    # PM25 0  2019-06-18 06:00:00+00:00  BETR801      pm25   18.0
    #      1  2019-06-17 08:00:00+00:00  BETR801      pm25    6.5
    #      2  2019-06-17 07:00:00+00:00  BETR801      pm25   18.5
    #      3  2019-06-17 06:00:00+00:00  BETR801      pm25   16.0
    #      4  2019-06-17 05:00:00+00:00  BETR801      pm25    7.5

    api = openaq.OpenAQ()
    res = api.locations()
    print(res[1]['meta'])