import csv
import numpy as np
import pandas as pd


def patient_info(file_path):
    path = file_path + "PatientInfo.csv"
    data_info = pd.read_csv(path)
    # global_num, country, disease, infection_order deleted
    data_info["group"] = 1
    data_info = data_info[["patient_id",
                           "sex",
                           "birth_year",
                           "age",
                           "province",
                           "city",
                           "infection_case",
                           "infected_by",
                           "contact_number",
                           "symptom_onset_date",
                           "confirmed_date",
                           "released_date",
                           "deceased_date",
                           "state",
                           "group"]]
    # fill missing value: infection_case
    data_info["infection_case"] = data_info["infection_case"].fillna("etc")
    data_info["group"] = 1
    # fill missing value:
    print(data_info.isnull().sum())
    print(data_info.head(10))
