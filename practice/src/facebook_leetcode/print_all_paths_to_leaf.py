class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printAllLeafPaths(root,path,pathlen):
    if root==None:
        return "Empty Tree"
    else:
        if pathlen<len(path):
            path[pathlen]=root.val
        else:
            path.append(root.val)
        pathlen+=1
        if root.left==None and root.right==None:
            printpath(path,pathlen)
        if root.left:
            printAllLeafPaths(root.left,path,pathlen)
        if root.right:
            printAllLeafPaths(root.right,path,pathlen)

def printpath(path,pathlen):
    for i in range(pathlen):
        print(str(path[i]), end=" ")
    print(" ")

path=[]
N1=Node(1)
N1.left=Node(2)
N1.right=Node(3)
printAllLeafPaths(N1,path,0)
