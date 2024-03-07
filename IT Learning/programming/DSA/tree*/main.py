class TreeNode:
    def __init__(self, val):
        self.data = val
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def preorderTrav(self, node):
        if node == None:
            return []
        else:
            return (node.val + self.inorderTrav(node.left) + self.inorderTrav(node.right))

    def inorderTrav(self, node):
        if node == None:
            return []
        else:
            return (self.inorderTrav(node.left) + node.val + self.inorderTrav(node.right))

    def postorderTrav(self, node):
        if node == None:
            return []
        else:
            return (self.inorderTrav(node.left) + self.inorderTrav(node.right) + node.val)

    def treeHeight(self, node):
        if node == None:
            return 0
        else:
            return 1 + max(self.treeHeight(node.left), self.treeHeight(node.right))

    def insert(self, val, node):
        newNode = TreeNode(val)

        if node == None:
            node = newNode
        else:
            if newNode.data > node.data:
                if node.left == None:
                    node = newNode
                else:
                    self.insert(val, node.left)
            else:
                if node.right == None:
                    node = newNode
                else:
                    self.insert(val, node.right)


if __name__ == '__main__':
    print('hi, i\'ll make a tree in a moment, please wait')
    # myTree = Tree()
    # node0 = myTree.root
    # myTree.inorderTrav(node0)