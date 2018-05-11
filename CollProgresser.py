# -*- coding: utf-8 -*-
from Collector import Collector


class CollProgresser(Collector):
  def __init__(self, pas1=None, pas2=None):
    self.iteration = 0
    self.pas1 = pas1 if pas1 is not None else 10
    self.pas2 = pas2 if pas2 is not None else self.pas1 * 5

  def initialize(self, cdm, max_iter):
    self.iteration = 0
    print("run({}): ".format(max_iter), end="", flush=True)

  def receive(self, cdm, iter, state):
    if iter % self.pas2 == 0:
      print("#", end="", flush=True)
    elif iter % self.pas1 == 0:
      print(".", end="", flush=True)
    return False

  def finalize(self, cdm, iteration):
    self.iteration = iteration
    print(" <-- stop with {} iterations".format(iteration))

  def get_results(self, cdm):
    return None
