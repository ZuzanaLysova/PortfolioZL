import sys
from traceback import print_last
from turtle import heading

# Class for tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Class for tree that consists of tree nodes
class AVLTree(object):
    # Add new node to tree and update its height
    def insert(self, root, newValue):
        if root is None:
            return TreeNode(newValue)
        elif root.key <= newValue:
                root.right = self.insert(root.right, newValue)
        else:
            root.left = self.insert(root.left, newValue)
        self.updateHeight(root)
        return self.rotate(root)

    def rotate(self, root):    
        nodeBalance = self.balance(root)
        if nodeBalance > 1:
            if self.balance(root.left)<0:
                root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if nodeBalance < -1:
            if self.balance(root.right)>0:
                root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root

    # Get the height of node when new node is added to tree
    def updateHeight(self, node):
        maxHeight = max(self.height(node.right), self.height(node.left))
        node.height = maxHeight+1

    # Help method to get node height
    def height(self, node):
        if node is not None:
            return node.height
        else:
            return 0

    # Get the balance of node - height(left child) - height(right child)
        # if balance < -1 : left rotation
        # if balance > 1 : right rotation
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left)-self.height(node.right)

    def rotateRight(self, node):
        leftNode = node.left
        newCenter = leftNode.right
        leftNode.right = node
        node.left = newCenter
        self.updateHeight(node)
        self.updateHeight(leftNode)
        return leftNode

    def rotateLeft(self, node):
        rightNode = node.right
        newCenter = rightNode.left
        rightNode.left = node
        node.right = newCenter
        self.updateHeight(node)
        self.updateHeight(rightNode)
        return rightNode

    # Traverse tree pre-order (node, left, right) - using recursion.
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def levelOrder(self,root):
        nodeHeight = self.height(root)
        i = 0
        helpPrintList = []
        while i<nodeHeight:
            self.printLevel(root, i, helpPrintList)
            helpPrintList.append("|")
            i += 1
        return helpPrintList
    
    def printLevel(self, root, level, helpPrintList):
        noChild = "_"
        if root:
            if level == 0:
                helpPrintList.append(root.key)
            else:
                if root.left:
                    self.printLevel(root.left, level-1, helpPrintList)
                else:
                    helpPrintList.append(noChild)
                if root.right:
                    self.printLevel(root.right, level-1, helpPrintList)
                else:
                    helpPrintList.append(noChild)
        for i in range(len(helpPrintList)):
            helpPrintList[i] = str(helpPrintList[i])
        # return helpPrintList
        # print(" ".join(helpPrintList))


# Create instance of AVL Tree
tree = AVLTree()
root = None
# Save numbers from input to list inputNodes = []
inputNodes = []
for line in sys.stdin:
    if line:
        node = int(line)
        inputNodes.append(node)
for node in inputNodes:
    root = tree.insert(root, node)


output = tree.levelOrder(root)
for i in range(len(output)):
    output[i] = str(output[i])
print(" ".join(output))
