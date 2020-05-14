import preproc as pp


class COVID(object):
    def __init__(self):
        self.DATA_PATH = "../coronavirusdataset/"
        self.patient_route = pp.patient_route(self.DATA_PATH)
        self.case = pp.case(self.DATA_PATH)
        self.patient_info = pp.patient_info(self.DATA_PATH)


def main():
    covid_model = COVID()


if __name__ == '__main__':
    main()
