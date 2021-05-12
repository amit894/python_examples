class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def removeNthFromEnd(head,n):
    totalNodes=countNodes(head)
    print(totalNodes)
    deleteNode(head,totalNodes-n+1)
    return head

def countNodes(head):
    if head==None:
        return 0
    else:
        count=0
        current_node=head
        while(current_node):
            count+=1
            current_node=current_node.next
        return count

def deleteNode(head,m):
    if head==None:
        return None
    else:
        count=0
        prev_node=None
        current_node=head
        while(current_node):
            if(count==m-1):
                break
            count+=1
            prev_node=current_node
            current_node=current_node.next
        if prev_node==None:
            head=current_node.next
        else:
            prev_node.next=current_node.next

head=Node(1)
removeNthFromEnd(head,1)
