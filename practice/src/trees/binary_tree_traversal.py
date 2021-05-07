class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def PrintInorder(root):
    if root!=None:
        PrintInorder(root.left)
        print(root.data,end=" ")
        PrintInorder(root.right)

def PrintPreorder(root):
    if root!=None:
        print(root.data,end=" ")
        PrintPreorder(root.left)
        PrintPreorder(root.right)

def PrintPostorder(root):
    if root!=None:
        PrintPostorder(root.left)
        PrintPostorder(root.right)
        print(root.data,end=" ")

N1=Node(1)
N2=Node(2)
N3=Node(3)
N4=Node(4)
N5=Node(5)

N1.left=N2
N2.left=N4
N2.right=N5
N1.right=N3
#PrintInorder(N1)
#PrintPreorder(N1)
PrintPostorder(N1)

# Perfect Binary Tree : A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.
# Balanced Binary Tree : A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes.
# Complete Binary Tree: A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible
