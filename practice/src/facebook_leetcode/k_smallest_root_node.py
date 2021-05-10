class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(root,val):
    if root==None:
        return(Node(val))
    else:
        if(val<=root.val):
            root.left=insert(root.left,val)
        else:
            root.right=insert(root.right,val)
    return root


def kthSmallest(root,k):
    s1=[]
    x=inorder(root,s1)
    if(k<=len(x)):
        return x[k-1].val


def inorder(root,s1):
    if root==None:
        return
    else:
        inorder(root.left,s1)
        s1.append(root)
        inorder(root.right,s1)
    return s1

def inOrderTraversal(root):
    if root==None:
        return
    else:
        inOrderTraversal(root.left)
        print(root.val)
        inOrderTraversal(root.right)

root=None
root=insert(root,5)
root=insert(root,1)
root=insert(root,3)
root=insert(root,4)
print(kthSmallest(root,4))
