'''
Data:
Employ: Honza, Pepa, Anna, Jarek, Tomas
Honza -> Pepa
Pepa -> Anna
Anna -> Jarek
Anna -> Pepa
Pepa -> Anna
Jarek -> Anna
Tomas -> Honza
Honza -> Tomas
'''

import sys
import re
import graph

g = graph.Graph()

for line in sys.stdin:
    groups = re.match("^([A-Za-z]+\s->\s[A-Za-z]+)$", line)
    #list of all couples of nodes that are connected        
    if groups:
        pairOfNodes = groups.group(1).split(" -> ")
        g = g.addNeighbours(pairOfNodes)
        g.oriented = True

notMutual = g.isMutual()
for x in notMutual:
    xStr = ' -> '.join(x[::-1])
    print(xStr)