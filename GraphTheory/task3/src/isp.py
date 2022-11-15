'''
Data:
ISP - Honza: 30m
ISP - Pepa: 20m
Honza - Tomas: 40m
Honza - Anna: 40m
Pepa - Anna: 10m
Pepa - Michal: 20m
Tomas - Ondra: 10m
Anna - Ondra: 20m
Anna - Jirka: 40m
Michal - Jirka: 20m
Ondra - Jirka: 20m
'''

import sys
import re

import graph

g = graph.Graph()
nodesSet = set()

for line in sys.stdin:
    groups = re.match("([A-Za-z]+\s-\s[A-Za-z]+):\s([0-9]+)m", line)
    #list of all couples of nodes that are connected
    if groups:
        pairOfNodes = groups.group(1).split(" - ")
        values = int(groups.group(2))
        node = pairOfNodes,values
        g = g.addNeighbours(node)
        # g.oriented = True

# print(g)
# print(g.allEdgesPositive())
neighDict = g.listOfNeighboursValued()
# g.listOfParentsValuedOriented()
nodesListDijkstr = g.DijkstrAlgo()
# g.printDijkstr2()

allNodes = []
for neigh in neighDict:
    allNodes.append(neigh)
for oneNode in allNodes:
    # print("ONE", oneNode)
    for node in nodesListDijkstr:
        if node[0]==oneNode:
            print(f"{node[0]} -> {node[1]}: {node[2]}m", end='\n')