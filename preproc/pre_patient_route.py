import pandas as pd


def patient_route(file_path):
    path = file_path + "PatientRoute.csv"
    data_route = pd.read_csv(path)
    # global_num deleted
    data_route = data_route[["patient_id",
                             "date",
                             "province",
                             "city",
                             "type",
                             "latitude",
                             "longitude"]]
    # print(data_route.isnull().sum())
    return data_route
