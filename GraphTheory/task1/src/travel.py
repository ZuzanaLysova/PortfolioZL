'''
Data:
BRNO, PRAHA, OSTRAVA
brno, praha, olomouc
BRNO -> PRAHA
OSTRAVA -> PRAHA
PRAHA -> BRNO
brno -> praha
olomouc -> praha
praha -> brno
'''

import sys
import re

import graph

nodesGraph = graph.Graph()
capGraph = graph.Graph()
lowGraph = graph.Graph()

for line in sys.stdin:
    groupsCap = re.match("(^[A-Z]+(,\s[A-Z]+|$)+)", line)
    groupsLow = re.match("(^[a-z]+(,\s[a-z]+|$)+)", line)
    neighboursCap = re.match("^([A-Z]+\s->\s[A-Z]+)$", line)
    neighboursLow = re.match("^([a-z]+\s->\s[a-z]+)$", line)
    # only edges of both graphs (cap, low)
    if groupsCap:
        nodesCap = groupsCap.group(1).split(", ")
        nodesGraph = nodesGraph.addNode(nodesCap)
    if groupsLow:
        nodesLow = groupsLow.group(1).split(", ")
        nodesGraph = nodesGraph.addNode(nodesLow)
    # couple of edges of both graphs (cap, low)
    if neighboursCap:
        capGroup = neighboursCap.group(1).split(" -> ")
        # capGroup = tuple(capGroup)
        capGraph = capGraph.addNeighbours(capGroup)
        capGraph.oriented = True
    if neighboursLow:
        lowGroup = neighboursLow.group(1).split(" -> ")
        # lowGroup = tuple(lowGroup)
        lowGraph = lowGraph.addNeighbours(lowGroup)
        lowGraph.oriented = True
else:
    print("End of stdin")

# print(nodesGraph)
# print(capGraph)
# print(lowGraph)

# TODO - doesn't work
print(capGraph.joinGraphs(lowGraph))
# capGraph.joinGraphs(lowGraph)