import pytest
from clean_air.clean_air import CleanAir

@pytest.fixture
def my_clean_air():
  return CleanAir()

def test_CO2_weight(my_clean_air):
  assert my_clean_air.CO2 == 1

