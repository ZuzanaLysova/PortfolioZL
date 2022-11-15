import math


class Graph:
    def __init__(self, nodes=[], oriented=False):
        self.nodes = nodes
        self.oriented = oriented

    def __repr__(self):
        return f"Graph(nodes={self.nodes})"

# Create new graph with updated list of graph nodes.
    def addNode(self, node):
        return Graph(nodes=self.nodes + [node])

# Create new graph with list of couples of nodes that are connected.
    def addNeighbours(self, node):
        return Graph(nodes=self.nodes + [node])

# Returns list of all nodes in graph no matter if they have edges or not.
    def listOfNodes(self):
        listOfNodes = []
        for node in self.nodes:
            listOfNodes.append(node)
        return listOfNodes

# Returns the neigbours of nodes ({node: [nodes that are connected with it]}).
    def listOfNeighbours(self):
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
                    nodesList = []
                    # listI = []
                    # listJ = []
                    while j < len(oneNode):
                        valueList.append(oneNode[i])
                        valueList.append(oneNode[j])
                        valueList.append(nodesValue)
                        # print(valueList)
                        # nodesList.append(valueList[0])
                        nodesList.append(valueList[1])
                        nodesList.append(valueList[2])
                        # listI.append(valueList[0])
                        # listI.append(valueList[2])
                        # listJ.append(valueList[1])
                        # listJ.append(valueList[2])
                        neighDict.setdefault(oneNode[i],[]).append(nodesList)
                        # neighDict.setdefault(oneNode[j],[]).append(listI)
                        j += 1
        return neighDict
        # print(neighDict)

# List of parents?
    def listOfParentsValuedOriented(self):
        parentDict = {}
        for node in self.nodes:
            oneNode = node[0]
            i=0
            while i<len(oneNode):
                parentDict[oneNode[i]]=[]
                i += 1
        for elem in self.nodes:
            oneNode = elem[0]
            nodesValue = elem[1]
            print(oneNode, nodesValue)
            for i in range(len(oneNode)):
                    j=i+1
                    valueList = []
                    nodesList = []
                    while j < len(oneNode):
                        valueList.append(oneNode[i])
                        valueList.append(oneNode[j])
                        valueList.append(nodesValue)
                        nodesList.append(valueList[0])
                        nodesList.append(valueList[2])
                        parentDict.setdefault(oneNode[j],[]).append(nodesList)
                        j += 1
        # print(parentDict)
        return parentDict


# Returns the number of edges that goes from/to each node in not oriented graph.
    def nodeDegree(self):
        nodesDict = {}
        for node in self.nodes:
            i=0
            while i<len(node):
                nodesDict[node[i]]=0
                i += 1
        for node in self.nodes:
            for i in range(len(node)):
                count = nodesDict[node[i]]
                # print(f"i: {i}, {node[i]}, count: {count}, len: {len(node)}")
                if node[i] in nodesDict:
                    count += len(node)-1
                    nodesDict[node[i]] = count
        # print(nodesDict)
        return nodesDict

# Find out if all nodes are connected to each other with an edge in not oriented graph (if graph is complete).
    def isComplete(self):
        allNodes = set()
        isCompleteList = []
        notConnectedNodes = []
        for node in self.nodes:
            allNodes.add(node[0][0])
            allNodes.add(node[0][1])
        # print("list", allNodes)
        # print("FIRST", firstNode)
        for oneNode in allNodes:
            searchedNodes = set()
            searchedNodes.add(oneNode)
            for node in self.nodes:
                # for couple in node:
                if oneNode != node[0][0] and oneNode == node[0][1]:
                    searchedNodes.add(node[0][0])
                if oneNode != node[0][1] and oneNode == node[0][0]:
                    searchedNodes.add(node[0][1])
                # print(searchedNodes)
            if len(searchedNodes) == len(allNodes):
                isCompleteList.append([oneNode, True])
            else:
                isCompleteList.append([oneNode, False])
        # print("List", isCompleteList)
        for result in isCompleteList:
            if result[1] is False:
                notConnectedNodes.append(result[0])
                # print(notConnectedNodes)
                # return False
        if notConnectedNodes:
            print("NOT CONNECTED NODES:", notConnectedNodes)
            return False
        else:
            return True

    def EulerGraph(self):
        if self.isComplete():
            print("Graph is complete, it can be solved with this algorithm")
        else:
            print("Graph is not complete, it cannot be solved with this algorithm.")

# Find out if all values of edges are more than 0
    def allEdgesPositive(self):
        # for node in self.nodes:
        if any(node[1] < 0 for node in self.nodes):
            return False
        else:
            return True

# Find the shortest path to all of the nodes
    def DijkstrAlgo(self):
        if self.allEdgesPositive():
            nodesDict = {}
            # parentDict = self.listOfParentsValuedOriented()
            neighDict = self.listOfNeighboursValued()
            # print("DICT:", parentDict)
            firstNode = list(neighDict.keys())[0]
            neigh = None
            path = math.inf
            pathFirstNode = 0
            for node in neighDict:
                if node == firstNode:
                    nodesDict[node] = list([neigh, pathFirstNode])
                else:
                    nodesDict[node] = list([neigh, path])
            nodeList = []
            for node in nodesDict:
                for neigh in neighDict:
                    if node == neigh:
                        for n in neighDict[node]:
                            if n[1]+nodesDict[n[0]][1]<nodesDict[node][1]:
                                    nodesDict[node][0] = n[0]
                                    nodesDict[node][1] = n[1] + nodesDict[n[0]][1]
            for node in nodesDict:
                nodeList.append([nodesDict[node][0], node, int(nodesDict[node][1])])
            return nodeList
        else:
            print("GRAF SA NEDA TYMTO SPOSOBOM VYRIESIT")

# Print the result of Dijkstr algorithm
    def printDijkstr2(self):
        nodesList = self.DijkstrAlgo()
        neighDict = self.listOfNeighboursValued()
        allNodes = []
        for neigh in neighDict:
            allNodes.append(neigh)
        for oneNode in allNodes:
            # print("ONE", oneNode)
            for node in nodesList:
                if node[0]==oneNode:
                    print(f"{node[0]} -> {node[1]}: {node[2]}m")
        # print(allNodes)