import pandas as pd


def time(file_path):
    path = file_path + "Time.csv"
    data_time = pd.read_csv(path)
    # time deleted
    data_time = data_time[["date","test","negative","confirmed", "released","deceased"]]
    # print(data_route.isnull().sum())
    return data_time
