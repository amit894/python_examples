class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

a=[]

def inOrderTraversetoArray(root,a):
    if(root):
        inOrderTraversetoArray(root.left,a)
        a.append(root.data)
        inOrderTraversetoArray(root.right,a)

def inOrderTraverse(root):
    if(root):
        inOrderTraverse(root.left)
        print(root.data,end=" ")
        inOrderTraverse(root.right)

def inOrderAddition(root):
    if(root):
        inOrderAddition(root.left)
        root.data=a.pop(0)
        inOrderAddition(root.right)


def partition(A,low,high):
    pivot=A[high]
    i=low-1
    for j in range(low,high):
        if(A[j]<=pivot):
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return (i+1)

def quick_sort(a,low,high):
    if len(a)==1:
        return a
    elif high > low:
        pi=partition(a,low,high)
        quick_sort(a,pi+1,high)
        quick_sort(a,low,pi-1)

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

inOrderTraversetoArray(N1,a)
print("De limiter")
print(a)
print("De limiter")
quick_sort(a,0,len(a)-1)
print(a)
inOrderAddition(N1)
print("De limiter")
inOrderTraverse(N1)
