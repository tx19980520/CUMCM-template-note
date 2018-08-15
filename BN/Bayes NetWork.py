# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
raw_data = load_iris().data
data = pd.DataFrame(raw_data, columns=["A","B","C","D"])


# Defining the model
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator

model = BayesianModel()
model.add_nodes_from(["A","B","C","D"])

# Learing CPDs using Maximum Likelihood Estimators
model.fit(data, estimator=MaximumLikelihoodEstimator)
for cpd in model.get_cpds():
    print("CPD of {variable}:".format(variable=cpd.variable))
    print(cpd)