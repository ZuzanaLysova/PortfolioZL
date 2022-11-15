'''
Data:
Store: Praha, Berlin, Pariz, Viden, Londyn
Z01: Praha -> Berlin
Z02: Pariz -> Praha
Z03: Praha -> Londyn
Z04: Pariz -> Viden
Z05: Viden -> Londyn
Z06: Pariz -> Berlin
Z07: Praha -> Pariz
Z08: Londyn -> Viden
Z09: Praha -> Londyn
'''

import sys
import re

import graph

g = graph.Graph()

for line in sys.stdin:
    groups = re.match("Z[0-9]+:\s([a-zA-Z]+\s->\s[A-Za-z]+)$", line)
    #list of all couples of nodes that are connected
    if groups:
        nodesGroup = groups.group(1).split(" -> ")
        nodesGroup = tuple(nodesGroup)
        g = g.addNeighbours(nodesGroup)
        g.oriented = True

# print(fullGraph)
outCount = g.nodeDegreeOut()
maxExport = g.sortGraph(outCount, 1)
inCount = g.nodeDegreeIn()
maxImport = g.sortGraph(inCount, 1)

for node in maxExport:
    print(f"Export: {node} ({maxExport[node]})")

for node in maxImport:
    print(f"Import: {node} ({maxImport[node]})")