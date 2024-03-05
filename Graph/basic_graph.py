# creating basic graph

class TreeNode:
    
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
            print(ret)
        return ret
    
    def addChildren(self, TreeNode):
        self.children.append(TreeNode)

# creating instance for TreeNode
        
tree = TreeNode('Drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])
tree.addChildren(cold)
tree.addChildren(hot)
coffee = TreeNode("Coffee", [])
tea = TreeNode("tea", [])
coke = TreeNode("coke", [])
sprite = TreeNode("sprite", [])
tree.addChildren(tea)
tree.addChildren(coffee)
tree.addChildren(sprite)
tree.addChildren(coke)
print(tree)