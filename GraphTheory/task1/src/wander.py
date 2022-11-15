'''
Data:
Guideposts: Keprnik, Pocaply, Strekov, Rovina, Mandava, Satalice
T01: Keprnik -> Pocaply -> Strekov -> Strekov -> Rovina
T02: Satalice -> Keprnik -> Mandava -> Mandava
T03: Pocaply -> Satalice -> Keprnik -> Satalice
T04: Strekov -> Mandava -> Pocaply
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
loops = g.loops()
loopsStr = ', '.join(loops)
print(loopsStr)