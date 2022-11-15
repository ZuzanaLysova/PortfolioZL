'''
Data:
Places: Praha, Berlin, Rim, Pariz, Viden, Londyn, Brno
2018: Praha -> Berlin -> Pariz -> Praha
2019: Praha -> Londyn -> Pariz -> Viden
2020: Viden -> Londyn -> Pariz -> Berlin
2021: Praha -> Pariz -> Viden
'''

import sys
import re

import graph

nodesGraph = graph.Graph()
fullGraph = graph.Graph()

for line in sys.stdin:
    allNodes = re.match("^Places:\s(.*)$", line)
    neighbours = re.match("[0-9]{4}:\s(([a-zA-Z]+)(.*|$)?)+", line)
    # list of all nodes of graph
    if allNodes:
        allGivenNodes = allNodes.group(1).split(", ")
        nodesGraph = nodesGraph.addNode(allGivenNodes)
    #list of all couples of nodes that are connected        
    if neighbours:
        nodesGroup = neighbours.group(1).split(" -> ")
        nodesGroup = tuple(nodesGroup)
        fullGraph = fullGraph.addNeighbours(nodesGroup)
        fullGraph.oriented = True

nodesList = nodesGraph.listOfNodes()
neighDict = fullGraph.listOfNeighbours()

# list of isolated nodes
nodesWithoutEdges = []
nodesHavingNeigh = list(neighDict.keys())
nodesList = nodesList[0]
for node in nodesList:
    if node not in nodesHavingNeigh:
        nodesWithoutEdges.append(node)

nodesWithoutEdgesStr = ', '.join(nodesWithoutEdges)
print(nodesWithoutEdgesStr)