import preproc as pp


class COVID(object):
    def __init__(self):
        self.DATA_PATH = "../coronavirusdataset/"
        self.patient_route = pp.patient_route(self.DATA_PATH)
        self.case, self.group_map = pp.case(self.DATA_PATH)
        self.patient_info = pp.patient_info(self.DATA_PATH)

    def fill_missing(self):
        # patient_info:
        # fill missing value: infection_case
        self.patient_info["infection_case"] = self.patient_info["infection_case"].fillna("etc")


def main():
    covid_model = COVID()


if __name__ == '__main__':
    main()
