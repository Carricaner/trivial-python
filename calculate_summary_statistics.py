import pandas as pd

if __name__ == '__main__':
    titanic = pd.read_excel("data/titanic.xlsx")
    print(titanic["Age"].mean())
    # 29.69911764705882

    print(titanic[["Age", "Fare"]].median())
    # Age     28.0000
    # Fare    14.4542
    # dtype: float64

    print(titanic[["Age", "Fare"]].describe())
    #               Age        Fare
    # count  714.000000  891.000000
    # mean    29.699118   32.204208
    # std     14.526497   49.693429
    # min      0.420000    0.000000
    # 25%     20.125000    7.910400
    # 50%     28.000000   14.454200
    # 75%     38.000000   31.000000
    # max     80.000000  512.329200

    print(titanic.agg(
        {
            "Age": ["min", "max", "median", "skew"],
            "Fare": ["min", "max", "median", "mean"],
        }
    ))
    #               Age        Fare
    # min      0.420000    0.000000
    # max     80.000000  512.329200
    # median  28.000000   14.454200
    # skew     0.389108         NaN
    # mean          NaN   32.204208

    print(titanic[["Sex", "Age"]].groupby("Sex").mean())
    #               Age
    # Sex
    # female  27.915709
    # male    30.726645

    print(titanic.groupby("Sex").mean(numeric_only=True))
    #         PassengerId  Survived    Pclass  ...     SibSp     Parch       Fare
    # Sex                                      ...
    # female   431.028662  0.742038  2.159236  ...  0.694268  0.649682  44.479818
    # male     454.147314  0.188908  2.389948  ...  0.429809  0.235702  25.523893
    #
    # [2 rows x 7 columns]

    print(titanic.groupby("Sex")["Age"].mean())
    # Sex
    # female    27.915709
    # male      30.726645
    # Name: Age, dtype: float64

    print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())
    # Sex     Pclass
    # female  1         106.125798
    #         2          21.970121
    #         3          16.118810
    # male    1          67.226127
    #         2          19.741782
    #         3          12.661633
    # Name: Fare, dtype: float64

    print(titanic["Pclass"].value_counts())
    # Pclass
    # 3    491
    # 1    216
    # 2    184
    # Name: count, dtype: int64

    print(titanic.groupby("Pclass")["Pclass"].count())
    # Pclass
    # 1    216
    # 2    184
    # 3    491
    # Name: Pclass, dtype: int64
