# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:06:34 2018

@author: ty020
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB
train_data = ["cnm ok", "nice body", "****", "shit"]# 这个里面的每一个元素其实应该是一条评论
train_target = ["middle", "good", "good", "bad"]# 这个是对应上述评论的标签
test_data = ["cnm ok", "nice", "shit"]
test_target = ["middle", "good", "bad"]
nbc = Pipeline([
    ('vect', TfidfVectorizer(# 词频统计，这个东西的单独用法请单独去网上搜一搜，但是貌似是为了分词
                         
    )),
    ('clf', MultinomialNB(alpha=1.0)),
])
nbc.fit(train_data, train_target)    #训练我们的多项式模型贝叶斯分类器
predict = nbc.predict(test_data)  #在测试集上预测结果
count = 0                                      #统计预测正确的结果个数
for left , right in zip(predict, test_target):# 作者自己写的一个手动的评分器
      if left == right:
            count += 1
print(count/len(test_target))
