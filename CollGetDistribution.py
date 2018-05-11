#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:51:21 2018

@author: arij
"""

from Collector import Collector
import numpy as np
class CollGetDistribution(Collector):
  def __init__(self,epsilon,pas):
    self.epsilon=epsilon
    self.pas=pas
    self.proba_states={}
    self.prev_dest={}
    self.error=0

  def initialize(self, cdm, max_iter):
    self.max_iter=max_iter
    self.prev_dest=cdm.get_initial_distribution()
  def receive(self, cdm, iter, state):
    #calcul fréquences des etats
    if (state in self.proba_states):
      self.proba_states[state]+=1.0
    else:
      self.proba_states[state]=1
    dest={}
    for (k,v) in self.proba_states.items():
      dest[k]=v/(iter+1)

    old=cdm.distribution_to_vector(self.prev_dest)
    courant=cdm.distribution_to_vector(dest)
#    print(old)       
#    print(current)              
    error=np.amax(np.abs(np.array(courant-old)))                   
    if (error<self.epsilon):                                
          self.error=error
          return True                                      
    self.prev_dest=dest                                    
    if(iter%self.pas==0):
      cdm.show_distribution(self.prev_dest)
    if(iter==0):
        self.error=error
    elif(self.error>error) and iter == self.max_iter-1:
        self.error=error
    return False

  def finalize(self, cdm, iteration):
    pass
    
  def get_results(self, cdm):
    return {"erreur": self.error, "proba":self.prev_dest}