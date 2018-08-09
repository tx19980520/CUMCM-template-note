# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 09:37:50 2018

@author: ty020
"""

import numpy as np
from scipy.optimize import linprog # for linear programming

# the example environment is in the document.
aim_function_para = np.array([4, 3])
# the objective function parameters
constraint_functions_para = np.array([[2, 1], [1, 1]])
# the constraint functions parameters, using different list to distinguish
constraint_functions_up_bound = np.array([10, 8])
# up_bound for the tow constraints_functions above.
bounds = ((0, None), (0, 7))
# the bounds the variables need obey(independent)
result = linprog(-aim_function_para, constraint_functions_para, constraint_functions_up_bound)