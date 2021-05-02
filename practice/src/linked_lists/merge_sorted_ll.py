class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def is_list_empty(self):
        if (self.head==None):
            return True
        else:
            return False

    def print_list(self):
        if (self.is_list_empty()):
            print("List is empty")
        else:
            current_node=self.head
            while(current_node!=None):
                print("Data Element is %d" %current_node.data)
                current_node=current_node.next

    def append(self,node):
        if (self.is_list_empty()):
            self.head=node
        else:
            current_node=self.head
            while(current_node.next!=None):
                current_node=current_node.next
            current_node.next=node

def merge_lists(head1,head2):
    if (head1==None):
        return head2
    if (head2==None):
        return head1
    if (head1.data<=head2.data):
        temp=head1
        temp.next=merge_lists(head1.next,head2)
    else:
        temp=head2
        temp.next=merge_lists(head1,head2.next)
    return temp

#Time Complexity : O(m+n)
#Auxililary Space Complexity: O(m+n)


list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))


list2 = LinkedList()
list2.append(Node(5))
list2.append(Node(15))
list2.append(Node(25))
list2.append(Node(35))
list2.append(Node(45))


list3 = LinkedList()


list3.head = merge_lists(list1.head, list2.head)

print(" Merged Linked List is : ", end="")
list3.print_list()
