# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:47:41 2018

@author: ty020
"""

import numpy as np
import matplotlib.pyplot as plt
import pydotplus
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO

dot_data = StringIO()
iris = load_iris()

clf = DecisionTreeClassifier().fit(iris.data, iris.target)
#对于整个树的深度之类的可以提出一些要求进入到参数中，具体使用的时候再进行区分
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
'''
tree.export_graphviz(clf,out_file = dot_data,feature_names=feature_name,
                     class_names=target_name,filled=True,rounded=True,
                     special_characters=True)
'''
# 以上是export_graphviz的接口，需要美化或者怎样的，可以进行美化。