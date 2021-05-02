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

    def contains_loop(self):
        s = set()
        if (self.is_list_empty()):
            return True
        else:
            current_node=self.head
            while(current_node!=None):
                if current_node in s:
                    return True
                else:
                    s.add(current_node)
                current_node=current_node.next

llist = LinkedList()
llist.append(Node(20))
llist.append(Node(4))
llist.append(Node(5))
llist.append(Node(10))

# Create a loop for testing
#llist.head.next.next.next.next = llist.head

if(llist.contains_loop()):
    print("Loop found")
else:
    print("No Loop ")
