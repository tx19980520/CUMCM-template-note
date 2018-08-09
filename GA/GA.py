# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 12:00:35 2018

@author: ty020
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Find the global maximum for function: f(x) = x + 10sin(5x) + 7cos(4x)
'''

from math import sin, cos

from gaft import GAEngine
from gaft.components import BinaryIndividual
from gaft.components import Population
from gaft.operators import TournamentSelection
from gaft.operators import UniformCrossover
from gaft.operators import FlipBitMutation

# Analysis plugin base class.
from gaft.plugin_interfaces.analysis import OnTheFlyAnalysis

# Built-in best fitness analysis.
from gaft.analysis.fitness_store import FitnessStore

# Define population.
# 先对你所指定的初始种群进行编码
indv_template = BinaryIndividual(ranges=[(0, 10)], eps=0.001)
        '''
        :param ranges: value ranges for all entries in solution.
        :type ranges: list of range tuples. e.g. [(0, 1), (-1, 1)]

        :param eps: decrete precisions for binary encoding, default is 0.001.
        :type eps: float or float list with the same length with ranges.
        '''
population = Population(indv_template=indv_template, size=30).init()

# Create genetic operators.
selection = TournamentSelection()
crossover = UniformCrossover(pc=0.8, pe=0.5)
'''
    Crossover operator with uniform crossover algorithm,
    see https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)

    :param pc: The probability of crossover (usaully between 0.25 ~ 1.0)
    :type pc: float in (0.0, 1.0]

    :param pe: Gene exchange probability.
'''
mutation = FlipBitMutation(pm=0.1)
# pm is the possibility of the mutation
# Create genetic algorithm engine.
engine = GAEngine(population=population, selection=selection,
                  crossover=crossover, mutation=mutation,
                  analysis=[FitnessStore])

# Define fitness function.
@engine.fitness_register
def fitness(indv):
    x, = indv.solution
    return x + 10*sin(5*x) + 7*cos(4*x)

# Define on-the-fly analysis.
@engine.analysis_register
class ConsoleOutputAnalysis(OnTheFlyAnalysis):
    interval = 1
    master_only = True

    def register_step(self, g, population, engine):
        best_indv = population.best_indv(engine.fitness)
        msg = 'Generation: {}, best fitness: {:.3f}'.format(g, engine.ori_fmax)
        self.logger.info(msg)

    def finalize(self, population, engine):
        best_indv = population.best_indv(engine.fitness)
        x = best_indv.solution
        y = engine.ori_fmax
        msg = 'Optimal solution: ({}, {})'.format(x, y)
        self.logger.info(msg)

if '__main__' == __name__:
    # Run the GA engine.
    engine.run(ng=100)
