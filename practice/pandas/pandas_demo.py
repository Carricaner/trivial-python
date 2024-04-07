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
    titanic = pd.read_excel("../../data/titanic.xlsx", sheet_name="passengers")
    # I’m interested in the names of the passengers older than 35 years.
    # When using loc/iloc, the part before the comma is the rows you want,
    # and the part after the comma is the columns you want to select.
    adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
    print(adult_names)
    # 1     Cumings, Mrs. John Bradley (Florence Briggs Th...
    # 6                               McCarthy, Mr. Timothy J
    # 11                             Bonnell, Miss. Elizabeth
    # 13                          Andersson, Mr. Anders Johan
    # 15                     Hewlett, Mrs. (Mary D Kingcome)
    # Name: Name, dtype: object

    print(adult_names)
    # (217,)

    print(titanic.loc[1:3, "Name":"Sex"])
    #                                                 Name     Sex
    # 1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female
    # 2                             Heikkinen, Miss. Laina  female
    # 3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female

    print(titanic.loc[titanic["PassengerId"].between(10, 15), "Name"])
    # 9      Nasser, Mrs. Nicholas (Adele Achem)
    # 10         Sandstrom, Miss. Marguerite Rut
    # 11                Bonnell, Miss. Elizabeth
    # 12          Saundercock, Mr. William Henry
    # 13             Andersson, Mr. Anders Johan
    # 14    Vestrom, Miss. Hulda Amanda Adolfina
    # Name: Name, dtype: object

    print(titanic[titanic["PassengerId"].between(10, 15) & titanic['Name'].str.startswith('S')]["Name"])
    # 10    Sandstrom, Miss. Marguerite Rut
    # 12     Saundercock, Mr. William Henry
    # Name: Name, dtype: object

    print(titanic.iloc[9:25, 2:5])
    #     Pclass                                               Name     Sex
    # 9        2                Nasser, Mrs. Nicholas (Adele Achem)  female
    # 10       3                    Sandstrom, Miss. Marguerite Rut  female
    # 11       1                           Bonnell, Miss. Elizabeth  female
    # 12       3                     Saundercock, Mr. William Henry    male
    # 13       3                        Andersson, Mr. Anders Johan    male
    # 14       3               Vestrom, Miss. Hulda Amanda Adolfina  female
    # 15       2                   Hewlett, Mrs. (Mary D Kingcome)   female
    # 16       3                               Rice, Master. Eugene    male
    # 17       2                       Williams, Mr. Charles Eugene    male
    # 18       3  Vander Planke, Mrs. Julius (Emelia Maria Vande...  female
    # 19       3                            Masselmani, Mrs. Fatima  female
    # 20       2                               Fynney, Mr. Joseph J    male
    # 21       2                              Beesley, Mr. Lawrence    male
    # 22       3                        McGowan, Miss. Anna "Annie"  female
    # 23       1                       Sloper, Mr. William Thompson    male
    # 24       3                      Palsson, Miss. Torborg Danira  female

    titanic.iloc[0:3, 3] = "anonymous"
    print(titanic["Name"].head())
    # 0                                       anonymous
    # 1                                       anonymous
    # 2                                       anonymous
    # 3    Futrelle, Mrs. Jacques Heath (Lily May Peel)
    # 4                        Allen, Mr. William Henry
    # Name: Name, dtype: object

