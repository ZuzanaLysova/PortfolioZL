'''
Employ: Honza, Pepa, Anna, Jarek, Tomas
P01: Honza, Pepa, Anna
P01: Pepa, Anna, Jarek
P01: Pepa, Anna, Jarek, Tomas
P01: Honza, Tomas
'''

import sys
import re
import graph

g = graph.Graph()

for line in sys.stdin:
    groups = re.match("P01:\s(([a-zA-Z]+)(.*|$)?)+", line)
    #list of all couples of nodes that are connected        
    if groups:
        nodesGroup = groups.group(1).split(", ")
        nodesGroup = tuple(nodesGroup)
        g = g.addNeighbours(nodesGroup)

neighDict = g.listOfNeighbours()
complete = g.isComplete(4)
print("Goal:",complete)