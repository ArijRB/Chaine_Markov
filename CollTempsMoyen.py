#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:38:24 2018

@author: arij
"""

import time
import numpy as np
from Collector import Collector


class CollTempsMoyen(Collector):
    def __init__(self):
        self.temps=[]
        self.depbut=0
        self.nb=0

    def initialize(self, cdm, max_iter):
        self.start=time.clock()

    def receive(self, cdm, iter, state):
        if state not in ["b1","b2"]:           
            if cdm.cases[int(state)-1] == -2 :
                return True
            if state == len(cdm.get_states()) : 
                self.temps.append(time.clock() - self.debut) 
                self.debut=time.clock() 
                self.nb+=1 
        return False

    def finalize(self, cdm, iteration):
        pass

    def get_results(self, cdm):
        return {"Nombre de retour vers debut": self.nb, "Temps Moyen ": np.nanmean(np.array(self.temps))}