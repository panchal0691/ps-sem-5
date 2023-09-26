# count lead nodes
class Node():
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
def countleafNode(root):
    if root == None :
        return 0
    if (root.left == None and root.right == None):
        return 1
    else:
        return countleafNode(root.left) + countleafNode(root.right)


    
        
        
root= Node(5)

root.left = Node(3)

root.left.right = Node(7)

root.right = Node(3)

root.right.right = Node(13)


print(countleafNode(root))

        
