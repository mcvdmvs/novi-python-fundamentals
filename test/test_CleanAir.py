import pytest
from clean_air import CleanAir

class test_CleanAir():
  self.CleanAir = CleanAir()
  
  def test_C1():
    assert self.CleanAir.C1 == 10
  
