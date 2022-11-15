'''
Data: 
City: Praha, Berlin, Pariz, Viden, Londyn
LS2021: Praha -> Berlin -> Pariz -> Praha
ZS2020: Praha -> Londyn -> Pariz -> Viden
AB111: Viden -> Londyn -> Pariz -> Berlin
XYZ007: Praha -> Pariz -> Viden
'''

import sys
import re

import graph

g = graph.Graph()

for line in sys.stdin:
    neighbours = re.match("[A-Z]+[0-9]+:\s(([a-zA-Z]+)(.*|$)?)+", line)
    #list of all couples of nodes that are connected        
    if neighbours:
        nodesGroup = neighbours.group(1).split(" -> ")
        nodesGroup = tuple(nodesGroup)
        g = g.addNeighbours(nodesGroup)
        g.oriented = True

neighDict = g.listOfNeighbours()
duplicates = g.findDuplicateNodes()
duplicates = sorted(duplicates)
for dupe in duplicates:
    print(dupe)