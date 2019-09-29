from __future__ import print_function


# Class Node
class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


# Class Binary Search Tree
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        new_node = Node(label, None)

        if self.empty():
            self.root = new_node
        else:
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)

    def getNode(self, label):
        curr_node = None
        if not self.empty():
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root=None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.getRoot()
        if not self.empty():
            while curr_node.getRight() is not None:
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root=None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.getRoot()
        if not self.empty():
            curr_node = self.getRoot()
            while curr_node.getLeft() is not None:
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if node == node.getParent().getRight():
            return True
        return False

    def __reassignNodes(self, node, newChildren):
        if newChildren is not None:
            newChildren.setParent(node.getParent())
        if node.getParent() is not None:
            if self.__isRightChildren(node):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)

    def traversalTree(self, traversalFunction=None, root=None):
        if traversalFunction is None:
            return self.__InOrderTraversal(self.root)
        else:
            return traversalFunction(self.root)

    # This Function evaluate the Ancestor common
    def findLCA(self, root, n1, n2):
        if root is None:
            return None
        if root.getLabel() > n1 and root.getLabel() > n2:
            return self.findLCA(root.getLeft(), n1, n2)
        if root.getLabel() < n1 and root.getLabel() < n2:
            return self.findLCA(root.getRight(), n1, n2)

        return root

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str


# This Function ordened the Tree in proerden form
def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList


