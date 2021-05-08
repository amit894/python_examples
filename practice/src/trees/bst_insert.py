class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insertNode(root,node):
    if root is None:
        return node
    else:
        if (node.data<root.data):
            root.left=insertNode(root.left,node)
        else:
            root.right=insertNode(root.right,node)
    return root

def inOrderTraversal(root):
    if root==None:
        return
    else:
        inOrderTraversal(root.left)
        print(root.data,end=" ")
        inOrderTraversal(root.right)


N1=Node(1)
N2=Node(2)

N3=Node(3)
N4=Node(4)

N6=Node(6)
N7=Node(7)

N5=Node(5)
N8=Node(8)

insertNode(None,N1)
print("De Limiter")
inOrderTraversal(N1)
insertNode(N1,N2)
print("De Limiter")
inOrderTraversal(N1)
insertNode(N1,N8)
insertNode(N1,N6)
insertNode(N1,N7)
insertNode(N1,N5)
insertNode(N1,N4)
insertNode(N1,N3)
print("De Limiter")
inOrderTraversal(N1)
