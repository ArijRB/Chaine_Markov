# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 16:12:29 2018

@author: 3523540
"""

from CdM import CdM
class MouseInMaze(CdM):
    def __init__(self):
        super().__init__()
        
    def get_states(self):
        return [1,2,3,4,5,6]
    
    def get_transition_distribution(self,state):
        if state==1:
            return {2:0.5, 1:0.5}
        elif state==2:
             return {4:0.5, 1:0.5}
        elif state==3:
             return {1:0.25, 6:0.25, 2:0.25, 5:0.25}
        elif state==4:
             return {3:1}
        elif state==5:
             return {5:1}
        elif state==6:
             return {6:1}   
        else:
            raise IndexError

    def get_initial_distribution(self):
        return {2:1} #etat initial 2 dans le cours
        

        
