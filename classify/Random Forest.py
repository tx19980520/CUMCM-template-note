# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:01:20 2018

@author: ty020
"""

#使用RandomForestClassifier 进行分类， RandomForestRegressor进行回归
'''
n_estimators 弱学习器的最大个数
oob_score 理论上袋外的样本可以用来检测泛化，最好设置为True
criterion 对基学习器的评估标准，例如CART树就是gini系数

上述是对于RF框架的一些参数
其余的参数主要是围绕树的一些参数，和之前的决策树的参数没有什么太大的不同

预测方法
predict_proba(x):给出带有概率值的记过，每个点在所有label的概率和为1
predict(x):直接给出结果
predict_log_proba(x)对predict_proba(x)得到的结果作log处理

训练完模型后可以使用属性feature_importances_，查看特征的重要性 ，值越大特征越重要。
'''

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
clf = RandomForestClassifier(n_estimators=13, oob_score=True)
clf.fit(X, y)






print(clf.feature_importances_)
#可以进行说明，对于某一个特征是更为重要的。
print(clf.predict([[0, 0, 0, 0]]))
