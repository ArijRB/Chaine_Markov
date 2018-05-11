# -*- coding: utf-8 -*-
import time

from Collector import Collector


class CollTimeOut(Collector):
  def __init__(self, max_duration):
    self.max_duration = max_duration
    self.start_time = 0
    self.duration = 0

  def initialize(self, cdm, max_iter):
    self.start_time = time.time()
    self.duration = 0

  def receive(self, cdm, iter, state):
    if iter % 100 == 0:
      self.duration = time.time() - self.start_time
      if self.duration > self.max_duration:
        print(" [Time Out]", end="", flush=True)
        return True
    return False

  def finalize(self, cdm, iteration):
    self.duration = time.time() - self.start_time
    print("Durée : {}s".format(self.duration))

  def get_results(self, cdm):
    return {"duration": self.duration}
