# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:56:34 2018

@author: ty020
"""

from sklearn import svm
import numpy as np
from sklearn.externals import joblib
#我们最开始准备空间上的点的时候，就需要先进行分成便签和样本点
X = np.array([[0], [1], [2], [3]])
Y = np.array([0, 1, 2, 3])
#对于多分类问题，我们需要设计出两种方法
'''
更加多的注意SVC中的这么几个参数的设置
C: C越大，越不允许出错，C越小，则越可以容忍出错，可以对实际情况进行适当的调试
kernel: kernel函数是用于将原有空间映射到高维空间上的，可以进行相应的调节，甚至是自己设定函数都可。
class_weight: 用于我们规定两个类之间的数据量比例，来引导分类。
'''
clf = svm.SVC(decision_function_shape='ovo')  # 采用one-vs-one方式训练分类器 
#进行训练
clf.fit(X, Y)
#进行预测
print (clf.predict([[2.4]]))
print (clf.predict([[2.5]]))


#储存模型，以供下次快速使用
joblib.dump(clf, 'mysvm.model')
#用于调用保存的分类器
#svm = joblib.load("mysvm.model")
