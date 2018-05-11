# -*- coding: utf-8 -*-
from Collector import Collector


class CollSingleStateCounter(Collector):
  def __init__(self, state):
    self.state = state

  def initialize(self, cdm, max_iter):
    self.counter = 0

  def receive(self, cdm, iter, state):
    if state == self.state:
      self.counter += 1
    return False

  def finalize(self, cdm, iteration):
    print("État <{}> visité {} fois".format(self.state, self.counter))

  def get_results(self, cdm):
    return {"count": {self.state: self.counter}}
