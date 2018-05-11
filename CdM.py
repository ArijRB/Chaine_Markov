# -*- coding: utf-8 -*-
import numpy as np
import pyAgrum as gum
import pyAgrum.lib.ipython as gnb
import functools
import utils
class CdM:
  """
  Class virtuelle représentant une Chaîne de Markov
  """

  def __init__(self):
    """
    Constructeur. En particulier, initalise le dictionaire stateToIndex

    :warning: doit être appelé en fin de __init__ des classes filles
    avec ` super().__init__()`
    """
    self.states=self.get_states()
    self.stateToIndex=dict()
    index=0
    for e in self.states:
        self.stateToIndex[e]=index
        index+=1

  def get_transition_distribution(self, state):
    """
    :param state: état initial
    :return: un dictionnaire {etat:proba} représentant l'ensemble des états atteignables à partir de state et leurs
    probabilités
    """
    raise NotImplementedError

  def get_initial_distribution(self):
    """
    :return: un dictionnaire représentant la distribution à t=0 {etat:proba}
    """
    raise NotImplementedError

  def __len__(self):
    """
    permet d'utiliser len(CdM) pour avoir le nombre d'état d'un CdM

    :warning: peut être surchargée
    :return: le nombre d'état
    """
    return len(self.get_states())
    

  def show_transition_matrix(self):
    utils.show_matrix(self.get_transition_matrix())
    
    
  def distribution_to_vector(self,dist):
      t=np.zeros(len(self.stateToIndex))
      for key,value in self.stateToIndex.items():
          if key in dist:
              t[value]=dist[key]
       
      return t
  def vector_to_distribution(self,vect):
      dicti=dict()
      for i in range(len(vect)):
          t= list(self.stateToIndex.keys())
          if vect[i] != 0:
              dicti[t[i]]=vect[i]
      return dicti
      
 
  def show_distribution(self,dist):
      vectform=self.distribution_to_vector(dist)
      return vectform.tolist()

  def get_transition_matrix(self):
      mat=[]
      for s in self.get_states():
          res = self.get_transition_distribution(s)
          mat.append(self.distribution_to_vector(res))
      return np.array(mat)  
   
  def get_transition_graph(self):
	   g=gum.DiGraph()
	   for i in range (self.__len__()):
		   g.addNode() #on ajoute autant de noeud qu'il n y a d'états
	   mat=self.get_transition_matrix()
	   for i in range(len(mat)):
		   l=mat[i] #une ligne de la matrice
		   for j in range(len(l)):
			   p= l[j] #on recupere la proba correspondante dans la matrice
			   if(p!=0):
				   g.addArc(i,j) #si la proba n'est pas null on ajoute un arc entre les deux etats
	   return g

  def show_transition_graph(self,gnb):
      showres="digraph {"
      i=0
      for s in self.get_states():
          lab='{}'.format(i+1)+'[label="[{}'.format(i)+'] {}"];'.format(s)
          showres=showres+lab
          i=i+1
      mat = self.get_transition_matrix() 
      for i in range(len(mat)):
          l = mat[i]
          for j in range(len(l)):
              p = l[j]
              if(p != 0):
                  lab = '{}'.format(i+1)+'->{}'.format(j+1)+'[label={}]'.format(p)
                  showres = showres + lab
      showres=showres+"}"         
      gnb.showDot(showres)
   
  def get_communication_classes(self):
  
    classes = utils.tarjan(self.get_transition_graph())
    classes_states = []
    
    for c in classes:
      new_c = set()
      for i in c:
        for k,v in self.stateToIndex.items():
            if v == i:
                break
        new_c.add(k)
        
      classes_states.append(new_c)
    return classes_states
  def get_absorbing_classes(self):
      comm_class = self.get_communication_classes()
      res=[]
      for e in comm_class:
          absr=True
          j=0
          while(absr and j <len(e)):
              t=list(self.get_transition_distribution(list(e)[j]))
              for k in t:
                  if k not in e:
                      absr= False
              j+=1
          if absr:
              res.append(e)
      return res
              
  def is_irreducible(self):
      return len(self.get_communication_classes()) == 1
  def is_aperiodic(self):
      return self.get_periodicity() == 1
  def rech_cycle(self,graph, node, graph_s, cycles_, d):
      if node in graph_s:
          cycles_.add(d)
          return cycles_
      for child in graph_s:
          cycles_.union(self.rech_cycle(graph,node, graph.children(child),cycles_, d+1))
      return cycles_
      
  def get_periodicity(self):
      #Si la chaine est n'es irreducible chercher la periodicity n'as pas de sens
      if self.is_irreducible()== False:
          return 1
      else:
          #Si il existe un etat avec une periode 1 la periode de la chaine est 1
          for s in self.get_states():
              if s in list(self.get_transition_distribution(s).keys()):
                  return 1
          graph = self.get_transition_graph()
          graph_s = graph.children(0)
          cycles_= self.rech_cycle(graph, 0, graph_s, set(), 1)
          pg=functools.reduce(utils.pgcd, cycles_) 
      return pg

  def is_ergodic(self):
      return self.is_irreducible() and self.is_aperiodic()
      
