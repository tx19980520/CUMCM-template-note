# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:38:01 2018

@author: ty020
"""

import pulp
import pandas as pd
model = pulp.LpProblem("DVD rent plan problem", pulp.LpMaximize)
DVDs = pd.read_excel("DVD.xlsx")
raw_orders = pd.read_excel("dd.xlsx").to_dict()
vars = []
for i in range(1000):
    var = []
    for j in range(100):
        var.append(pulp.LpVariable("order%dDVD%d"%(i,j), cat='Integer', lowBound=0, upBound=1))
    vars.append(var)

expression = []
for i in range(1000):
    likes = raw_orders["order%d"%(i+1)]
    var = vars[i]
    for i in range(len(var)):
        expression.append(var[i]*likes[i])

model += pulp.lpSum(expression)
#add constraint
for j in range(1,101):
    j_constraint = []
    for i in range(1000):
        j_constraint.append(vars[i][j-1])
    model += pulp.lpSum(j_constraint) <= DVDs["D%03d"%(j)]
    
model.solve()# start the model
model.writeLP("test.txt")
for var in vars:
    for v in var:
        print(v.varValue),
print(pulp.value(model.objective))