# -*- coding: utf-8 -*-

from CdM import CdM


class PeriodicCdM(CdM):
  def __init__(self):
    super().__init__()

  def get_states(self):
    return "DEABCF"

  def get_transition_distribution(self, state):
    if state == 'A':
      return {'D': 1}
    elif state == 'B':
      return {'A': 1}
    elif state == 'C':
      return {'B': 1}
    elif state == 'D':
      return {'C': 0.3, 'E': 0.7}
    elif state == 'E':
      return {'F': 1}
    elif state == 'F':
      return {'A': 1}
    else:
      raise IndexError

  def get_initial_distribution(self):
    return {'A': 1}
