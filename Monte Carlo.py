# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:14:32 2018

@author: ty020
"""

import numpy as np
import matplotlib.pyplot as plt
sampleNo = 1002;
mu = 1500
sigma = 900
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo )
# 产生一个(mu, sigma)的正态分布，并且丛中提取sampleNo个数据
st1 = 0.0
st2 = 0.0
val1 = []
val2 = []
value = 4
cost = 1.5

for index in range(2,len(s)):
    pre1 = s[index-1]
    pre2 = (s[index-1] + s[index-2]) / 2.0
    fact1 = pre1 if s[index] > pre1 else s[index]
    fact2 = pre2 if s[index] > pre2 else s[index]
    st1 += -pre1*1.5+4*fact1
    st2 += -pre2*1.5+4*fact2
    val1.append(st1)
    val2.append(st2)
plt.plot(val1, ms=15, lw=2, alpha=0.7)
plt.plot(val2, ms=15, lw=2, alpha=0.7)