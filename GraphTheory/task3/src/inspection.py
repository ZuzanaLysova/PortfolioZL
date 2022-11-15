'''
Data:
Ua |-01-| Ub
Ub |-02-| Uc
Uc |-03-| Ud
Ud |-04-| Uf
Uf |-05-| Uc
Uc |-06-| Ua
Ua |-07-| Uf
'''

import sys
import re

import graph

g = graph.Graph()
nodesSet = set()

for line in sys.stdin:
    groups = re.match("^(U[a-z])\s\|\-([0-9][0-9])\-\|\s(U[a-z])$", line)
    #list of all couples of nodes that are connected
    if groups:
        pairOfNodes = groups.group(1,3)
        # To know how many nodes we have in graph and find out if graph is complete
        nodesSet.add(pairOfNodes[0])
        nodesSet.add(pairOfNodes[1])
        values = groups.group(2)
        node = pairOfNodes,values
        g = g.addNeighbours(node)

# print(g)
# g.EulerGraph()
print("TO FIX AND COMPLETE")