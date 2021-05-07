class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def height(root):
    if root==None:
        return 0
    else:
        hl=height(root.left)
        hr=height(root.right)
        h=max(hl,hr)+1
        return h


N1=Node(1)
N2=Node(2)
N3=Node(3)
N4=Node(4)
N5=Node(5)
N6=Node(6)
N7=Node(7)

N1.left=N2
N2.left=N4
N2.right=N5
N1.right=N3
N5.left=N6
N6.right=N7
#PrintInorder(N1)
#PrintPreorder(N1)
print(height(N1))
