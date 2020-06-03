import pandas as pd
import sys

def region(file_path):
    path = file_path + "Region.csv"
    rg = pd.read_csv(path)
    # code deleted
    rg.drop("code", axis=1, inplace=True)
    # print(data_route.isnull().sum())
    return rg
