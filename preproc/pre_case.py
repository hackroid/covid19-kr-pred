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
    # print(data_case.isnull().sum())
    return data_case
