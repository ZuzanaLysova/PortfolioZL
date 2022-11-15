'''
Data:
Group: Honza, Pepa, Anna, Jarek, Tomas
Honza - Pepa
Jarek - Anna
Anna - Tomas
Honza - Tomas
'''

import sys
import re

import graph

g = graph.Graph()

for line in sys.stdin:
    allNodes = re.match("^Group:\s(.*)$", line)
    groups = re.match("^((.*)\s-\s(.*))$", line)
    #list of all couples of nodes that are connected
    if groups:
        pairOfNodes = groups.group(1).split(" - ")
        g = g.addNeighbours(pairOfNodes)

nodesDict = g.nodeDegree()
sortedDict = g.sortGraph(nodesDict,2)
for node in sortedDict:
    print(f"{node} ({sortedDict[node]})")