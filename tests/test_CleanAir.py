import pytest
from src.clean_air import * 

@pytest.fixture
def my_clean_air():
  return CleanAir()

def test_C1():
  assert my_clean_air.C1 == 10

