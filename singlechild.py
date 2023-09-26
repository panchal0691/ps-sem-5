# count lead nodes
class Node():
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
def countsinglechildNode(root):
    if root == None:
        return 0
    
    
    if root.left != None and root.right == None:
        return countsinglechildNode(root.left) +1
    if root.left == None and root.right != None:
        return countsinglechildNode(root.right) +1
    if root.left != None and root.right != None:
        return countsinglechildNode(root.left) and countsinglechildNode(root.right)
    
        
        
root= Node(5)

root.left = Node(3)

root.left.right = Node(7)

root.right = Node(3)

root.right.right = Node(13)

print(countsinglechildNode(root))

        
