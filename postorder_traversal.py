class Node():
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
#     def PreOrder(self,data):
#         if self.data.next > self.data:
#             self.left = 
#             print(f{self.data})
def printPostorder(root):
 
    if root:
        printPostorder(root.left)

        print(root.val, end=" "),

        printPostorder(root.right)   
            
            
root= Node(5)

root.left = Node(3)

root.left.right = Node(7)

root.right = Node(3)

root.right.right = Node(13)
print(printPostorder(root))
