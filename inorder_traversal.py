class Node():
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
#     def PreOrder(self,data):
#         if self.data.next > self.data:
#             self.left = 
#             print(f{self.data})
    def printInorder(root):
 
        if root:
            printInorder(root.left)

            print(root.data, end=" ")

            printInorder(root.right)   
            
            
root= Node(5)

root.left = Node(3)

root.left.right = Node(7)

root.right = Node(3)

root.right.right = Node(13)
print(printInorder(root))
