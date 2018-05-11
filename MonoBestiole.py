# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:31 2018

@author: amrouche
"""

import matplotlib.pyplot as plt

import utils
from CdM import CdM


class MonoBestiole(CdM):
  def __init__(self,t,pp1,pp2):
    self.taille = t
    self.p1 =pp1
    self.p2 =pp2
    super().__init__()


  def get_states(self):
    lr=[]
    i=1
    while (i<self.taille+1):
        lr.append(i)
        i=i+1
    return lr
 #tous les états possible

  def get_transition_distribution(self, state):
    if (state==1):
        return {1:self.p2, 2: self.p1}
    elif (state==self.taille):
        return {self.taille-1:self.p2, self.taille: self.p1}
    else:
        return {state-1:self.p2,state+1:self.p1}

  def get_initial_distribution(self):
      return  self.get_transition_distribution(1)
  def show_transition_matrix(self):
    utils.show_matrix(self.get_transition_matrix())
  def __len__(self):
    return len(self.get_states())
  def show_distribution(self, distribution):
      fig, ax = plt.subplots()
      fig.set_size_inches(self.taille, 1)
      ax.set_yticks([])
      ax.set_xticklabels(self.get_states())
      ax.set_xticks(list(range(0,(self.taille))))
      ax.imshow(self.distribution_to_vector(distribution).reshape(1,self.taille), cmap=utils.ProbaMap)
