"""
this script was designed to initialize the graph G
and the rest of the demo is in an interactive ipython stint
ie i just
    %run example.py
this also loads some functions for manipulating G
as well as the coloring of G returned by networkx
so that I wouldn't have to come up with these routines on the spot
"""
import networkx as nx
from itertools import combinations

#get all the names of the elements
with open("elements.txt", "r") as f:
    lines = f.readlines()
names = []
for line in lines:
    names.append(line.split()[0])

#all possible pairs of names
pairs = list(combinations(names,2))

#any two names which share the first or last letter conflict
G = nx.Graph()
for pair in pairs:
    if (pair[0][0] == pair[1][0]) or (pair[0][-1] == pair[1][-1]):
        #add the edge
        G.add_edge(pair[0], pair[1])

#produce a coloring for G
coloring = nx.greedy_color(G, strategy='DSATUR')

def numColors(coloring):
    #find max value of coloring, which is a dict
    #then add 1, since indices start at 0
    return coloring[max(coloring, key=coloring.get)] + 1

def maxDegree(graph):
    #find the max degree in graph
    degrees = []
    for node in list(graph.degree(names)):
        degrees.append(node[1])
    return max(degrees)

def verticesWithColor(i, coloring):
    #return all vertices with color i as specified by coloring
    verts = [k for k,v in coloring.items() if v == i]
    return verts
