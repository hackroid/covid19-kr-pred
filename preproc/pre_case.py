import pandas as pd


def case(file_path):
    path = file_path + "Case.csv"
    data_case = pd.read_csv(path)
    # fill missing value: city, latitude, longitude
    data_case.loc[data_case["city"] == "-", "city"] = "etc"
    data_case.loc[data_case["latitude"] == "-", "latitude"] = -1
    data_case.loc[data_case["longitude"] == "-", "longitude"] = -1
    data_case["latitude"] = data_case["latitude"].astype("float64")
    data_case["longitude"] = data_case["longitude"].astype("float64")
    map_group = dict()
    for _, row in data_case.iterrows():
        map_group[row["infection_case"]] = row["group"]
    # print(data_case.isnull().sum())
    # print(map_group)
    return data_case, map_group
