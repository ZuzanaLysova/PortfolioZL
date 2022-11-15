'''
Data:
A - B: 1m
B - C: 2m
C - D: 1m
D - A: 3m
A - C: 3m
B - D: 2m
'''

import sys
import re

import graph

g = graph.Graph()
nodesSet = set()

for line in sys.stdin:
    groups = re.match("^([A-Z]\s-\s[A-Z]):\s([0-9])m$", line)
    #list of all couples of nodes that are connected
    if groups:
        pairOfNodes = groups.group(1).split(" - ")
        # To know how many nodes we have in graph and find out if graph is complete
        nodesSet.add(pairOfNodes[0])
        nodesSet.add(pairOfNodes[1])
        values = int(groups.group(2))
        node = pairOfNodes,values
        g = g.addNeighbours(node)

# print(g)
# g.EulerGraph()
print("TO FIX AND COMPLETE")
# g.isComplete()
# print(g.listOfNeighboursValued())

# print(len(nodesSet))