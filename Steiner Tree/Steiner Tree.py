# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:46:37 2018

@author: ty020
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()# create an empty graph 
core_G = nx.Graph()# create an empty graph 
#G.add_node(1)# add new node into the graph(here we need preprocess the data)
# add the edge, idem
G.add_weighted_edges_from([(1,3,4),(2,3,10),(2, 4, 3.5),(2, 1, 7.0)])
# for steiner tree we use prim to get the core graph and use dij to get the edge and update
core_nodes = [1, 3, 4]
dis = np.zeros(9)# start at 0 count up by 2, stop before 30
dis = dis.reshape(3, 3) # reshape array to be 3x5
has_in = set([1])
# discount all the distance
for i in range(3):
    for j in range(3):
        dis[i][j] = nx.dijkstra_path_length(G,core_nodes[i],core_nodes[j])
        core_G.add_weighted_edges_from([(core_nodes[i],core_nodes[j],dis[i][j])])
# init the core graph to use prim algorithms
T=nx.minimum_spanning_tree(core_G)
# pirm    
core_path = sorted(T.edges(data=True))

normal_path_nodes = set()
# convert core graph to normal graph
for path in core_path: 
    nodes = nx.dijkstra_path(G, path[0], path[1])
    for n in nodes:
        normal_path_nodes.add(n)
print(normal_path_nodes)


