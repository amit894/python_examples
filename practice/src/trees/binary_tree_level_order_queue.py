class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelOrder(root):
    q1=[]
    if root==None:
        return
    else:
        q1.append(root)
        while(len(q1)>0):
            node=q1.pop(0)
            print(node.data,end=" ")
            if(node.left):
                q1.append(node.left)
            if(node.right):
                q1.append(node.right)

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

levelOrder(N1)
