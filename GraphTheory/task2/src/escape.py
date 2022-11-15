'''
Data:
Sections: mustek, motory, navigace, komunikace, kyslik, unikovy_modul
mustek - motory
mustek - kyslik
motory - kyslik
motory - navigace
kyslik - komunikace
komunikace - navigace
navigace - unikovy_modul
'''

import sys
import re

import graph

g = graph.Graph()

for line in sys.stdin:
    allNodes = re.match("^Sections:\s(.*)$", line)
    groups = re.match("^(([a-z]|[0-9])+\s-\s([a-z]|[0-9]|_)+?)$", line)
    #list of all couples of nodes that are connected
    if groups:
        pairOfNodes = groups.group(1).split(" - ")
        node = tuple(pairOfNodes)
        g = g.addNeighbours(node)

# print(g.listOfNeighboursNotValued())

wanderList = g.wander()
if wanderList:
    for elem in wanderList:
        print(' -> '.join((map(str,elem))))
