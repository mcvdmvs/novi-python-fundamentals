import pytest

from clean_air.clean_air import CleanAir


@pytest.fixture
def my_clean_air():
    return CleanAir()


def test_CO2_weight(my_clean_air):
    assert my_clean_air.CO2 == 1


def test_calcEmissions(my_clean_air):
    my_clean_air.measurements = [{"CO2": 2, "CH4": 4, "NO2": 54, "NH3": 7}]
    total = my_clean_air.calcEmissions()
    assert total == my_clean_air.CO2 * 2 + my_clean_air.CH4 * \
        4 + my_clean_air.NO2 * 54 + my_clean_air.NH3 * 7
