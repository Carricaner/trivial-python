import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "height": [177, 180, 165],
        "Sex": ["male", "male", "female"],
    }
)

if __name__ == '__main__':
    titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
    ages = titanic["Age"]
    print(ages.head())
    # 0    22.0
    # 1    38.0
    # 2    26.0
    # 3    35.0
    # 4    35.0
    # Name: Age, dtype: float64
    print(type(ages))
    # <class 'pandas.core.series.Series'>
    print(ages.shape)
    # (891,)
    # A pandas Series is 1-dimensional and only the number of rows is returned.

    age_sex = titanic[["Age", "Sex"]]
    print(age_sex.head())
    #     Age     Sex
    # 0  22.0    male
    # 1  38.0  female
    # 2  26.0  female
    # 3  35.0  female
    # 4  35.0    male
    print(type(age_sex))
    #     Age     Sex
    # 0  22.0    male
    # 1  38.0  female
    # 2  26.0  female
    # 3  35.0  female
    # 4  35.0    male
    # <class 'pandas.core.frame.DataFrame'>
    print(age_sex.shape)
    # (891, 2)

    above_35 = titanic[titanic["Age"] > 35]
    print(above_35.head())
    #     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 1             2         1       1  ...  71.2833   C85         C
    # 6             7         0       1  ...  51.8625   E46         S
    # 11           12         1       1  ...  26.5500  C103         S
    # 13           14         0       3  ...  31.2750   NaN         S
    # 15           16         1       2  ...  16.0000   NaN         S
    #
    # [5 rows x 12 columns]
    print(titanic["Age"] > 35)
    # 0      False
    # 1       True
    # 2      False
    # 3      False
    # 4      False
    #        ...
    # 886    False
    # 887    False
    # 888    False
    # 889    False
    # 890    False
    # Name: Age, Length: 891, dtype: bool

    class_23 = titanic[titanic["Pclass"].isin([2, 3])]
    print(class_23.head())
    # Name: Age, Length: 891, dtype: bool
    #    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 0            1         0       3  ...   7.2500   NaN         S
    # 2            3         1       3  ...   7.9250   NaN         S
    # 4            5         0       3  ...   8.0500   NaN         S
    # 5            6         0       3  ...   8.4583   NaN         Q
    # 7            8         0       3  ...  21.0750   NaN         S
    #
    # [5 rows x 12 columns]

    # When combining multiple conditional statements, each condition must be surrounded by parentheses ().
    # Moreover, you can not use or/and but need to use the or operator | and the and operator &.
    class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
    print(class_23.head())
    #    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 0            1         0       3  ...   7.2500   NaN         S
    # 2            3         1       3  ...   7.9250   NaN         S
    # 4            5         0       3  ...   8.0500   NaN         S
    # 5            6         0       3  ...   8.4583   NaN         Q
    # 7            8         0       3  ...  21.0750   NaN         S
    #
    # [5 rows x 12 columns]

    age_no_na = titanic[titanic["Age"].notna()]
    print(age_no_na.head())
    # [5 rows x 12 columns]
    #    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 0            1         0       3  ...   7.2500   NaN         S
    # 1            2         1       1  ...  71.2833   C85         C
    # 2            3         1       3  ...   7.9250   NaN         S
    # 3            4         1       1  ...  53.1000  C123         S
    # 4            5         0       3  ...   8.0500   NaN         S
    #
    # [5 rows x 12 columns]
