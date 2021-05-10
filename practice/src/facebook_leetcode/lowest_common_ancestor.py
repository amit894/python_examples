class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def path_to_a_node(root,a,key):
    if root:
        a.append(root.val)
        if root.val==key:
            return True
        if ((root.left != None and path_to_a_node(root.left,a,key)) or
            (root.right!= None and path_to_a_node(root.right,a,key))):
            return True
        a.pop()
        return False

def findLCA(root, n1, n2):

    path1 = []
    path2 = []

    if (not path_to_a_node(root, path1, n1) or not path_to_a_node(root, path2, n2)):
        return -1

    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

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
