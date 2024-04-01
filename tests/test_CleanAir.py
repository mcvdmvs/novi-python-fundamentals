import pytest
import CleanAir

class test_CleanAir():
  def __init__(self):
    self.CleanAir = CleanAir()
  
  def test_C1():
    assert self.CleanAir.C1 == 10
  
