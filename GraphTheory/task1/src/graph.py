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

# Return the number of edges that goes from node in oriented graph.
    def nodeDegreeOut(self):
        nodesDictOut = {}
        for node in self.nodes:
            i=0
            while i<len(node):
                nodesDictOut[node[i]]=0
                i += 1
        for node in self.nodes:
            for i in range(len(node)-1):
                count = nodesDictOut[node[i]]
                count += 1
                nodesDictOut[node[i]] = count
        # print(nodesDictOut)
        return nodesDictOut

# Return the number of edges that comes to node in oriented graph.
    def nodeDegreeIn(self):
        nodesDictIn = {}
        for node in self.nodes:
            i=0
            while i<len(node):
                nodesDictIn[node[i]]=0
                i += 1
        for node in self.nodes:
            i = len(node)-1
            while i>0:
                count = nodesDictIn[node[i]]
                count += 1
                nodesDictIn[node[i]] = count
                i -= 1
        # print(nodesDictIn)
        return nodesDictIn

# Sort the values descending and print results. Parameter top is the amount of results we want to print.
    def sortGraph(self, dict, top):
        sortedValues = sorted(dict.values(), reverse=True)[:top]  
        sortedDict = {}
        for i in sortedValues:
            for k in dict.keys():
                if dict[k] == i:
                    sortedDict[k] = dict[k]
        # print(sorted_dict)
        return sortedDict

# Make set of a list of neighbours - remove duplicate nodes for each node ({node: [unique nodes that are connected with it]}).
    def removeDuplicateNodes(self):
        neighDict = self.listOfNeighbours()
        for node in neighDict:
            neighDict[node] = set(neighDict[node])
        return neighDict

# Find out if graph has more edges between 2 nodes (if node is more times in list of neighbours).
    def isSimpleGraph(self):
        neighDict = self.listOfNeighbours()
        for node in neighDict:
            if any(neighDict):
                len(neighDict[node]) != len(set(neighDict[node]))
                return False
            else:
                return True

# Returns list of nodes that have more than 1 edge between each other.
    def findDuplicateNodes(self):
        neighDict = self.listOfNeighbours()
        newList = []
        dupeList = []
        for node in neighDict:
            for i in range(len(neighDict[node])):
                appendStr = node + " -> " + neighDict[node][i]
                if appendStr not in newList:
                    newList.append(appendStr)
                else:
                    dupeList.append(appendStr)
        return dupeList

# Find out if all nodes are connected to each other with an edge in not oriented graph (if graph is complete).
    def isComplete(self, numberOfNodes):
        neighDict = self.listOfNeighbours()
        self.removeDuplicateNodes()
        for node in neighDict:
            neighDict[node] = len(neighDict[node])
        if any(neighDict)<numberOfNodes:
            return False
        else:
            return True

# Find if any key is same as value in neighbour dictionary and return these keys.
    def loops(self):
        neighDict = self.listOfNeighbours()
        loopsList = []
        for node in neighDict:
            for i in range(len(neighDict[node])):
                if node == neighDict[node][i]:
                    loopsList.append(node)
        return loopsList

# Find out if there are both-way edges (A->B and B->A).
    def isMutual(self):
        # neighDict = self.listOfNeighbours()
        # neighList = []
        # for node in neighDict:
        #     for i in range(len(neighDict[node])):
        #         x = [node, neighDict[node][i]]
        #         neighList.append(x)
        # for i in range(len(neighList)):
        #     neighList[i] = tuple(neighList[i])
        # neighList= list(set(neighList))
        newList=[]
        neighList=self.nodes
        # print("NEIGHLIST",neighList)
        for x in neighList:
            # print("x",x,"-1", x[::-1])
            if x[::-1] not in neighList:
                newList.append(x)
        return newList

# Create new graph that consists of unification of 2 graphs (G1 U G2).
# TODO - doesnt work
    def joinGraphs(self, graph):
        tempGraph = []
        for node in self.nodes:
            tempGraph.append(node)
        for node in graph.nodes:
            tempGraph.append(node)
        listOfNodes = []
        for node in tempGraph:
            nodeStr = ' -> '.join(node)
            listOfNodes.append(nodeStr)
        # print(listOfNodes)
        newGraph = []
        for i in range(len(listOfNodes)):
            j = i+1
            while j < len(listOfNodes):
                # print("i", i, ", ", listOfNodes[i], listOfNodes[i].lower(), "j", j, ", ", listOfNodes[j], listOfNodes[j].lower())
                if listOfNodes[i].lower() == listOfNodes[j].lower():
                    newGraph.append(listOfNodes[i])
                    # listOfNodes.remove(listOfNodes[i])
                    listOfNodes.remove(listOfNodes[j])
                    # j -= 1
                    break
                if listOfNodes[i].lower() != listOfNodes[j].lower():
                    newGraph.append(listOfNodes[i])
                    break
                j += 1
            # newGraph = newGraph.append(nodeStr)
        # lowNeigh = []
        # capNeigh = []
        # for node in tempGraph:
        #     lowNodes = []
        #     capNodes = []
        #     if node not in newGraph:
        #         for n in node:
        #             lowNodes.append(n.lower())
        #         for n in node:
        #             capNodes.append(n.upper())
        #         lowNeigh.append(lowNodes)
        #         capNeigh.append(capNodes)
        # print(lowNeigh)
        # print(capNeigh)
        # for node in tempGraph:
        #     if node in capNeigh:
        #         print(node)
        #         capNeigh.remove(node)
        #         if node in lowNeigh:
        #             lowNeigh.remove(node)
        #         # newGraph = newGraph.append(node)
        #     elif node in lowNeigh:
        #         print(node)
        #         lowNeigh.remove(node)
        #         if node in capNeigh:
        #             capNeigh.remove(node)

                # newGraph = newGraph.append(node)
        # for node in graph.nodes:
        #     tempList = []
        #     for n in node:
        #         nodeCap = n.upper()
        #         tempList.append(nodeCap)
        #         tempTuple = tuple(tempList)
        #         if node not in graph.nodes:
        #             newGraph.append(n)
        #     print(tempTuple)
        # print(tempGraph)
        return newGraph