class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class Solution:
    def rangeSumBST(self,root,low,high):
        a=[]
        self.inOrder(root,low,high,a)
        return sum(a)

    def inOrder(self,root,low,high,a):
        if root:
            self.inOrder(root.left,low,high,a)
            if root.val>=low and root.val<=high:
                a.append(root.val)
            self.inOrder(root.right,low,high,a)

    def insert(self,root,key):
        if root==None:
            return Node(key)
        else:
            if (key<=root.val):
                root.left=self.insert(root.left,key)
            else:
                root.right=self.insert(root.right,key)
        return root

    def inOrderTraversal(self,root):
        if root==None:
            return
        else:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)

S1=Solution()
root=None
root=S1.insert(root,7)
root=S1.insert(root,8)
root=S1.insert(root,2)
root=S1.insert(root,1)
S1.inOrderTraversal(root)
print(S1.rangeSumBST(root,2,8))
