'''
Data: 
City: Praha, Berlín, Paříž, Vídeň, Londýn
LS2021: Praha -> Berlín -> Paříž -> Praha
ZS2020: Praha -> Londýn -> Paříž -> Vídeň
AB111: Vídeň -> Londýn -> Paříž -> Berlín
XYZ007: Praha -> Paříž -> Vídeň
'''

import sys
import re

import graph

g = graph.Graph()

for line in sys.stdin:
    groups = re.match("([A-Z]+|[0-9]+)+:\s(([a-zA-Z]+)(.*|$)?)+", line)
    #list of all couples of nodes that are connected        
    if groups:
        pairOfNodes = groups.group(2).split(" -> ")
        node = tuple(pairOfNodes)
        g = g.addNeighbours(node)
        g.oriented = True

print("graf prehladany do hlbky:", ", ".join(g.DFS()), "\nzvysok sa mi nepodarilo naimplementovat")