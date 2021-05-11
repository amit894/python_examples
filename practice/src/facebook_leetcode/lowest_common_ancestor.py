class Node:
    def __init__(self,val):
        self.info=val
        self.left=None
        self.right=None


def findLCA(root, v1, v2):
    path1=[]
    path2=[]

    path_to_node(root,v1,path1)
    path_to_node(root,v2,path2)


    if(len(path1)==0 and len(path2)==0):
        return "No Path exists"

    i=0
    while (i<min(len(path1),len(path2))):
        if path1[i]!=path2[i]:
            break
        i+=1
    return path1[i-1].info


def path_to_node(root,v,path):
    if root==None:
        return
    else:
        path.append(root)
        if root.info==v:
            return True
        if ((root.left != None and path_to_node(root.left,v,path)) or
            (root.right!= None and path_to_node(root.right,v,path))):
            return True
        path.pop()
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4, 5) = %d" %(findLCA(root, 4, 5,)))
print("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" %(findLCA(root,3,4)))
print("LCA(2, 4) = %d" %(findLCA(root,2, 4)))
