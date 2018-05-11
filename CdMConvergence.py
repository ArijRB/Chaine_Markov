#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:05:26 2018

@author: arij
"""
import numpy as np
from CollTimeOut import CollTimeOut
from CdMSampler import CdMSampler
from CollGetDistribution import CollGetDistribution
import time

class  CdMConvergence:
  def __init__(self, cdm):
    self.cdm = cdm
  def simulation(cdm,temps,nbrIter,eps):
      sampler=CdMSampler(cdm)
      sampler.add_collector(CollGetDistribution(epsilon=eps,pas=20000))
      sampler.add_collector(CollTimeOut(temps)) 
      return sampler.run(nbrIter)
  def ConvergencePi(cdm,temps,nbrIter,eps):
        start = time.time()
        temps_converg= time.time()
        pi_n_1=cdm.distribution_to_vector(cdm.get_initial_distribution())
        pi_n = np.dot(pi_n_1, cdm.get_transition_matrix())
        error=np.amax(np.abs(np.array(pi_n-pi_n_1)))
        i=1
        while (i<=nbrIter ) and temps_converg<=temps:
            pi_n = np.dot(pi_n_1, cdm.get_transition_matrix())
            error=np.amax(np.abs(np.array(pi_n-pi_n_1)))
            temps_converg=time.time() - start
            if error<eps:
                break
            pi_n_1=pi_n.copy()
            i+=1
        return {"erreur": error, "proba":cdm.vector_to_distribution(pi_n),"nbrIteration":i,"temps_conver":temps_converg}

  def CollConvergenceMat(cdm,temps,nbrIter,eps):
        start = time.time()
        temps_converg= time.time()
        M_n =cdm.get_transition_matrix()
        M_n_1=cdm.get_transition_matrix()
        M_n = np.dot(M_n, M_n_1)
        error=np.amax(np.abs(np.array(M_n-M_n_1)))
        i=1
        while (i<=nbrIter )and temps_converg<=temps:
            M_n = np.dot(M_n, M_n_1)
            error=np.amax(np.abs(np.array(M_n-M_n_1)))
            temps_converg=time.time() - start
            if error<eps:
                break
            M_n_1=M_n.copy()
            i+=1
        return {"erreur": error, "proba":M_n[0],"nbrIteration":i,"temps_conver":temps_converg}

  def ConvergencePtfixe(cdm,temps):
     start = time.time()
     a=cdm.get_transition_matrix()
     _,w=np.linalg.eig(a.T)
     left=w[:,0]
     pi=left/left.sum()
     fin=time.time()
     return {"proba":pi,"temps_conver":fin-start}
      
  def Convergence4Methodes(cdm,temps,nbrIter,eps):
      if(cdm.is_ergodic()):
          print("Methode : Simulation")
          print(CdMConvergence.simulation(cdm,temps,nbrIter,eps))
          print("*******************************************************************************")
          print("Methode : Convergence de  πn")
          print(CdMConvergence.ConvergencePi(cdm,temps,nbrIter,eps))
          print("*******************************************************************************")
          print("Methode : Convergence de  Mn ")
          print(CdMConvergence.CollConvergenceMat(cdm,temps,nbrIter,eps))
          print("*******************************************************************************")
          print("Methode : Point fixe")
          print(CdMConvergence.ConvergencePtfixe(cdm,temps))
      else:
          print("La chaine de Markov n'est ergodique")