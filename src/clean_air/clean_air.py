import sys
import numpy
import Inspector

class CleanAir:
  # weight
  C1 = 1
  C2 = 2
  C3 = 4
  C4 = 7

  # fines
  F1 = 3
  F2 = 10
  F3 = 5
  F4 = 28
  
  def __init__(self, name):
    self.name = name

  def get_permanent_data(self, filename):
    self.permanent_data = filename
  
  def get_measure_file(self, filename):
    self.measure_file = filename
  
