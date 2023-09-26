class Node():
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
#     def PreOrder(self,data):
#         if self.data.next > self.data:
#             self.left = 
#             print(f{self.data})
def printPreorder(root):
 
    if root:
        print(root.val, end=" "),

        printPreorder(root.left)

        
        printPreorder(root.right)   
            
            
root= Node(5)

root.left = Node(3)

root.left.right = Node(7)

root.right = Node(3)

root.right.right = Node(13)
print(printPreorder(root))
