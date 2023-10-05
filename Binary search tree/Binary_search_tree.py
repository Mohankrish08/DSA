# Creating the Binary search tree class
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Inserting Node function

def InsertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            InsertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            InsertNode(rootNode.rightChild, nodeValue)
    return 'The node added successfully'


# Preorder traversal

def PreOrderTraversal(rootNode):
    if rootNode is None:
        return None
    else:
        print(rootNode.data)
        PreOrderTraversal(rootNode.leftChild)
        PreOrderTraversal(rootNode.rightChild)

# Inorder traversal

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Post order traversal

def PostOrderTraversal(rootNode):
    if not rootNode:
        return None
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Searching the nodeValue

def SearchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The value is found')
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print('The value is found')
        else:
            SearchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == rootNode.data:
            print('The value is found')
        else:
            SearchNode(rootNode.rightNode, nodeValue)




newBst = BSTNode(None)
print(InsertNode(newBst, 70))
print(InsertNode(newBst, 80))
print(InsertNode(newBst, 40))
print(InsertNode(newBst, 20))
print(InsertNode(newBst, 50))
print(InsertNode(newBst, 60))
print(newBst.data)
print(newBst.rightChild.data)
# print(PreOrderTraversal(newBst))
# print(inOrderTraversal(newBst))
print(PostOrderTraversal(newBst))
print(SearchNode(newBst, 100))