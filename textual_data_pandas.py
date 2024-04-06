import pandas as pd

if __name__ == "__main__":
    titanic = pd.read_csv("data/titanic.csv")
    print(titanic.head())
    #    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 0            1         0       3  ...   7.2500   NaN         S
    # 1            2         1       1  ...  71.2833   C85         C
    # 2            3         1       3  ...   7.9250   NaN         S
    # 3            4         1       1  ...  53.1000  C123         S
    # 4            5         0       3  ...   8.0500   NaN         S
    #
    # [5 rows x 12 columns]

    titanic["Name"].str.lower()
    print(titanic.head())
    #    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    # 0            1         0       3  ...   7.2500   NaN         S
    # 1            2         1       1  ...  71.2833   C85         C
    # 2            3         1       3  ...   7.9250   NaN         S
    # 3            4         1       1  ...  53.1000  C123         S
    # 4            5         0       3  ...   8.0500   NaN         S
    #
    # [5 rows x 12 columns]

    print(titanic["Name"].str.split(","))
    # 0                             [Braund,  Mr. Owen Harris]
    # 1      [Cumings,  Mrs. John Bradley (Florence Briggs ...
    # 2                              [Heikkinen,  Miss. Laina]
    # 3        [Futrelle,  Mrs. Jacques Heath (Lily May Peel)]
    # 4                            [Allen,  Mr. William Henry]
    #                              ...
    # 886                             [Montvila,  Rev. Juozas]
    # 887                      [Graham,  Miss. Margaret Edith]
    # 888          [Johnston,  Miss. Catherine Helen "Carrie"]
    # 889                             [Behr,  Mr. Karl Howell]
    # 890                               [Dooley,  Mr. Patrick]
    # Name: Name, Length: 891, dtype: object

    titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
    print(titanic["Surname"])
    # 0         Braund
    # 1        Cumings
    # 2      Heikkinen
    # 3       Futrelle
    # 4          Allen
    #          ...
    # 886     Montvila
    # 887       Graham
    # 888     Johnston
    # 889         Behr
    # 890       Dooley
    # Name: Surname, Length: 891, dtype: object

    print(titanic["Name"].str.contains("Countess"))
    # 0      False
    # 1      False
    # 2      False
    # 3      False
    # 4      False
    #        ...
    # 886    False
    # 887    False
    # 888    False
    # 889    False
    # 890    False
    # Name: Name, Length: 891, dtype: bool
    print(titanic[titanic["Name"].str.contains("Countess")])
    #      PassengerId  Survived  Pclass  ... Cabin Embarked  Surname
    # 759          760         1       1  ...   B77        S   Rothes
    #
    # [1 rows x 13 columns]

    print(titanic["Name"].str.len().idxmax())
    # 307
    print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])
    # Penasco y Castellana, Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo)

    titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
    print(titanic["Sex_short"])
    # 0      M
    # 1      F
    # 2      F
    # 3      F
    # 4      M
    #       ..
    # 886    M
    # 887    F
    # 888    F
    # 889    M
    # 890    M
    # Name: Sex_short, Length: 891, dtype: object
