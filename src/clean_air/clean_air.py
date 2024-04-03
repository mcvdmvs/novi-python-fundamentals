import numpy

from clean_air.inspector import Inspector


class CleanAir:
    # weight
    CO2 = 1
    CH4 = 2
    NO2 = 4
    NH3 = 7

    # fines
    F1 = 3
    F2 = 10
    F3 = 5
    F4 = 28

    def __init__(self):
        pass

    def get_permanent_data(self, filename):
        self.permanent_data = filename

    def get_measure_file(self, filename):
        self.measure_file = filename
