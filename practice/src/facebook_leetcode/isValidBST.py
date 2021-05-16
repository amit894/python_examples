class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def isValidBST(root):
    a=[]
    inOrderTraversal(root,a)
    for i in range(1,len(a)):
        if a[i-1]>=a[i]:
            return False
    return True


def inOrderTraversal(root,a):
    if root:
        inOrderTraversal(root.left,a)
        a.append(root.val)
        inOrderTraversal(root.right,a)

N1=Node(1)
N2=Node(2)
N3=Node(3)
N4=Node(4)
N5=Node(5)
N6=Node(6)

N5.left=N1
N5.right=N4
N4.left=N3
N4.right=N6


print(isValidBST(N5))
