class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def minNumber(root):
    if root==None:
        return "Empty Tree"
    else:
        current_node=root
        while(current_node):
            prev=current_node
            current_node=current_node.left
        return prev.data

def maxNumber(root):
    if root==None:
        return "Empty Tree"
    else:
        current_node=root
        while(current_node):
            prev=current_node
            current_node=current_node.right
        return prev.data

def insertNode(root,node):
    if root==None:
        return node
    else:
        if node.data<root.data:
            root.left=insertNode(root.left,node)
        else:
            root.right=insertNode(root.right,node)
    return root

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.data,end=" ")
        inOrderTraversal(root.right)

N1=Node(1)
N2=Node(2)
N3=Node(3)
N4=Node(4)
N5=Node(5)
N6=Node(6)
N7=Node(7)

root=None
root=insertNode(root,N1)
root=insertNode(root,N2)
root=insertNode(root,N3)
root=insertNode(root,N4)
root=insertNode(root,N5)
root=insertNode(root,N6)
root=insertNode(root,N7)

inOrderTraversal(root)
print("de limiter")
print(minNumber(root))
print("de limiter")
print(maxNumber(root))
