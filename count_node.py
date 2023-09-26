# Count the node 

class Node():
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
def countNode(root):
    if root == None :
        return 0
    left = countNode(root.left)
    right = countNode(root.right)
    
    count = left + right +1
    return count


    
        
        
root= Node(5)

root.left = Node(3)

root.left.right = Node(7)

root.right = Node(3)

root.right.right = Node(13)
root.right.right.left = Node(133)


print(countNode(root))

        
