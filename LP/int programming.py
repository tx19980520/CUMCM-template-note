# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 11:12:42 2018

@author: ty020
"""

import pulp
model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)
A = pulp.LpVariable('A', lowBound=0, cat='Integer')# define the variable and the bound and type
B = pulp.LpVariable('B', lowBound=0, cat='Integer')
model += 30000 * A + 45000 * B, "HI"
#add constraint
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21
model.solve()# start the model
model.writeLP("test.txt")
print("Production of Car A = {}".format(A.varValue))
print("Production of Car B = {}".format(B.varValue))
print(pulp.value(model.objective))