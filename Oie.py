#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 01:41:33 2018

@author: arij
"""

import numpy as np
from CdM import CdM
import matplotlib.pyplot as plt
import utils



class Oie(CdM):
    def __init__(self, n,p,q):
        self.n=n
        self.cases = np.zeros(n)
        self.p=p
        self.q=q
        self.case=1
        super().__init__()
    def get_type(self):
        type1=["N","P"]
        type2=["g","t","p"]
        t=np.random.choice(type1, p=[0.9,0.1])
        if t != "N":
            t=np.random.choice(type2, p=[self.p,self.p,self.q])
    def get_states(self):
        states=[]
        for i in list(range(1, self.n + 1)):
            states.append(str(i))
        states.append("b1")
        states.append("b2")

        return states
    def get_transition_distribution(self, state):
        if state == "1":
          self.case=2
          return {2 : 1}
        elif state == str(self.n):
          return {1: 1}
        elif state == 'b1':
            return {'b2': 1}
        elif state == 'b2':
            return {str(self.case ): 1}
        elif int(state) > self.n:
            return {str(self.n) : 1}
        else:
          s=int(state)
          t=self.get_type()
          if t=="N":
              return {str(s+1):1/6,str(s+2):1/6,str(s+3):1/6,str(s)+4:1/6,str(s+5):1/6,str(s+6):1/6}
          else:
              if(t=="g"):
                  return {str(s-1): 1}
              if(t=="t"):
                  return {str(s+1): 1}
              else:
                  self.case=s
                  return {'b1': 1}
                  
    def get_initial_distribution(self):
        return { 1 : 1.0}
    def show_transition_graph(self,gnb):
      super().show_transition_graph(gnb)
    def show_distribution(self, distribution):
      fig, ax = plt.subplots()
      fig.set_size_inches(self.taille, 1)
      ax.set_yticks([])
      ax.set_xticklabels(self.get_states())
      ax.set_xticks(list(range(0,(self.taille))))
      ax.imshow(self.distribution_to_vector(distribution).reshape(1,self.taille), cmap=utils.ProbaMap)
