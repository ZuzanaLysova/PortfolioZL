from re import A


class Graph:
    def __init__(self, nodes=[], oriented=False):
        self.nodes = nodes
        self.oriented = oriented
        # self.value = value

    def __repr__(self):
        return f"Graph(nodes={self.nodes})"

# Create new graph with updated list of graph nodes.
    def addNode(self, node):
        return Graph(nodes=self.nodes + [node])

# Create new graph with list of couples of nodes that are connected.
    def addNeighbours(self, node):
        return Graph(nodes=self.nodes + [node])

# Returns the neigbours of nodes ({node: [[node that is connected with it with, value of edge],[],...]}).
    def listOfNeighboursValued(self):
        neighDict = {}
        if not self.oriented:
            for node in self.nodes:
                oneNode = node[0]
                i=0
                while i<len(oneNode):
                    neighDict[oneNode[i]]=[]
                    i += 1
            for elem in self.nodes:
                oneNode = elem[0]
                nodesValue = elem[1]
                for i in range(len(oneNode)):
                    j=i+1
                    valueList = []
                    listI = []
                    listJ = []
                    while j < len(oneNode):
                        valueList.append(oneNode[i])
                        valueList.append(oneNode[j])
                        valueList.append(nodesValue)
                        listI.append(valueList[0])
                        listI.append(valueList[2])
                        listJ.append(valueList[1])
                        listJ.append(valueList[2])
                        neighDict.setdefault(oneNode[i],[]).append(listJ)
                        neighDict.setdefault(oneNode[j],[]).append(listI)
                        j += 1
        else:
            for node in self.nodes:
                i=0
                while i<len(node):
                    neighDict[node[i]]=[]
                    i += 1 
            for node in self.nodes:
                for i in range(len(node)-1):
                    j=i+1
                    neighDict.setdefault(node[i],[]).append(node[j])
        return neighDict
        # print(neighDict)

    def listOfNeighboursNotValued(self):
        neighDict = {}
        if not self.oriented:
            for node in self.nodes:
                i=0
                while i<len(node):
                    neighDict[node[i]]=[]
                    i += 1
            for node in self.nodes:
                for i in range(len(node)):
                    j=i+1
                    while j < len(node):
                        neighDict.setdefault(node[i],[]).append(node[j])
                        neighDict.setdefault(node[j], []).append(node[i])
                        j += 1
        else:
            for node in self.nodes:
                i=0
                while i<len(node):
                    neighDict[node[i]]=[]
                    i += 1 
            for node in self.nodes:
                for i in range(len(node)-1):
                    j=i+1
                    neighDict.setdefault(node[i],[]).append(node[j])
        return neighDict

# Returns the node couples we should visit to visit all nodes with minimum sum of values.
    def minSkelet(self):
        neighDict = self.listOfNeighboursValued()
        listOfNodes = []
        for node in neighDict:
            for nodeValue in neighDict[node]:
                listOfNodes.append([node,nodeValue[0],nodeValue[1]])
        sortedListOfNodes = sorted(listOfNodes, key=lambda x: x[2])
        markedNodes = []
        minSkeletList = []
        for node in sortedListOfNodes:
            # print("ONE NODE", node[0], node[1], "VALUE", node[2])
            if node[1] not in markedNodes:
                markedNodes.append(node[0])
                markedNodes.append(node[1])
                minSkeletList.append([node[0],node[1]])
        # print(minSkeletList)
        return minSkeletList

# Breadth First Search (prehladavanie grafu do sirky)
    def BFS(self):
        visited = set()
        queue = []
        listBFS = []
        neighDict = self.listOfNeighboursNotValued()
        startNode = list(neighDict.keys())[0]
        # print(startNode)
        queue.append(startNode)
        visited.add(startNode)
        # print("QUEUE", queue, "VISITED", visited, "FIRST", startNode)
        while queue:
            currentNode = queue.pop(0)
            listBFS.append(currentNode)
            for neigh in neighDict[currentNode]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)
        return listBFS
        # print("BFS:", listBFS)

# TODO
    def deleteOrientation(self):
        nodeGroups = self.nodes
        nodeCouples = []
        # for i in range(len(self.nodes)):
        for group in nodeGroups:
            for i in range(len(group)-1):
                # print("output", group[i])
                node1 = group[i]
                node2 = group[i+1]
                newNodeCouple = tuple([node1,node2])
                if newNodeCouple not in nodeCouples:
                    nodeCouples.append(tuple(newNodeCouple))
                if newNodeCouple[::-1] not in nodeCouples:
                    nodeCouples.append(tuple(newNodeCouple[::-1]))
            # print("NEXT")
        # print("NODES...", nodeCouples)
        return nodeCouples

            # print("NODE", node)

# Depth First Search (prehladavanie grafu do hlbky)
    def DFS(self):
        visited = []
        edges = self.deleteOrientation()
        startNode = edges[0][0]
        # print(startNode)
        self.DFSRecursion(startNode, visited, edges)
        return visited

    def DFSRecursion(self, node, visited, edges):
        if node not in visited:
            visited.append(node)
            for edge in edges:
                for node in edge:
                    if node not in visited:
                        self.DFSRecursion(node, visited, edges)
        return visited
# artikulace
    def articulation(self):
        dictOfNodes = self.BFS()
        dictOfNeighbors = self.listOfNeighboursValued()
        # dictOfNodes = listOfNodes[::-1] # reversed
        # print(dictOfNodes)
        for node in dictOfNodes:
            for i in range(len(dictOfNodes[node])):
                # print("icko", dictOfNodes[node][i])
                # for i in range(len(value)):
                #     print("icko", i)
                if(dictOfNodes[node][2]==None):
                    firstNode = node
        # print("FIRST:",firstNode)
        for keyNode in dictOfNeighbors:
            print("first", firstNode)
            # print("key", keyNode, "first", firstNode)
            listOfNeighbors = []
            if firstNode == keyNode:
                listOfNeighbors.append(dictOfNeighbors[keyNode])
                # print(keyNode, firstNode, listOfNeighbors)
                for node in dictOfNodes:
                    if dictOfNodes[node][2] == firstNode:
                        firstNode = node
                    print(listOfNeighbors)
                    print("LOOK", dictOfNodes[keyNode])
                    if dictOfNodes[node][2] == None:
                        for n in range(len(listOfNeighbors[0])):
                            if node == listOfNeighbors[0][n]:
                                lowNode = min(dictOfNodes[keyNode][0], dictOfNodes[node][0])
                                dictOfNodes[node][1] = lowNode
                                break
                    else:
                        for myNode in dictOfNodes:
                            for n in range(len(listOfNeighbors[0])):
                                if dictOfNodes[keyNode][2] == myNode:
                                    if node == listOfNeighbors[0][n]:
                                        lowNode = min(dictOfNodes[keyNode][0], dictOfNodes[node][0], dictOfNodes[myNode][1])
                                        dictOfNodes[node][1] = lowNode
                                        break
                                    else:
                                        lowNode = min(dictOfNodes[keyNode][0], dictOfNodes[myNode][1])
                                        dictOfNodes[node][1] = lowNode
                                        break
        print(dictOfNodes)
        # for i in range(len(dictOfNodes)):
        #     if i-1<0: # node has no successor (naslednik)
        #         if i+2<len(dictOfNodes): # we can look on node out of tree
        #             lowNode = min(dictOfNodes[i][1], dictOfNodes[i+2][1])
        #     elif i+2<len(dictOfNodes):
        #             lowNode = min(dictOfNodes[i][1], dictOfNodes[i+2][1], dictOfNodes[i+1][2])
        #     else:
        #         lowNode = min(dictOfNodes[i][1], dictOfNodes[i+1][2])
        #     dictOfNodes[i][2] = lowNode
        # print(dictOfNodes)

# Returns list of all couple of nodes in not oriented graph [(A-B),(B-A),(A-C),(C-A)...].
    def listOfAllConnectedNodes(self):
        listOfNodes=[]
        for node in self.nodes:
            listOfNodes.append(node)
        print(listOfNodes)
        listOfReversedNodes = []
        for node in listOfNodes:
            listOfReversedNodes.append(node[::-1])
        print(listOfReversedNodes)
        listOfAllNodes = listOfNodes + listOfReversedNodes
        print(listOfAllNodes)
        # return listOfNodes

    def wander(self):
        neighDict = self.listOfNeighboursNotValued()
        # print(neighDict)
        visited = set()
        wanderList = []
        for node in neighDict:
            key = node
            break
        # print(key)
        counter = 0
        lastNode = list(neighDict.keys())[len(neighDict)-1]
        while key != lastNode and counter<=50:
            if key not in visited:
                visited.add(key)
                for neigh in neighDict[key]:
                    if neigh not in visited:
                        # print("KEY", key, "NEIGH", neigh, "NEIGHDICTKEY", neighDict[key])
                        wanderList.append([key, neigh])
                        # print("wander list", wanderList)
                        key = neigh
                        break
                    counter += 1
                    if neigh not in visited:
                        visited.add(neigh)
                        wanderList.append([key,neigh])
                        break
                    # print(wanderList)
                key = neigh
            counter += 1
        if counter >= 50:
            print("NIE JE CESTY VON")
            return
        # print("WANDER LIST", wanderList)
        else:
            return wanderList

# wander2 and wander3 are bad, I just tried
    def wander2(self):
        neighDict = self.listOfNeighboursNotValued()
        inNodes = {}
        outNodes = {}
        # for neigh in neighDict:
        #     inNodes[neigh] = []
        #     outNodes[neigh] = []
        # print("IN", inNodes, "OUT", outNodes)
        wanderList = []
        lastNode = list(neighDict.keys())[len(neighDict)-1]
        actualNode = list(neighDict.keys())[0]
        counter = 0
        # print("LAST", lastNode, "ACTUAL", actualNode)
        while actualNode != lastNode and counter<=50:
            # print("LAST", lastNode, "ACTUAL", actualNode)
            if actualNode not in outNodes:
                outNodes[actualNode] = []
                for neigh in neighDict[actualNode]:
                    if neigh not in outNodes[actualNode]:
                        # outNodes[actualNode].append(neigh)
                        # if neigh not in inNodes:
                        #     inNodes[neigh] = []
                        # if actualNode not in inNodes[neigh]:
                        # inNodes[neigh].append(actualNode)
                        # inNodes.add(neigh)
                        wanderList.append([actualNode, neigh])
                        print("ACTUAL", actualNode, "NEIGH", neigh)
                        actualNode = neigh
                        print("LAST ACTUAL", actualNode, "LAST NEIGH", neigh)
                        break
                    counter += 1
                    if neigh not in outNodes[actualNode]:
                        outNodes[actualNode].append(neigh)
                        wanderList.append([actualNode, neigh])
                        break
                #     # if neigh not in inNodes:
                #     #     inNodes[neigh] = []
                #     # if actualNode not in inNodes[neigh]:
                #     # inNodes[neigh].append(actualNode)
                #     wanderList.append([actualNode, neigh])
                #     break
                # if neigh not in inNodes:
                #     inNodes.add(neigh)
                #     wanderList.append([actualNode,neigh])
                #     break
                # wanderList.append([actualNode,neigh])
                print("OUTNODES", outNodes)
                actualNode = neigh
                # print("LAST ACTUAL", actualNode, "LAST NEIGH", neigh)
            counter += 1
        if counter >= 50:
            print("nie je cesty von")
            return
        else:
            return wanderList


    def wander3(self):
        neighDict = self.listOfNeighboursNotValued()
        visited = set()
        reversedNodes = []
        for node in self.nodes:
            reversedNodes.append(node[::-1])
        allNodes = self.nodes + reversedNodes
        # print("reversed:",reversedNodes)
        # print(outNodes)
        print("ALL NODES:", allNodes)
        lastNode = list(neighDict.keys())[len(neighDict)-1]
        actualNode = list(neighDict.keys())[0]
        counter = 0
        # for i in range(len(neighDict[actualNode])):
        #     print(neighDict[actualNode][i])
        while actualNode != lastNode and counter<=50:
            for i in range(len(neighDict[actualNode])):
                print("X")
                coupleList = []
                couple = tuple()
                coupleList = [actualNode, neighDict[actualNode][i]]
                couple = tuple(coupleList)
                print("Couple", couple)
                if (couple not in visited and couple[::-1] not in visited) and couple in allNodes:
                    visited.add(couple)
                    print("VISITED:",visited)
                    actualNode = neighDict[actualNode][i]
                    counter += 1
                    break
                else:
                    if i < len(neighDict[actualNode]):
                        actualNode = neighDict[actualNode][i+1]
                    else:
                        break
                # actualNode = node
            counter += 1
        if counter >= 50:
            print("nie je cesty von")
            return
        else:
            return visited
        # print("all", allNodes)
        # print("visited", visited)