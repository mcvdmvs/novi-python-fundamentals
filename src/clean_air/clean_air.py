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

    # files
    measure_file = None
    permanent_data = []

    # measurements
    measurements = {}

    def __init__(self):
        pass

    def get_permanent_data(self, filename):
        self.permanent_data = filename

    def get_measure_file(self, filename):
        self.measure_file = filename

    def readMeasureData(self):
        self.measurements = {}

    def calcEmissions(self):
        total = 0
        for row in self.measurements:
            total += self.CO2 * row['CO2'] + self.CH4 * row['CH4'] + \
                self.NO2 * row['NO2'] + self.NH3 * row['NH3']

        return total
