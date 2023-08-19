
class TreeNode:

    def __init__(self, value = 0, left = None, right = None) -> None:
        self.val = value
        self.left = left
        self.right = right 
        
        
class BST:

    def __init__(self):
        self.root = None

    def addNode(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.addNodeRecursively(self.root, val)

    def addNodeRecursively(self, current, val):

        if not current:
            node = TreeNode(val)
            return node

        if val < current.val:
            current.left = self.addNodeRecursively(current.left, val)
        else:
            current.right = self.addNodeRecursively(current.right, val)
            
        return current
    
    def printInorderTree(self):
        self.printInorderRecursively(self.root)

    def printInorderRecursively(self, root):
        if not root:
            # print("Empty")
            return 
        
        self.printInorderRecursively(root.left)
        print(root.val)
        self.printInorderRecursively(root.right)

    def printAllLeaves(self):
        self.printAllLeavesRecursively(self.root)

    def printAllLeavesRecursively(self, current):
        if not current:
            return 
        
        if not current.left and not current.right:
            print(current.val)
            return
        
        self.printAllLeavesRecursively(current.left)
        self.printAllLeavesRecursively(current.right)


    
root = BST()
root.addNode(4)
root.addNode(3)
root.addNode(5)
root.addNode(2)
root.addNode(510)
root.addNode(15)
root.addNode(-5)
root.printAllLeaves()

    

            