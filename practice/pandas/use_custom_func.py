import pandas as pd


def convert(cabin: int) -> bool:
    return 1 < cabin <= 3


if __name__ == "__main__":
    titanic = pd.read_csv("../../data/titanic.csv")
    print(titanic.head())
    #    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 0            1         0       3  ...   7.2500   NaN         S
    # 1            2         1       1  ...  71.2833   C85         C
    # 2            3         1       3  ...   7.9250   NaN         S
    # 3            4         1       1  ...  53.1000  C123         S
    # 4            5         0       3  ...   8.0500   NaN         S
    #
    # [5 rows x 12 columns]

    titanic["new_col"] = titanic["Pclass"].apply(convert)
    print(titanic["new_col"].head())
    # 0     True
    # 1    False
    # 2     True
    # 3    False
    # 4     True
    # Name: new_col, dtype: bool
