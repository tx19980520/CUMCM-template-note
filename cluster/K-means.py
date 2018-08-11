# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
n_clusters: 即我们的k值
max_iter: 最大迭代次数
n_init: 由于初始化质心的次数是随机的，所以我们可以多次循环得到最优解
init: 初始中心选择的方式，优化过的就是k-means++
algorithm: elkan指根据三角不等式来简化计算量，而且还能保证所有距离满足三角不等式
'''
#我最终要实现的就是一个只有距离的高维的东西，最终转到二维平面图，然后做k-means
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
from sklearn import manifold
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering


similarity= np.load("similarity.npy")
nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000,
                    dissimilarity="precomputed", n_jobs=1, n_init=1)
npos = nmds.fit_transform(similarity)
# 以上是通过凉凉直接的距离得到的二维图像

#在此你可以通过不通的聚类方式得到聚类的结果，并且作图
clustering = AgglomerativeClustering(linkage="ward", n_clusters=10)
y_pred = clustering.fit_predict(npos)
plt.scatter(npos[:, 0], npos[:, 1], c=y_pred)
plt.title("Bilibili anime ward")
#以下两种方式选出的最好的n_cluster
'''
result = []
mean = []
for i in range(2,20):
    y_pred = KMeans(n_clusters=i, max_iter=400, init='k-means++').fit(npos)
    result.append(metrics.silhouette_score(npos, y_pred.labels_,metric='euclidean'))
    mean.append(sum(np.min(cdist(
            npos,y_pred.cluster_centers_,"euclidean"),axis=1))/npos.shape[0])
plt.figure(1)
ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)
plt.sca(ax1)
plt.plot(range(2, 20), result)
plt.sca(ax2)
plt.plot(range(2, 20),mean,'bx-')
'''