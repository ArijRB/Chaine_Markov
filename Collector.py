# -*- coding: utf-8 -*-


class Collector:
  def initialize(self, cdm, max_iter):
    """
    :param max_iter: le nombre max d'itération de la simulation
    Fonction appelée en début de simulation
    """
    raise NotImplementedError

  def receive(self, cdm, iter, state):
    """
    Fonction appelée à chaque itération d'une simulation
    :param cdm: la CdM simulée
    :param iter: l'indice de l'itération
    :param state: l'état dans l'itération courante
    :return: True si on doit arrêter la simulation
    """
    raise NotImplementedError

  def finalize(self, cdm, iteration):
    """
    Fonction appelée à la fin de la simulation
    :param iteration: l'indice de la dernière itération
    """
    raise NotImplementedError

  def get_results(self, cdm):
    """
    Fonction appelée après la simulation afin de collecter les résultats
    :return: None si pas de résultats, sinon un dictionnaire contenant une clé et comme valeur un type simple ou un
    dictionnaire.
    """
    raise NotImplementedError
