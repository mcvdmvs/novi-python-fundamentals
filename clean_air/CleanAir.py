import sys
import numpy
import .Inspector

def CleanAir():
  # weight
  self.C1 = 1
  self.C2 = 2
  self.C3 = 4
  self.C4 = 7

  # fines
  self.F1 = 3
  self.F2 = 10
  self.F3 = 5
  self.F4 = 28
  
  def __init__(self, name):
    self.name = name

  def get_permanent_data(self, filename):
    self.permanent_data = filename
  
  def get_measure_file(self, filename):
    self.measure_file = filename
  
