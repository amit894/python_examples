class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inOrderTraversal(root):
    if(root):
        inOrderTraversal(root.left)
        print(root.data,end=" ")
        inOrderTraversal(root.right)

def insertNode(root,key):
    if root==None:
        return Node(key)
    else:
        if (key <root.data):
            root.left=insertNode(root.left,key)
        else :
            root.right=insertNode(root.right,key)
    return root

def minValueNode(root):
    if root==None:
        return
    else:
        current_node=root
        while(current_node):
            prev=current_node
            current_node=current_node.left
        return prev

def deleteNode(root,val):
    if root==None:
        return
    else:
        if (val<root.data):
            root.left=deleteNode(root.left,val)
            return root
        elif (val>root.data):
            root.right=deleteNode(root.right,val)
            return root
        else:
            if (root.left==None):
                temp=root.right
                root=None
                return temp
            elif (root.right==None):
                temp=root.left
                root=None
                return temp

            rightTreeMinNode=minValueNode(root.right)

            root.data=rightTreeMinNode.data
            root.right=deleteNode(root.right,rightTreeMinNode.data)
    return root


root=None
root=insertNode(root,50)
root=insertNode(root,60)
root=insertNode(root,40)
root=insertNode(root,20)
root=insertNode(root,30)
root=insertNode(root,70)
root=insertNode(root,80)

inOrderTraversal(root)
print("de limiter")
deleteNode(root, 20)
deleteNode(root, 30)
deleteNode(root, 50)
inOrderTraversal(root)
print("de limiter")
inOrderTraversal(root)
