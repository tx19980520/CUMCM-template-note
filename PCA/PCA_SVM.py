# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:35:59 2018

@author: ty020
"""

print(__doc__)


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause


import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import decomposition, datasets
from sklearn import svm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


pca = decomposition.PCA(n_components=3)
digits = datasets.load_iris()
X_digits = digits.data
y_digits = digits.target

# Plot the PCA spectrum
X_digits = pca.fit_transform(X_digits)
train_x,test_x,train_y,test_y = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
clf = svm.SVC(decision_function_shape='ovo')  # 采用one-vs-one方式训练分类器 
clf.fit(train_x, train_y)
result = clf.score(test_x,test_y)
print(result)

# 三维图的展示
colors = ["lavender","lightskyblue", "darkorange"]
ax = plt.subplot(111, projection='3d')
for node,label in zip(X_digits, y_digits):
    
    ax.scatter(node[0],node[1],node[2],c=colors[label], cmap=plt.cm.nipy_spectral,edgecolor='k')
    

plt.show()