'''
Data:
CPU: motory, navigace, komunikace, mustek, kyslik
motory - kyslik: 15s
navigace - komunikace: 90s
mustek - kyslik: 20s
motory - navigace: 50s
komunikace - mustek: 35s
kyslik - komunikace: 15s
'''

import sys
import re

import graph

g = graph.Graph()

for line in sys.stdin:
    allNodes = re.match("^CPU:\s(.*)$", line)
    groups = re.match("^([a-z]+\s-\s[a-z]+):\s([0-9]+)s$", line)
    #list of all couples of nodes that are connected
    if groups:
        pairOfNodes = groups.group(1).split(" - ")
        values = int(groups.group(2))
        node = pairOfNodes,values
        g = g.addNeighbours(node)

minSkelet = g.minSkelet()

for elem in g.nodes:
    for node in minSkelet:
        if node == elem[0]:
            print(' - '.join((map(str,node))))
        elif node[::-1] == elem[0]:
            print(' - '.join((map(str,node[::-1]))))