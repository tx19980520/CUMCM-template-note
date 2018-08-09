# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:59:50 2018

@author: ty020
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#构建graph 
G = nx.DiGraph() 
G.add_edge('x','a', capacity=3.0) 
G.add_edge('x','b', capacity=1.0) 
G.add_edge('a','c', capacity=3.0) 
G.add_edge('b','c', capacity=5.0) 
G.add_edge('b','d', capacity=4.0) 
G.add_edge('d','e', capacity=2.0) 
G.add_edge('c','y', capacity=2.0) 
G.add_edge('e','y', capacity=3.0) 
pos=nx.spring_layout(G) 
 
#显示graph 
edge_labels = nx.get_edge_attributes(G,'capacity') 
nx.draw_networkx_nodes(G,pos) 
nx.draw_networkx_labels(G,pos) 
nx.draw_networkx_edges(G,pos) 
nx.draw_networkx_edge_labels(G, pos,edge_labels) 
plt.axis('on') 
plt.xticks([]) 
plt.yticks([]) 
plt.show() 
 
#求最大流 
flow_value, flow_dict = nx.maximum_flow(G, 'x', 'y') 
print("最大流值: ",flow_value) 
print("最大流流经途径: ",flow_dict) 