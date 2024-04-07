import pandas as pd

if __name__ == '__main__':
    titanic = pd.read_excel("../../data/titanic.xlsx")

    print(titanic.sort_values(by="Age").head())
    #      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 803          804         1       3  ...   8.5167   NaN         C
    # 755          756         1       2  ...  14.5000   NaN         S
    # 644          645         1       3  ...  19.2583   NaN         C
    # 469          470         1       3  ...  19.2583   NaN         C
    # 78            79         1       2  ...  29.0000   NaN         S
    #
    # [5 rows x 12 columns]

    print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False)[["Pclass", "Age"]].head())
    #      Pclass   Age
    # 851       3  74.0
    # 116       3  70.5
    # 280       3  65.0
    # 483       3  63.0
    # 326       3  61.0

    air_quality = pd.read_csv("../../data/air_quality_long.csv")
    air_quality.set_index('date.utc', inplace=True)

    no2 = air_quality[air_quality["parameter"] == "no2"]
    no2_subset = no2.sort_index().groupby(["location"]).head(2)
    print(no2_subset)
    #                                 city country  ... value   unit
    # date.utc                                      ...
    # 2019-04-09 01:00:00+00:00  Antwerpen      BE  ...  22.5  µg/m³
    # 2019-04-09 01:00:00+00:00      Paris      FR  ...  24.4  µg/m³
    # 2019-04-09 02:00:00+00:00     London      GB  ...  67.0  µg/m³
    # 2019-04-09 02:00:00+00:00  Antwerpen      BE  ...  53.5  µg/m³
    # 2019-04-09 02:00:00+00:00      Paris      FR  ...  27.4  µg/m³
    # 2019-04-09 03:00:00+00:00     London      GB  ...  67.0  µg/m³
    #
    # [6 rows x 6 columns]

    print(no2_subset.pivot(columns="location", values="value"))
    # location                   BETR801  FR04014  London Westminster
    # date.utc
    # 2019-04-09 01:00:00+00:00     22.5     24.4                 NaN
    # 2019-04-09 02:00:00+00:00     53.5     27.4                67.0
    # 2019-04-09 03:00:00+00:00      NaN      NaN

    no2.pivot(columns="location", values="value").plot()

    print(air_quality.pivot_table(
        values="value", index="location", columns="parameter", aggfunc="mean"
    ))
    # parameter                 no2       pm25
    # location
    # BETR801             26.950920  23.169492
    # FR04014             29.374284        NaN
    # London Westminster  29.740050  13.443568

    print(air_quality.pivot_table(
        values="value",
        index="location",
        columns="parameter",
        aggfunc="mean",
        margins=True,
    ))
    # parameter                 no2       pm25        All
    # location
    # BETR801             26.950920  23.169492  24.982353
    # FR04014             29.374284        NaN  29.374284
    # London Westminster  29.740050  13.443568  21.491708
    # All                 29.430316  14.386849  24.222743

    print(air_quality.groupby(["parameter", "location"])[["value"]].mean())
    #                                   value
    # parameter location
    # no2       BETR801             26.950920
    #           FR04014             29.374284
    #           London Westminster  29.740050
    # pm25      BETR801             23.169492
    #           London Westminster  13.443568

    print(air_quality["value"].mean())
    # 24.22274279210926

    no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
    print(no2_pivoted.head())
    # location                   date.utc  BETR801  FR04014  London Westminster
    # 0         2019-04-09 01:00:00+00:00     22.5     24.4                 NaN
    # 1         2019-04-09 02:00:00+00:00     53.5     27.4                67.0
    # 2         2019-04-09 03:00:00+00:00     54.5     34.2                67.0
    # 3         2019-04-09 04:00:00+00:00     34.5     48.5                41.0
    # 4         2019-04-09 05:00:00+00:00     46.5     59.5                41.0

    no_2 = no2_pivoted.melt(id_vars="date.utc")
    print(no_2.head())
    #                     date.utc location  value
    # 0  2019-04-09 01:00:00+00:00  BETR801   22.5
    # 1  2019-04-09 02:00:00+00:00  BETR801   53.5
    # 2  2019-04-09 03:00:00+00:00  BETR801   54.5
    # 3  2019-04-09 04:00:00+00:00  BETR801   34.5
    # 4  2019-04-09 05:00:00+00:00  BETR801   46.5

    # `value_vars` defines which columns to melt together
    # `value_name` provides a custom column name for the values column instead of the default column name value
    # `var_name` provides a custom column name for the column collecting the column header names. Otherwise it takes the index name or a default variable
    no_2 = no2_pivoted.melt(
        id_vars="date.utc",
        value_vars=["BETR801", "FR04014", "London Westminster"],
        value_name="NO_2",
        var_name="id_location",
    )
    print(no_2.head())
    #                     date.utc id_location  NO_2
    # 0  2019-04-09 01:00:00+00:00     BETR801  22.5
    # 1  2019-04-09 02:00:00+00:00     BETR801  53.5
    # 2  2019-04-09 03:00:00+00:00     BETR801  54.5
    # 3  2019-04-09 04:00:00+00:00     BETR801  34.5
    # 4  2019-04-09 05:00:00+00:00     BETR801  46.5

    # plt.show()
